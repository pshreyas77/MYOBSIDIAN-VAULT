---
title: "Download stock portfolio"
date: 2026-03-27
tags:
  - sql
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - history
  - geopolitics
  - stock-market
  - research
  - creative
  - finance
source: claude-export
---

# Download stock portfolio

> **Conversation Overview**

The person asked Claude to download their stock portfolio. Claude attempted to use an MCP registry search tool to find a connected brokerage or portfolio tracking integration, but no such integration was available. Claude then provided manual instructions for how to export portfolio holdings from several Indian brokerage platforms, including Zerodha (Kite/Console), Groww, Upstox, and Angel One/ICICI Direct/HDFC Securities, explaining the navigation path for each. Claude offered to help analyze the portfolio once the person downloads and uploads the file, suggesting potential outputs such as performance breakdown, sector allocation, and P&L summary, and offered to build a portfolio analysis dashboard.

**Tool Knowledge**

Claude used the `search_mcp_registry` tool with keywords including "stocks," "portfolio," "investments," and "brokerage" to check for available integrations. The search returned no relevant connected tools, indicating that brokerage or investment platform integrations are not currently available in this environment. For future reference, when portfolio-related requests arise, Claude should immediately clarify that no direct brokerage connection exists and pivot to manual export guidance paired with an offer to analyze uploaded files.

**Date:** 2026-03-27  
**Topics:** [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[History]] · [[Geopolitics]] · [[Stock-Market]] · [[Research]] · [[Creative]] · [[Finance]]

---

### 🧑 You

download my total stock portfolio

---

### 🧑 You

download my total stock portfolio

---

### 🤖 Claude

I can help you pull your stock portfolio! Let me check what tools are available for this.

{'type': 'text', 'text': '{"results":[{"name":"LunarCrush","description":"Add real-time social media data to your searches","tools":["List","Cryptocurrencies","Stocks","Topic","Creator","Post","Topic_Time_Series","Topic_Posts","+3 more"],"url":"https://lunarcrush.ai/mcp","iconUrl":"https://lunarcrush.com","directoryUuid":"837cceff-9820-4510-823f-9bdc5ef21f3a","connected":false,"enabledInChat":false},{"name":"Asana","description":"Connect to Asana to coordinate tasks, projects, and goals","tools":["create_project_preview","create_task_preview","search_tasks_preview","get_status_overview","get_items_for_portfolio","get_portfolio","get_portfolios","get_project","+7 more"],"url":"https://mcp.asana.com/v2/mcp","iconUrl":"https://mcp.asana.com/v2/mcp","directoryUuid":"41aefcf3-a829-45eb-8cee-d90b93912f57","connected":false,"enabledInChat":false},{"name":"CB Insights","description":"Predictive intelligence on private companies","tools":["api_chatcbi","api_rag","company_advanced_search","get_company_acquisitions","get_company_competitors","get_company_exits","get_company_funding","get_company_investments","+7 more"],"url":"https://mcp.cbinsights.com","iconUrl":"https://www.cbinsights.com","directoryUuid":"e7952077-b4e6-49f7-8670-ca53f8d50c40","connected":false,"enabledInChat":false},{"name":"PitchBook Premium","description":"PitchBook data, embedded in the way you work.","tools":["pitchbook_search","pitchbook_get_profile","pitchbook_get_company_deals","pitchbook_get_company_investors","pitchbook_get_company_financials","pitchbook_get_investor_investments","pitchbook_get_deal_participants","pitchbook_get_deal_cap_table","+3 more"],"url":"https://premium.mcp.pitchbook.com/mcp","iconUrl":"https://www.pitchbook.com","directoryUuid":"79c545e3-8878-4557-bcbb-3add11c86890","connected":false,"enabledInChat":false},{"name":"Chronograph","description":"Interact with your Chronograph data directly in Claude","tools":["query-help-center-documentation","get-help-center-article","top-exposures","run-query","entity-search","commitment-history","investment-metrics"],"url":"https://ai.chronograph.pe/mcp","iconUrl":"https://www.chronograph.pe/","directoryUuid":"01744591-790c-471b-9452-f338eff230af","connected":false,"enabledInChat":false},{"name":"Morningstar","description":"Up-to-date investment and market insights","tools":["morningstar-id-lookup-tool","morningstar-data-tool","morningstar-analyst-research-tool","morningstar-articles-tool","morningstar-screener-tool","morningstar-fund-holdings-tool"],"url":"https://mcp.morningstar.com/mcp","iconUrl":"https://www.morningstar.com/","directoryUuid":"2e98be30-8dba-486e-94a9-9a01d34678e2","connected":false,"enabledInChat":false},{"name":"Yardi Virtuoso","description":"Real-time Yardi data & insights","tools":["rfm_connectai_create_work_order","rfm_connectai_search_work_orders","rfm_workorder_mark_work_order_as_complete","vn_mcpframework_get_autocomplete","vn_mcpframework_list_autocomplete_types"],"url":"https://mcp.virtuoso.ai/mcp","iconUrl":"https://yardi.com","directoryUuid":"01953ddd-4139-40c5-bbf9-47c1e2499623","connected":false,"enabledInChat":false},{"name":"MSCI","description":"Turn data into insight","tools":["execute_index_gql_schema","get_index_gql_schema_fragments","get_pci_measure_detail","get_pci_user_profiles","get_pci_help"],"url":"https://mcp.msci.com/mcp/v1.0/mcp","iconUrl":"https://msci.com","directoryUuid":"2cc10749-99cb-4853-a9d7-b2292ec589fc","connected":false,"enabledInChat":false},{"name":"Intapp Celeste","description":"Securely, compliantly access Intapp Celeste products","tools":["dc_list_objects","dc_list_fields","dc_find_records","dc_entry","dc_lookup","dc_aggregate","dc_check_duplicates","dc_create_record","+9 more"],"iconUrl":"https://intapp.com","directoryUuid":"dd9a36b4-e356-4ca5-a771-d979e8a898c6","connected":false,"enabledInChat":false},{"name":"Clarity AI","description":"Simulate fund classifications under proposed SFDR 2.0","tools":["search_securities","sfdr20_check","sfdr20_check_by_query","interpret_sfdr20_result"],"url":"https://clarity-sfdr20-mcp.pro.clarity.ai/mcp","iconUrl":"https://clarity.ai","directoryUuid":"3bb23b8e-f796-4156-991b-e3f4e0b25fff","connected":false,"enabledInChat":false}]}', 'uuid': 'd3734adf-980e-4d8d-b642-a11a750a8aaa'}
Unfortunately, there's no connected brokerage or portfolio tracking integration available (like Zerodha, Groww, Upstox, etc.) that could pull your holdings directly.

To download your stock portfolio, here are your best options depending on where you hold it:

**Zerodha (Kite)**
- Log in → Console → Portfolio → Holdings → Export as CSV

**Groww**
- Login → Stocks → Portfolio → Download (top right)

**Upstox**
- Login → Portfolio → Holdings → Export

**Angel One / ICICI Direct / HDFC Securities**
- Similar path: Portfolio → Holdings → Export/Download

Once you download the CSV or Excel file from your broker, you can upload it here and I can help you analyze it — performance breakdown, sector allocation, P&L summary, anything you need. Want me to build a portfolio analysis dashboard once you have the file?

---
