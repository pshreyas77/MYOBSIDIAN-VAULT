---
source_file: "genericagent/llmcore.py"
type: "code"
community: "Community None"
location: "L517"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_None
---

# LLMSession

## Connections
- [[.make_messages()_1]] - `method` [EXTRACTED]
- [[.raw_ask()_1]] - `method` [EXTRACTED]
- [[think tags (used by MiniMax M2.7) should be stripped from content.]] - `uses` [INFERRED]
- [[think tags in old messages should be truncated.]] - `uses` [INFERRED]
- [[think tags should be separated from tool_use blocks.]] - `uses` [INFERRED]
- [[thinking tags (used by Claude) should still work.]] - `uses` [INFERRED]
- [[BaseSession]] - `inherits` [EXTRACTED]
- [[Build a mock SSE HTTP response from a list of text chunks.]] - `uses` [INFERRED]
- [[Capture the payload sent by _openai_stream.]] - `uses` [INFERRED]
- [[End-to-end integration test LLMSession + ToolClient + MiniMax streaming.]] - `uses` [INFERRED]
- [[Full ToolClient pipeline with real MiniMax API.]] - `uses` [INFERRED]
- [[Full pipeline LLMSession → _openai_stream → ToolClient parse with think tag.]] - `uses` [INFERRED]
- [[Full pipeline MiniMax response with tool_use block.]] - `uses` [INFERRED]
- [[GeneraticAgent]] - `uses` [INFERRED]
- [[Integration tests for MiniMax provider support.  These tests verify end-to-end M]] - `uses` [INFERRED]
- [[KimiMoonshot temp override should still work.]] - `uses` [INFERRED]
- [[LLMSession should initialize correctly with MiniMax config.]] - `uses` [INFERRED]
- [[LLMSession should work with MiniMax-M2.7-highspeed model.]] - `uses` [INFERRED]
- [[Live integration tests against MiniMax API (requires MINIMAX_API_KEY).]] - `uses` [INFERRED]
- [[MiniMax rejects temperature=0, should be clamped to 0.01.]] - `uses` [INFERRED]
- [[Model name matching should be case-insensitive.]] - `uses` [INFERRED]
- [[NativeOAISession.ask should extract think tags from MiniMax M2.7 responses.]] - `uses` [INFERRED]
- [[NativeToolClient should extract think tags from MiniMax responses.]] - `uses` [INFERRED]
- [[Negative temperature should be clamped to 0.01.]] - `uses` [INFERRED]
- [[Non-MiniMax models should not have temperature clamped.]] - `uses` [INFERRED]
- [[Normal temperature (0  t = 1) should be preserved.]] - `uses` [INFERRED]
- [[Send a real chat completion to MiniMax API.]] - `uses` [INFERRED]
- [[Temperature  1.0 should be clamped to 1.0.]] - `uses` [INFERRED]
- [[Temperature=1.0 should be preserved.]] - `uses` [INFERRED]
- [[Test think tag handling in NativeOAISession.]] - `uses` [INFERRED]
- [[Test think tag handling in NativeToolClient.chat.]] - `uses` [INFERRED]
- [[Test think...think tag stripping for MiniMax M2.7 responses.]] - `uses` [INFERRED]
- [[Test LLMSession configuration with MiniMax settings.]] - `uses` [INFERRED]
- [[Test MiniMax temperature clamping in _openai_stream.]] - `uses` [INFERRED]
- [[Test URL construction for MiniMax API base.]] - `uses` [INFERRED]
- [[Test that think tags are compressed in history like thinking tags.]] - `uses` [INFERRED]
- [[TestMiniMaxAutoMakeUrl]] - `uses` [INFERRED]
- [[TestMiniMaxCompressHistoryTags]] - `uses` [INFERRED]
- [[TestMiniMaxEndToEnd]] - `uses` [INFERRED]
- [[TestMiniMaxLLMSessionConfig]] - `uses` [INFERRED]
- [[TestMiniMaxLive]] - `uses` [INFERRED]
- [[TestMiniMaxNativeOAISessionThinkTag]] - `uses` [INFERRED]
- [[TestMiniMaxNativeToolClientThinkTag]] - `uses` [INFERRED]
- [[TestMiniMaxTemperatureClamping]] - `uses` [INFERRED]
- [[TestMiniMaxThinkTagHandling]] - `uses` [INFERRED]
- [[Unit tests for MiniMax provider support in llmcore.py.]] - `uses` [INFERRED]
- [[Verify streaming works with MiniMax API.]] - `uses` [INFERRED]
- [[Verify the actual HTTP request has clamped temperature for MiniMax.]] - `uses` [INFERRED]
- [[llmcore.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_None