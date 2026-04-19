#!/usr/bin/env python3
"""
Claude API Client
Integrates with Anthropic's Claude models
"""

import json
from datetime import datetime
from typing import List, Dict, Optional, Callable
import anthropic
from config import Config


class ClaudeClient:
    """Client for Anthropic Claude API"""

    def __init__(self):
        self.client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)
        self.model = Config.CLAUDE_MODEL
        self.max_tokens = Config.MAX_TOKENS
        self.messages: List[Dict] = []
        self.tools: List[Dict] = []
        self.tool_handlers: Dict[str, Callable] = {}
        self.system_prompt = Config.SYSTEM_PROMPT

    def add_tool(self, name: str, description: str, parameters: Dict, handler: Callable):
        """Register a tool that Claude can use"""
        self.tools.append({
            "name": name,
            "description": description,
            "input_schema": {
                "type": "object",
                "properties": parameters,
                "required": list(parameters.keys())
            }
        })
        self.tool_handlers[name] = handler

    def clear_history(self):
        """Clear conversation history"""
        self.messages = []

    def add_to_memory(self, role: str, content: str):
        """Add message to conversation history"""
        self.messages.append({"role": role, "content": content})

        # Trim if too long
        if len(self.messages) > Config.MAX_MEMORY_ENTRIES:
            self.messages = self.messages[-Config.MAX_MEMORY_ENTRIES:]

    def chat(self, user_input: str, use_tools: bool = True) -> str:
        """Send message to Claude and get response"""
        self.add_to_memory("user", user_input)

        try:
            # Prepare message
            messages = []
            for msg in self.messages:
                if msg["role"] == "user":
                    messages.append({"role": "user", "content": msg["content"]})
                else:
                    messages.append({"role": "assistant", "content": msg["content"]})

            # Create request
            kwargs = {
                "model": self.model,
                "max_tokens": self.max_tokens,
                "system": self.system_prompt,
                "messages": messages,
                "temperature": 0.7
            }

            if use_tools and self.tools:
                kwargs["tools"] = self.tools
                kwargs["tool_choice"] = {"type": "auto"}

            # Get response
            response = self.client.messages.create(**kwargs)

            # Handle response
            content_text = ""
            tool_calls = []

            for content_block in response.content:
                if content_block.type == "text":
                    content_text += content_block.text
                elif content_block.type == "tool_use":
                    tool_calls.append({
                        "name": content_block.name,
                        "input": content_block.input,
                        "id": content_block.id
                    })

            # Execute tools if any
            if tool_calls:
                results = self._execute_tools(tool_calls)

                # Send results back to Claude
                results_msg = "Tool results:\n"
                for result in results:
                    results_msg += f"- {result['name']}: {result['result']}\n"

                messages.append({"role": "assistant", "content": content_text})
                messages.append({"role": "user", "content": results_msg})

                final_response = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    system=self.system_prompt,
                    messages=messages
                )
                content_text = final_response.content[0].text

            self.add_to_memory("assistant", content_text)
            return content_text

        except anthropic.APIError as e:
            return f"API Error: {e.message}"
        except Exception as e:
            if Config.DEBUG_MODE:
                import traceback
                traceback.print_exc()
            return f"Error communicating with Claude: {str(e)}"

    def _execute_tools(self, tool_calls: List[Dict]) -> List[Dict]:
        """Execute tool calls and return results"""
        results = []

        for call in tool_calls:
            try:
                name = call["name"]
                inputs = call["input"]

                if name in self.tool_handlers:
                    result = self.tool_handlers[name](**inputs)
                    results.append({
                        "name": name,
                        "result": str(result),
                        "success": True
                    })
                else:
                    results.append({
                        "name": name,
                        "result": f"Tool '{name}' not found",
                        "success": False
                    })
            except Exception as e:
                results.append({
                    "name": call["name"],
                    "result": f"Error: {str(e)}",
                    "success": False
                })

        return results

    def get_token_count(self, text: str) -> int:
        """Estimate token count (approximate)"""
        return len(text) // 4

    def stream_chat(self, user_input: str):
        """Stream response from Claude"""
        self.add_to_memory("user", user_input)

        try:
            messages = [{"role": m["role"], "content": m["content"]} for m in self.messages]

            with self.client.messages.stream(
                model=self.model,
                max_tokens=self.max_tokens,
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


if __name__ == "__main__":
    # Test client
    client = ClaudeClient()
    response = client.chat("Hello, who are you?")
    print(response)