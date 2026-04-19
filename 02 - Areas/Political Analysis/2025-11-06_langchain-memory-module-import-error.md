---
title: "Langchain memory module import error"
date: 2025-11-06
tags:
  - python
  - llm-ai
  - linux
  - history
  - geopolitics
  - creative
source: claude-export
---

# Langchain memory module import error

**Date:** 2025-11-06  
**Topics:** [[Python]] · [[LLM-AI]] · [[Linux]] · [[History]] · [[Geopolitics]] · [[Creative]]

---

### 🧑 You

(myenv) PS C:\Users\shrey\Documents\open-source-agent> python app.py
C:\Users\shrey\Documents\open-source-agent\myenv\Lib\site-packages\langchain_core\_api\deprecation.py:26: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
  from pydantic.v1.fields import FieldInfo as FieldInfoV1
Traceback (most recent call last):
  File "C:\Users\shrey\Documents\open-source-agent\app.py", line 6, in <module>
    from langchain.memory import ConversationBufferMemory
ModuleNotFoundError: No module named 'langchain.memory'


i am getting this error when trying to run the app.py file

---

### 🤖 Claude

The error occurs because `langchain.memory` has been moved or removed in newer versions of LangChain. The code already has a fallback implementation, but the import statement is still trying to import from the old location first.

Here's the fix - update the import section around line 24-42 in your `app.py`:

```python
# Compatibility wrapper for ConversationBufferMemory in langchain 1.0+
try:
    from langchain_community.memory import ConversationBufferMemory
except ImportError:
    try:
        from langchain.memory import ConversationBufferMemory
    except ImportError:
        from typing import Any
        class ConversationBufferMemory:
            def __init__(self, memory_key: str = 'chat_history', output_key: str = 'answer', 
                         return_messages: bool = True, chat_memory: Any = None):
                self.memory_key = memory_key
                self.output_key = output_key
                self.return_messages = return_messages
                self.chat_memory = chat_memory or ChatMessageHistory()
                
            def load_memory_variables(self, inputs: dict) -> dict:
                return {self.memory_key: self.chat_memory.messages}
            
            def save_context(self, inputs: dict, outputs: dict) -> None:
                if self.return_messages:
                    if 'question' in inputs:
                        self.chat_memory.add_user_message(inputs['question'])
                    if self.output_key in outputs:
                        self.chat_memory.add_ai_message(outputs[self.output_key])
            
            @property
            def memory_variables(self) -> list:
                return [self.memory_key]
```

The key change is trying `langchain_community.memory` first before falling back to `langchain.memory`, and then finally using the custom implementation if both fail.

Alternatively, if you want a cleaner solution, you could install the missing package:

```bash
pip install langchain-community
```

Then the code should work with the modified import order above. This is the recommended approach since `langchain-community` is where many of the moved modules now reside.

---

### 🧑 You

can you edit the code and give me a new app.py

---

### 🧑 You

Continue

---
