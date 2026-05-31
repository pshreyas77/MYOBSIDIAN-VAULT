#!/usr/bin/env python3
"""
Generic LLM Client - Supports multiple free backends
- Ollama (local, completely free)
- OpenAI-compatible APIs (NVIDIA, DeepSeek, etc)
- Anthropic Claude (if API key available)
"""

import json
import re
from datetime import datetime
from typing import List, Dict, Optional, Callable, Generator
from config import Config


class LLMClient:
    """Universal LLM client supporting multiple backends"""

    def __init__(self, backend: str = "auto"):
        """
        Initialize LLM client
        backend: "ollama", "anthropic", "openai", or "auto" (try in order)
        """
        self.backend = backend
        self.client = None
        self.model = None
        self.messages: List[Dict] = []
        self.tools: List[Dict] = []
        self.tool_handlers: Dict[str, Callable] = {}
        self.system_prompt = Config.SYSTEM_PROMPT

        self._init_backend()

    def _init_backend(self):
        """Try to initialize available backend"""
        if self.backend == "auto":
            # Try in order: Ollama (free) > Anthropic > OpenAI compatible
            if self._try_ollama():
                print(f"      ✓ Using Ollama (local/)")
            elif self._try_anthropic():
                print(f"      ✓ Using Claude")
            elif self._try_openai():
                print(f"      ✓ Using OpenAI-compatible API")
            else:
                raise RuntimeError("No LLM backend available! Install Ollama or set API keys.")
        elif self.backend == "ollama":
            self._try_ollama()
        elif self.backend == "anthropic":
            self._try_anthropic()
        elif self.backend == "openai":
            self._try_openai()

    def _try_ollama(self) -> bool:
        """Try to connect to local Ollama instance"""
        try:
            import requests
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            if response.status_code == 200:
                self.backend_type = "ollama"
                self.model = Config.OLLAMA_MODEL
                return True
        except:
            pass
        return False

    def _try_anthropic(self) -> bool:
        """Try to initialize Anthropic client"""
        if not Config.ANTHROPIC_API_KEY:
            return False
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)
            self.backend_type = "anthropic"
            self.model = Config.CLAUDE_MODEL
            return True
        except:
            return False

    def _try_openai(self) -> bool:
        """Try to initialize OpenAI-compatible client"""
        if not Config.OPENAI_API_KEY:
            return False
        try:
            import openai
            self.client = openai.OpenAI(
                api_key=Config.OPENAI_API_KEY,
                base_url=Config.OPENAI_BASE_URL
            )
            self.backend_type = "openai"
            self.model = Config.OPENAI_MODEL
            return True
        except:
            return False

    def add_tool(self, name: str, description: str, parameters: Dict, handler: Callable):
        """Register a tool"""
        # Format for different backends
        if self.backend_type == "anthropic":
            # Anthropic format
            self.tools.append({
                "name": name,
                "description": description,
                "input_schema": {
                    "type": "object",
                    "properties": parameters,
                    "required": list(parameters.keys())
                }
            })
        else:
            # OpenAI format (also used by Ollama)
            self.tools.append({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": {
                        "type": "object",
                        "properties": parameters,
                        "required": list(parameters.keys())
                    }
                }
            })
        self.tool_handlers[name] = handler

    def clear_history(self):
        """Clear conversation history"""
        self.messages = []

    def add_to_memory(self, role: str, content: str):
        """Add message to history"""
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > Config.MAX_MEMORY_ENTRIES:
            self.messages = self.messages[-Config.MAX_MEMORY_ENTRIES:]

    def chat(self, user_input: str, use_tools: bool = True) -> str:
        """Send message and get response"""
        self.add_to_memory("user", user_input)

        if self.backend_type == "ollama":
            return self._chat_ollama(use_tools)
        elif self.backend_type == "anthropic":
            return self._chat_anthropic(use_tools)
        elif self.backend_type == "openai":
            return self._chat_openai(use_tools)
        else:
            return "Error: No backend available"

    def _chat_ollama(self, use_tools: bool) -> str:
        """Chat using Ollama (local)"""
        import requests

        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend([{"role": m["role"], "content": m["content"]} for m in self.messages])

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": 0.7
            }
        }

        if use_tools and self.tools:
            # Ollama tool support
            payload["tools"] = self.tools

        try:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json=payload,
                timeout=300
            )
            response.raise_for_status()
            data = response.json()

            content = data.get("message", {}).get("content", "")

            # Handle tool calls
            if "tool_calls" in data.get("message", {}):
                tool_calls = data["message"]["tool_calls"]
                results = self._execute_tools_ollama(tool_calls)

                # Add to messages and get final response
                messages.append({"role": "assistant", "content": content})
                messages.append({"role": "user", "content": f"Tool results: {json.dumps(results)}"})

                payload["messages"] = messages
                response = requests.post(
                    "http://localhost:11434/api/chat",
                    json=payload,
                    timeout=300
                )
                data = response.json()
                content = data.get("message", {}).get("content", "")

            self.add_to_memory("assistant", content)
            return content

        except Exception as e:
            return f"Ollama error: {str(e)}. Make sure Ollama is running: 'ollama serve'"

    def _chat_anthropic(self, use_tools: bool) -> str:
        """Chat using Anthropic"""
        messages = []
        for msg in self.messages:
            messages.append({"role": msg["role"], "content": msg["content"]})

        kwargs = {
            "model": self.model,
            "max_tokens": Config.MAX_TOKENS,
            "system": self.system_prompt,
            "messages": messages,
            "temperature": 0.7
        }

        if use_tools and self.tools:
            kwargs["tools"] = self.tools
            kwargs["tool_choice"] = {"type": "auto"}

        try:
            response = self.client.messages.create(**kwargs)

            content_text = ""
            tool_calls = []

            for content_block in response.content:
                if content_block.type == "text":
                    content_text += content_block.text
                elif content_block.type == "tool_use":
                    tool_calls.append({
                        "name": content_block.name,
                        "input": content_block.input
                    })

            if tool_calls:
                results = self._execute_tools_anthropic(tool_calls)
                messages.append({"role": "assistant", "content": content_text})
                messages.append({"role": "user", "content": f"Tool results: {json.dumps(results)}"})

                final_response = self.client.messages.create(
                    model=self.model,
                    max_tokens=Config.MAX_TOKENS,
                    system=self.system_prompt,
                    messages=messages
                )
                content_text = final_response.content[0].text

            self.add_to_memory("assistant", content_text)
            return content_text

        except Exception as e:
            return f"Claude error: {str(e)}"

    def _chat_openai(self, use_tools: bool) -> str:
        """Chat using OpenAI-compatible API"""
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend([{"role": m["role"], "content": m["content"]} for m in self.messages])

        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": Config.MAX_TOKENS
        }

        if use_tools and self.tools:
            kwargs["tools"] = self.tools
            kwargs["tool_choice"] = "auto"

        try:
            response = self.client.chat.completions.create(**kwargs)
            message = response.choices[0].message
            content = message.content

            if message.tool_calls:
                results = self._execute_tools_openai(message.tool_calls)
                messages.append({"role": "assistant", "content": content or ""})
                messages.append({"role": "user", "content": f"Tool results: {json.dumps(results)}"})

                kwargs["messages"] = messages
                final_response = self.client.chat.completions.create(**kwargs)
                content = final_response.choices[0].message.content

            self.add_to_memory("assistant", content)
            return content

        except Exception as e:
            return f"API error: {str(e)}"

    def _execute_tools_ollama(self, tool_calls):
        """Execute tools for Ollama"""
        results = []
        for call in tool_calls:
            try:
                func = call.get("function", {})
                name = func.get("name")
                args = json.loads(func.get("arguments", "{}"))
                if name in self.tool_handlers:
                    result = self.tool_handlers[name](**args)
                    results.append({"name": name, "result": str(result)})
            except Exception as e:
                results.append({"error": str(e)})
        return results

    def _execute_tools_anthropic(self, tool_calls):
        """Execute tools for Anthropic"""
        results = []
        for call in tool_calls:
            try:
                name = call["name"]
                inputs = call["input"]
                if name in self.tool_handlers:
                    result = self.tool_handlers[name](**inputs)
                    results.append({"name": name, "result": str(result)})
            except Exception as e:
                results.append({"error": str(e)})
        return results

    def _execute_tools_openai(self, tool_calls):
        """Execute tools for OpenAI"""
        results = []
        for call in tool_calls:
            try:
                name = call.function.name
                args = json.loads(call.function.arguments)
                if name in self.tool_handlers:
                    result = self.tool_handlers[name](**args)
                    results.append({"name": name, "result": str(result)})
            except Exception as e:
                results.append({"error": str(e)})
        return results

    def stream_chat(self, user_input: str) -> Generator[str, None, None]:
        """Stream response"""
        self.add_to_memory("user", user_input)

        if self.backend_type == "anthropic":
            messages = [{"role": m["role"], "content": m["content"]} for m in self.messages]
            try:
                with self.client.messages.stream(
                    model=self.model,
                    max_tokens=Config.MAX_TOKENS,
                    system=self.system_prompt,
                    messages=messages
                ) as stream:
                    full_response = ""
                    for text in stream.text_stream:
                        full_response += text
                        yield text
                    self.add_to_memory("assistant", full_response)
            except Exception as e:
                yield f"Error: {str(e)}"
        else:
            # Non-streaming fallback for other backends
            response = self.chat(user_input)
            yield response


if __name__ == "__main__":
    client = LLMClient()
    print(f"Backend: {client.backend_type}")
    print(client.chat("Hello, who are you?"))