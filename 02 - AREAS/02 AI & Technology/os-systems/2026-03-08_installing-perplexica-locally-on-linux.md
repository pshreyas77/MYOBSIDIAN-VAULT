---
title: "Installing Perplexica locally on Linux"
date: 2026-03-08
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
  - web-dev
  - game-design
source: claude-export
---

# Installing Perplexica locally on Linux

> **Conversation Overview**

The person asked for help installing and running Perplexica (an open-source, privacy-focused AI search engine from https://github.com/ItzCrazyKns/Perplexica) locally on a Linux system for free. Claude provided a comprehensive overview of installation methods, then the person requested a more detailed Docker-focused walkthrough. Claude delivered a step-by-step Docker guide covering: installing Docker, installing Ollama with a free local model, exposing Ollama to Docker by editing the systemd service file, running the Perplexica container, and configuring it via the browser UI at localhost:3000.

The person successfully pulled the `phi3` model via Ollama (suitable for systems with around 4GB RAM), then encountered an issue where they accidentally pasted instructional text directly into the terminal instead of only running the `sudo nano` command. This caused shell errors like `Command 'Find' not found` and `[Service]: command not found`. Claude diagnosed the mistake and provided a corrected, isolated command to open the Ollama service file properly, along with clear nano editor instructions for adding `Environment="OLLAMA_HOST=0.0.0.0:11434"` under the `[Service]` section. The conversation ended at this troubleshooting step, with the person mid-process configuring Ollama's network binding. The Linux-specific requirement to bind Ollama to `0.0.0.0` rather than `localhost` was emphasized as a critical step for Docker container connectivity.

**Date:** 2026-03-08  
**Topics:** [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[History]] · [[Geopolitics]] · [[Stock-Market]] · [[Research]] · [[Creative]] · [[Finance]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

how to install and run perplexcika in my linux system and run it locally for free  https://github.com/ItzCrazyKns/Perplexica.git

---

### 🤖 Claude

{'type': 'text', 'text': '{"error_type": "PERMISSIONS_ERROR", "error_message": "This URL cannot be fetched because it was not provided by the user nor did it appear in any search/fetch results"}', 'uuid': 'ad2bce19-bae0-4ac8-9aa7-303b4b14ac6f'}

{'type': 'knowledge', 'title': 'GitHub - ItzCrazyKns/Perplexica: Perplexica is an AI-powered answering engine.', 'url': 'https://github.com/ItzCrazyKns/Perplexica.git', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'github'}, 'is_missing': False, 'text': 'GitHub - ItzCrazyKns/Perplexica: Perplexica is an AI-powered answering engine. · GitHub\n\n\n\n[Skip to content](#start-of-content)\n\n\n\n\n\n\n\n\n\n\n\n\n\n## Navigation Menu\n\nToggle navigation\n\n[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FItzCrazyKns%2FPerplexica)\n\nAppearance settings\n\n* Platform\n\n  + AI CODE CREATION\n    - [GitHub CopilotWrite better code with AI](https://github.com/features/copilot)\n    - [GitHub SparkBuild and deploy intelligent apps](https://github.com/features/spark)\n    - [GitHub ModelsManage and compare prompts](https://github.com/features/models)\n    - [MCP RegistryNewIntegrate external tools](https://github.com/mcp)\n  + DEVELOPER WORKFLOWS\n    - [ActionsAutomate any workflow](https://github.com/features/actions)\n    - [CodespacesInstant dev environments](https://github.com/features/codespaces)\n    - [IssuesPlan and track work](https://github.com/features/issues)\n    - [Code ReviewManage code changes](https://github.com/features/code-review)\n  + APPLICATION SECURITY\n    - [GitHub Advanced SecurityFind and fix vulnerabilities](https://github.com/security/advanced-security)\n    - [Code securitySecure your code as you build](https://github.com/security/advanced-security/code-security)\n    - [Secret protectionStop leaks before they start](https://github.com/security/advanced-security/secret-protection)\n  + EXPLORE\n    - [Why GitHub](https://github.com/why-github)\n    - [Documentation](https://docs.github.com)\n    - [Blog](https://github.blog)\n    - [Changelog](https://github.blog/changelog)\n    - [Marketplace](https://github.com/marketplace)\n\n  [View all features](https://github.com/features)\n* Solutions\n\n  + BY COMPANY SIZE\n    - [Enterprises](https://github.com/enterprise)\n    - [Small and medium teams](https://github.com/team)\n    - [Startups](https://github.com/enterprise/startups)\n    - [Nonprofits](https://github.com/solutions/industry/nonprofits)\n  + BY USE CASE\n    - [App Modernization](https://github.com/solutions/use-case/app-modernization)\n    - [DevSecOps](https://github.com/solutions/use-case/devsecops)\n    - [DevOps](https://github.com/solutions/use-case/devops)\n    - [CI/CD](https://github.com/solutions/use-case/ci-cd)\n    - [View all use cases](https://github.com/solutions/use-case)\n  + BY INDUSTRY\n    - [Healthcare](https://github.com/solutions/industry/healthcare)\n    - [Financial services](https://github.com/solutions/industry/financial-services)\n    - [Manufacturing](https://github.com/solutions/industry/manufacturing)\n    - [Government](https://github.com/solutions/industry/government)\n    - [View all industries](https://github.com/solutions/industry)\n\n  [View all solutions](https://github.com/solutions)\n* Resources\n\n  + EXPLORE BY TOPIC\n    - [AI](https://github.com/resources/articles?topic=ai)\n    - [Software Development](https://github.com/resources/articles?topic=software-development)\n    - [DevOps](https://github.com/resources/articles?topic=devops)\n    - [Security](https://github.com/resources/articles?topic=security)\n    - [View all topics](https://github.com/resources/articles)\n  + EXPLORE BY TYPE\n    - [Customer stories](https://github.com/customer-stories)\n    - [Events & webinars](https://github.com/resources/events)\n    - [Ebooks & reports](https://github.com/resources/whitepapers)\n    - [Business insights](https://github.com/solutions/executive-insights)\n    - [GitHub Skills](https://skills.github.com)\n  + SUPPORT & SERVICES\n    - [Documentation](https://docs.github.com)\n    - [Customer support](https://support.github.com)\n    - [Community forum](https://github.com/orgs/community/discussions)\n    - [Trust center](https://github.com/trust-center)\n    - [Partners](https://github.com/partners)\n\n  [View all resources](https://github.com/resources)\n* Open Source\n\n  + COMMUNITY\n    - [GitHub SponsorsFund open source developers](https://github.com/sponsors)\n  + PROGRAMS\n    - [Security Lab](https://securitylab.github.com)\n    - [Maintainer Community](https://maintainers.github.com)\n    - [Accelerator](https://github.com/accelerator)\n    - [Archive Program](https://archiveprogram.github.com)\n  + REPOSITORIES\n    - [Topics](https://github.com/topics)\n    - [Trending](https://github.com/trending)\n    - [Collections](https://github.com/collections)\n* Enterprise\n\n  + ENTERPRISE SOLUTIONS\n    - [Enterprise platformAI-powered developer platform](https://github.com/enterprise)\n  + AVAILABLE ADD-ONS\n    - [GitHub Advanced SecurityEnterprise-grade security features](https://github.com/security/advanced-security)\n    - [Copilot for BusinessEnterprise-grade AI features](https://github.com/features/copilot/copilot-business)\n    - [Premium SupportEnterprise-grade 24/7 support](https://github.com/premium-support)\n* [Pricing](https://github.com/pricing)\n\nSearch or jump to...\n\n\n# Search code, repositories, users, issues, pull requests...\n\nSearch\n\nClear\n\n[Search syntax tips](https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax)\n\n# Provide feedback\n\nWe read every piece of feedback, and take your input very seriously.\n\n\nInclude my email address so I can be contacted\n\nCancel\n Submit feedback\n\n\n\n\n\n# Saved searches\n\n## Use saved searches to filter your results more quickly\n\nName\n\nQuery\n\nTo see all available qualifiers, see our [documentation](https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax).\n\nCancel\n Create saved search\n\n[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FItzCrazyKns%2FPerplexica)\n\n[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=ItzCrazyKns%2FPerplexica)\n\nAppearance settings\n\nResetting focus\n\nYou signed in with another tab or window. Reload to refresh your session.\nYou signed out in another tab or window. Reload to refresh your session.\nYou switched accounts on another tab or window. Reload to refresh your session.\n \n\n\nDismiss alert\n\n{{ message }}\n\n[ItzCrazyKns](/ItzCrazyKns) \n/\n**[Perplexica](/ItzCrazyKns/Perplexica)**\nPublic\n\n* [Notifications](/login?return_to=%2FItzCrazyKns%2FPerplexica) You must be signed in to change notification settings\n* [Fork\n  3.4k](/login?return_to=%2FItzCrazyKns%2FPerplexica)\n* [Star\n   32.1k](/login?return_to=%2FItzCrazyKns%2FPerplexica)\n\n* [Code](/ItzCrazyKns/Perplexica)\n* [Issues\n  182](/ItzCrazyKns/Perplexica/issues)\n* [Pull requests\n  70](/ItzCrazyKns/Perplexica/pulls)\n* [Discussions](/ItzCrazyKns/Perplexica/discussions)\n* [Actions](/ItzCrazyKns/Perplexica/actions)\n* [Projects](/ItzCrazyKns/Perplexica/projects)\n* [Security\n  0](/ItzCrazyKns/Perplexica/security)\n* [Insights](/ItzCrazyKns/Perplexica/pulse)\n\nAdditional navigation options\n\n\n* [Code](/ItzCrazyKns/Perplexica)\n* [Issues](/ItzCrazyKns/Perplexica/issues)\n* [Pull requests](/ItzCrazyKns/Perplexica/pulls)\n* [Discussions](/ItzCrazyKns/Perplexica/discussions)\n* [Actions](/ItzCrazyKns/Perplexica/actions)\n* [Projects](/ItzCrazyKns/Perplexica/projects)\n* [Security](/ItzCrazyKns/Perplexica/security)\n* [Insights](/ItzCrazyKns/Perplexica/pulse)\n\n# ItzCrazyKns/Perplexica\n\nmaster\n\n[Branches](/ItzCrazyKns/Perplexica/branches)[Tags](/ItzCrazyKns/Perplexica/tags)\n\nGo to file\n\nCode\n\nOpen more actions menu\n\n## Folders and files\n\n| Name | | Name | Last commit message | Last commit date |\n| --- | --- | --- | --- | --- |\n| Latest commit   History[967 Commits](/ItzCrazyKns/Perplexica/commits/master/)   967 Commits | | |\n| [.assets](/ItzCrazyKns/Perplexica/tree/master/.assets ".assets") | | [.assets](/ItzCrazyKns/Perplexica/tree/master/.assets ".assets") |  |  |\n| [.github](/ItzCrazyKns/Perplexica/tree/master/.github ".github") | | [.github](/ItzCrazyKns/Perplexica/tree/master/.github ".github") |  |  |\n| [data](/ItzCrazyKns/Perplexica/tree/master/data "data") | | [data](/ItzCrazyKns/Perplexica/tree/master/data "data") |  |  |\n| [docs](/ItzCrazyKns/Perplexica/tree/master/docs "docs") | | [docs](/ItzCrazyKns/Perplexica/tree/master/docs "docs") |  |  |\n| [drizzle](/ItzCrazyKns/Perplexica/tree/master/drizzle "drizzle") | | [drizzle](/ItzCrazyKns/Perplexica/tree/master/drizzle "drizzle") |  |  |\n| [public](/ItzCrazyKns/Perplexica/tree/master/public "public") | | [public](/ItzCrazyKns/Perplexica/tree/master/public "public") |  |  |\n| [searxng](/ItzCrazyKns/Perplexica/tree/master/searxng "searxng") | | [searxng](/ItzCrazyKns/Perplexica/tree/master/searxng "searxng") |  |  |\n| [src](/ItzCrazyKns/Perplexica/tree/master/src "src") | | [src](/ItzCrazyKns/Perplexica/tree/master/src "src") |  |  |\n| [.dockerignore](/ItzCrazyKns/Perplexica/blob/master/.dockerignore ".dockerignore") | | [.dockerignore](/ItzCrazyKns/Perplexica/blob/master/.dockerignore ".dockerignore") |  |  |\n| [.eslintrc.json](/ItzCrazyKns/Perplexica/blob/master/.eslintrc.json ".eslintrc.json") | | [.eslintrc.json](/ItzCrazyKns/Perplexica/blob/master/.eslintrc.json ".eslintrc.json") |  |  |\n| [.gitignore](/ItzCrazyKns/Perplexica/blob/master/.gitignore ".gitignore") | | [.gitignore](/ItzCrazyKns/Perplexica/blob/master/.gitignore ".gitignore") |  |  |\n| [.prettierignore](/ItzCrazyKns/Perplexica/blob/master/.prettierignore ".prettierignore") | | [.prettierignore](/ItzCrazyKns/Perplexica/blob/master/.prettierignore ".prettierignore") |  |  |\n| [.prettierrc.js](/ItzCrazyKns/Perplexica/blob/master/.prettierrc.js ".prettierrc.js") | | [.prettierrc.js](/ItzCrazyKns/Perplexica/blob/master/.prettierrc.js ".prettierrc.js") |  |  |\n| [CONTRIBUTING.md](/ItzCrazyKns/Perplexica/blob/master/CONTRIBUTING.md "CONTRIBUTING.md") | | [CONTRIBUTING.md](/ItzCrazyKns/Perplexica/blob/master/CONTRIBUTING.md "CONTRIBUTING.md") |  |  |\n| [Dockerfile](/ItzCrazyKns/Perplexica/blob/master/Dockerfile "Dockerfile") | | [Dockerfile](/ItzCrazyKns/Perplexica/blob/master/Dockerfile "Dockerfile") |  |  |\n| [Dockerfile.slim](/ItzCrazyKns/Perplexica/blob/master/Dockerfile.slim "Dockerfile.slim") | | [Dockerfile.slim](/ItzCrazyKns/Perplexica/blob/master/Dockerfile.slim "Dockerfile.slim") |  |  |\n| [LICENSE](/ItzCrazyKns/Perplexica/blob/master/LICENSE "LICENSE") | | [LICENSE](/ItzCrazyKns/Perplexica/blob/master/LICENSE "LICENSE") |  |  |\n| [README.md](/ItzCrazyKns/Perplexica/blob/master/README.md "README.md") | | [README.md](/ItzCrazyKns/Perplexica/blob/master/README.md "README.md") |  |  |\n| [docker-compose.yaml](/ItzCrazyKns/Perplexica/blob/master/docker-compose.yaml "docker-compose.yaml") | | [docker-compose.yaml](/ItzCrazyKns/Perplexica/blob/master/docker-compose.yaml "docker-compose.yaml") |  |  |\n| [drizzle.config.ts](/ItzCrazyKns/Perplexica/blob/master/drizzle.config.ts "drizzle.config.ts") | | [drizzle.config.ts](/ItzCrazyKns/Perplexica/blob/master/drizzle.config.ts "drizzle.config.ts") |  |  |\n| [entrypoint.sh](/ItzCrazyKns/Perplexica/blob/master/entrypoint.sh "entrypoint.sh") | | [entrypoint.sh](/ItzCrazyKns/Perplexica/blob/master/entrypoint.sh "entrypoint.sh") |  |  |\n| [next-env.d.ts](/ItzCrazyKns/Perplexica/blob/master/next-env.d.ts "next-env.d.ts") | | [next-env.d.ts](/ItzCrazyKns/Perplexica/blob/master/next-env.d.ts "next-env.d.ts") |  |  |\n| [next.config.mjs](/ItzCrazyKns/Perplexica/blob/master/next.config.mjs "next.config.mjs") | | [next.config.mjs](/ItzCrazyKns/Perplexica/blob/master/next.config.mjs "next.config.mjs") |  |  |\n| [package.json](/ItzCrazyKns/Perplexica/blob/master/package.json "package.json") | | [package.json](/ItzCrazyKns/Perplexica/blob/master/package.json "package.json") |  |  |\n| [postcss.config.js](/ItzCrazyKns/Perplexica/blob/master/postcss.config.js "postcss.config.js") | | [postcss.config.js](/ItzCrazyKns/Perplexica/blob/master/postcss.config.js "postcss.config.js") |  |  |\n| [tailwind.config.ts](/ItzCrazyKns/Perplexica/blob/master/tailwind.config.ts "tailwind.config.ts") | | [tailwind.config.ts](/ItzCrazyKns/Perplexica/blob/master/tailwind.config.ts "tailwind.config.ts") |  |  |\n| [tsconfig.json](/ItzCrazyKns/Perplexica/blob/master/tsconfig.json "tsconfig.json") | | [tsconfig.json](/ItzCrazyKns/Perplexica/blob/master/tsconfig.json "tsconfig.json") |  |  |\n| [yarn.lock](/ItzCrazyKns/Perplexica/blob/master/yarn.lock "yarn.lock") | | [yarn.lock](/ItzCrazyKns/Perplexica/blob/master/yarn.lock "yarn.lock") |  |  |\n| View all files | | |\n\n## Repository files navigation\n\n* [README](#)\n* [Contributing](#)\n* [MIT license](#)\n\n# Perplexica 🔍\n\n[![GitHub Repo stars](https://camo.githubusercontent.com/f48d5016d2a00ea94a704dad840435f1f4a978574d0bd3af73639233c15b0147/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f49747a4372617a794b6e732f506572706c65786963613f7374796c653d736f6369616c)](https://github.com/ItzCrazyKns/Perplexica/stargazers)\n[![GitHub forks](https://camo.githubusercontent.com/cca90e59cc6293888ad27ad817568c546f5a38a5f9c55a10bddf7eba9f99476b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f49747a4372617a794b6e732f506572706c65786963613f7374796c653d736f6369616c)](https://github.com/ItzCrazyKns/Perplexica/network/members)\n[![GitHub watchers](https://camo.githubusercontent.com/2ad6ccebf00678ffbd6c37ead0dead812c3f473b6d2e5c47f016261bc7a868e5/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f77617463686572732f49747a4372617a794b6e732f506572706c65786963613f7374796c653d736f6369616c)](https://github.com/ItzCrazyKns/Perplexica/watchers)\n[![Docker Pulls](https://camo.githubusercontent.com/07c6a4ad302d5559364fbe8330767099a986e78ae5336aa82dec4bcdab566608/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f69747a6372617a796b6e73313333372f706572706c65786963613f636f6c6f723d626c7565)](https://hub.docker.com/r/itzcrazykns1337/perplexica)\n[![License: MIT](https://camo.githubusercontent.com/fdf2982b9f5d7489dcf44570e714e3a15fce6253e0cc6b5aa61a075aac2ff71b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f772e737667)](https://github.com/ItzCrazyKns/Perplexica/blob/master/LICENSE)\n[![GitHub last commit](https://camo.githubusercontent.com/657a5463a624e88643f83b9f3491414246fbd7f795904b949a2d7113c801531b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f49747a4372617a794b6e732f506572706c65786963613f636f6c6f723d677265656e)](https://github.com/ItzCrazyKns/Perplexica/commits/master)\n[![Discord](https://camo.githubusercontent.com/9dfdf1360f53662d1e12eea52f833f4245041da52876070644e31926d6150553/68747470733a2f2f646362616467652e6c696d65732e70696e6b2f6170692f7365727665722f32366141724d793874543f7374796c653d666c6174)](https://discord.gg/26aArMy8tT)\n\nPerplexica is a **privacy-focused AI answering engine** that runs entirely on your own hardware. It combines knowledge from the vast internet with support for **local LLMs** (Ollama) and cloud providers (OpenAI, Claude, Groq), delivering accurate answers with **cited sources** while keeping your searches completely private.\n\n[![preview](/ItzCrazyKns/Perplexica/raw/master/.assets/perplexica-screenshot.png)](/ItzCrazyKns/Perplexica/blob/master/.assets/perplexica-screenshot.png)\n\nWant to know more about its architecture and how it works? You can read it [here](https://github.com/ItzCrazyKns/Perplexica/tree/master/docs/architecture/README.md).\n\n## ✨ Features\n\n🤖 **Support for all major AI providers** - Use local LLMs through Ollama or connect to OpenAI, Anthropic Claude, Google Gemini, Groq, and more. Mix and match models based on your needs.\n\n⚡ **Smart search modes** - Choose Speed Mode when you need quick answers, Balanced Mode for everyday searches, or Quality Mode for deep research.\n\n🧭 **Pick your sources** - Search the web, discussions, or academic papers. More sources and integrations are in progress.\n\n🧩 **Widgets** - Helpful UI cards that show up when relevant, like weather, calculations, stock prices, and other quick lookups.\n\n🔍 **Web search powered by SearxNG** - Access multiple search engines while keeping your identity private. Support for Tavily and Exa coming soon for even better results.\n\n📷 **Image and video search** - Find visual content alongside text results. Search isn\'t limited to just articles anymore.\n\n📄 **File uploads** - Upload documents and ask questions about them. PDFs, text files, images - Perplexica understands them all.\n\n🌐 **Search specific domains** - Limit your search to specific websites when you know where to look. Perfect for technical documentation or research papers.\n\n💡 **Smart suggestions** - Get intelligent search suggestions as you type, helping you formulate better queries.\n\n📚 **Discover** - Browse interesting articles and trending content throughout the day. Stay informed without even searching.\n\n🕒 **Search history** - Every search is saved locally so you can revisit your discoveries anytime. Your research is never lost.\n\n✨ **More coming soon** - We\'re actively developing new features based on community feedback. Join our Discord to help shape Perplexica\'s future!\n\n## Sponsors\n\nPerplexica\'s development is powered by the generous support of our sponsors. Their contributions help keep this project free, open-source, and accessible to everyone.\n\n[![Warp Terminal](/ItzCrazyKns/Perplexica/raw/master/.assets/sponsers/warp.png)](https://www.warp.dev/perplexica)\n\n### **✨ [Try Warp - The AI-Powered Terminal →](https://www.warp.dev/perplexica)**\n\nWarp is revolutionizing development workflows with AI-powered features, modern UX, and blazing-fast performance. Used by developers at top companies worldwide.\n\n---\n\nWe\'d also like to thank the following partners for their generous support:\n\n|  |  |\n| --- | --- |\n| [Exa](https://dashboard.exa.ai) | [Exa](https://dashboard.exa.ai) • The Perfect Web Search API for LLMs - web search, crawling, deep research, and answer APIs |\n\n## Installation\n\nThere are mainly 2 ways of installing Perplexica - With Docker, Without Docker. Using Docker is highly recommended.\n\n### Getting Started with Docker (Recommended)\n\nPerplexica can be easily run using Docker. Simply run the following command:\n\n```\ndocker run -d -p 3000:3000 -v perplexica-data:/home/perplexica/data --name perplexica itzcrazykns1337/perplexica:latest\n```\n\nThis will pull and start the Perplexica container with the bundled SearxNG search engine. Once running, open your browser and navigate to <http://localhost:3000>. You can then configure your settings (API keys, models, etc.) directly in the setup screen.\n\n**Note**: The image includes both Perplexica and SearxNG, so no additional setup is required. The `-v` flags create persistent volumes for your data and uploaded files.\n\n#### Using Perplexica with Your Own SearxNG Instance\n\nIf you already have SearxNG running, you can use the slim version of Perplexica:\n\n```\ndocker run -d -p 3000:3000 -e SEARXNG_API_URL=http://your-searxng-url:8080 -v perplexica-data:/home/perplexica/data --name perplexica itzcrazykns1337/perplexica:slim-latest\n```\n\n**Important**: Make sure your SearxNG instance has:\n\n* JSON format enabled in the settings\n* Wolfram Alpha search engine enabled\n\nReplace `http://your-searxng-url:8080` with your actual SearxNG URL. Then configure your AI provider settings in the setup screen at <http://localhost:3000>.\n\n#### Advanced Setup (Building from Source)\n\nIf you prefer to build from source or need more control:\n\n1. Ensure Docker is installed and running on your system.\n2. Clone the Perplexica repository:\n\n   ```\n   git clone https://github.com/ItzCrazyKns/Perplexica.git\n   ```\n3. After cloning, navigate to the directory containing the project files.\n4. Build and run using Docker:\n\n   ```\n   docker build -t perplexica .\n   docker run -d -p 3000:3000 -v perplexica-data:/home/perplexica/data --name perplexica perplexica\n   ```\n5. Access Perplexica at <http://localhost:3000> and configure your settings in the setup screen.\n\n**Note**: After the containers are built, you can start Perplexica directly from Docker without having to open a terminal.\n\n### Non-Docker Installation\n\n1. Install SearXNG and allow `JSON` format in the SearXNG settings. Make sure Wolfram Alpha search engine is also enabled.\n2. Clone the repository:\n\n   ```\n   git clone https://github.com/ItzCrazyKns/Perplexica.git\n   cd Perplexica\n   ```\n3. Install dependencies:\n\n   ```\n   npm i\n   ```\n4. Build the application:\n\n   ```\n   npm run build\n   ```\n5. Start the application:\n\n   ```\n   npm run start\n   ```\n6. Open your browser and navigate to <http://localhost:3000> to complete the setup and configure your settings (API keys, models, SearxNG URL, etc.) in the setup screen.\n\n**Note**: Using Docker is recommended as it simplifies the setup process, especially for managing environment variables and dependencies.\n\nSee the [installation documentation](https://github.com/ItzCrazyKns/Perplexica/tree/master/docs/installation) for more information like updating, etc.\n\n### Troubleshooting\n\n#### Local OpenAI-API-Compliant Servers\n\nIf Perplexica tells you that you haven\'t configured any chat model providers, ensure that:\n\n1. Your server is running on `0.0.0.0` (not `127.0.0.1`) and on the same port you put in the API URL.\n2. You have specified the correct model name loaded by your local LLM server.\n3. You have specified the correct API key, or if one is not defined, you have put *something* in the API key field and not left it empty.\n\n#### Ollama Connection Errors\n\nIf you\'re encountering an Ollama connection error, it is likely due to the backend being unable to connect to Ollama\'s API. To fix this issue you can:\n\n1. **Check your Ollama API URL:** Ensure that the API URL is correctly set in the settings menu.\n2. **Update API URL Based on OS:**\n\n   * **Windows:** Use `http://host.docker.internal:11434`\n   * **Mac:** Use `http://host.docker.internal:11434`\n   * **Linux:** Use `http://<private_ip_of_host>:11434`\n\n   Adjust the port number if you\'re using a different one.\n3. **Linux Users - Expose Ollama to Network:**\n\n   * Inside `/etc/systemd/system/ollama.service`, you need to add `Environment="OLLAMA_HOST=0.0.0.0:11434"`. (Change the port number if you are using a different one.) Then reload the systemd manager configuration with `systemctl daemon-reload`, and restart Ollama by `systemctl restart ollama`. For more information see [Ollama docs](https://github.com/ollama/ollama/blob/main/docs/faq.md#setting-environment-variables-on-linux)\n   * Ensure that the port (default is 11434) is not blocked by your firewall.\n\n#### Lemonade Connection Errors\n\nIf you\'re encountering a Lemonade connection error, it is likely due to the backend being unable to connect to Lemonade\'s API. To fix this issue you can:\n\n1. **Check your Lemonade API URL:** Ensure that the API URL is correctly set in the settings menu.\n2. **Update API URL Based on OS:**\n\n   * **Windows:** Use `http://host.docker.internal:8000`\n   * **Mac:** Use `http://host.docker.internal:8000`\n   * **Linux:** Use `http://<private_ip_of_host>:8000`\n\n   Adjust the port number if you\'re using a different one.\n3. **Ensure Lemonade Server is Running:**\n\n   * Make sure your Lemonade server is running and accessible on the configured port (default is 8000).\n   * Verify that Lemonade is configured to accept connections from all interfaces (`0.0.0.0`), not just localhost (`127.0.0.1`).\n   * Ensure that the port (default is 8000) is not blocked by your firewall.\n\n## Using as a Search Engine\n\nIf you wish to use Perplexica as an alternative to traditional search engines like Google or Bing, or if you want to add a shortcut for quick access from your browser\'s search bar, follow these steps:\n\n1. Open your browser\'s settings.\n2. Navigate to the \'Search Engines\' section.\n3. Add a new site search with the following URL: `http://localhost:3000/?q=%s`. Replace `localhost` with your IP address or domain name, and `3000` with the port number if Perplexica is not hosted locally.\n4. Click the add button. Now, you can use Perplexica directly from your browser\'s search bar.\n\n## Using Perplexica\'s API\n\nPerplexica also provides an API for developers looking to integrate its powerful search engine into their own applications. You can run searches, use multiple models and get answers to your queries.\n\nFor more details, check out the full documentation [here](https://github.com/ItzCrazyKns/Perplexica/tree/master/docs/API/SEARCH.md).\n\n## Expose Perplexica to network\n\nPerplexica runs on Next.js and handles all API requests. It works right away on the same network and stays accessible even with port forwarding.\n\n## One-Click Deployment\n\n[![Deploy to Sealos](https://raw.githubusercontent.com/labring-actions/templates/main/Deploy-on-Sealos.svg)](https://usw.sealos.io/?openapp=system-template%3FtemplateName%3Dperplexica)\n[![Deploy to RepoCloud](https://camo.githubusercontent.com/bb59e7a3c986f97daed8cee9518a0e5edf7567e1b7823158ea3f946ef15768db/68747470733a2f2f64313674307063343834367835322e636c6f756466726f6e742e6e65742f6465706c6f796c6f62652e737667)](https://repocloud.io/details/?app_id=267)\n[![Run on ClawCloud](https://raw.githubusercontent.com/ClawCloud/Run-Template/refs/heads/main/Run-on-ClawCloud.svg)](https://template.run.claw.cloud/?referralCode=U11MRQ8U9RM4&openapp=system-fastdeploy%3FtemplateName%3Dperplexica)\n[![Deploy on Hostinger](https://camo.githubusercontent.com/d9d518de2066eec8a06a45596bf993602aa76a9a9c7cb9b81278d5bc3dc1c54a/68747470733a2f2f6173736574732e686f7374696e6765722e636f6d2f7670732f6465706c6f792e737667)](https://www.hostinger.com/vps/docker-hosting?compose_url=https://raw.githubusercontent.com/ItzCrazyKns/Perplexica/refs/heads/master/docker-compose.yaml)\n\n## Upcoming Features\n\n* Adding more widgets, integrations, search sources\n* Adding ability to create custom agents (name T.B.D.)\n* Adding authentication\n\n## Support Us\n\nIf you find Perplexica useful, consider giving us a star on GitHub. This helps more people discover Perplexica and supports the development of new features. Your support is greatly appreciated.\n\n### Donations\n\nWe also accept donations to help sustain our project. If you would like to contribute, you can use the following options to donate. Thank you for your support!\n\n| Ethereum |\n| --- |\n| Address: `0xB025a84b2F269570Eb8D4b05DEdaA41D8525B6DD` |\n\n## Contribution\n\nPerplexica is built on the idea that AI and large language models should be easy for everyone to use. If you find bugs or have ideas, please share them in via GitHub Issues. For more information on contributing to Perplexica you can read the [CONTRIBUTING.md](/ItzCrazyKns/Perplexica/blob/master/CONTRIBUTING.md) file to learn more about Perplexica and how you can contribute to it.\n\n## Help and Support\n\nIf you have any questions or feedback, please feel free to reach out to us. You can create an issue on GitHub or join our Discord server. There, you can connect with other users, share your experiences and reviews, and receive more personalized help. [Click here](https://discord.gg/EFwsmQDgAu) to join the Discord server. To discuss matters outside of regular support, feel free to contact me on Discord at `itzcrazykns`.\n\nThank you for exploring Perplexica, the AI-powered search engine designed to enhance your search experience. We are constantly working to improve Perplexica and expand its capabilities. We value your feedback and contributions which help us make Perplexica even better. Don\'t forget to check back for updates and new features!\n\n## About\n\nPerplexica is an AI-powered answering engine.\n\n### Topics\n\n[search-engine](/topics/search-engine "Topic: search-engine")\n[machine-learning](/topics/machine-learning "Topic: machine-learning")\n[artificial-intelligence](/topics/artificial-intelligence "Topic: artificial-intelligence")\n[ai-agents](/topics/ai-agents "Topic: ai-agents")\n[rag](/topics/rag "Topic: rag")\n[answering-engine](/topics/answering-engine "Topic: answering-engine")\n[searxng](/topics/searxng "Topic: searxng")\n[llm](/topics/llm "Topic: llm")\n[ai-search-engine](/topics/ai-search-engine "Topic: ai-search-engine")\n[open-source-ai-search-engine](/topics/open-source-ai-search-engine "Topic: open-source-ai-search-engine")\n[perplexica](/topics/perplexica "Topic: perplexica")\n[searxng-copilot](/topics/searxng-copilot "Topic: searxng-copilot")\n[self-hosted-ai](/topics/self-hosted-ai "Topic: self-hosted-ai")\n\n### Resources\n\n[Readme](#readme-ov-file)\n\n### License\n\n[MIT license](#MIT-1-ov-file)\n\n### Contributing\n\n[Contributing](#contributing-ov-file)\n\n### Uh oh!\n\nThere was an error while loading. Please reload this page.\n\n[Activity](/ItzCrazyKns/Perplexica/activity)\n\n### Stars\n\n[**32.1k**\nstars](/ItzCrazyKns/Perplexica/stargazers)\n\n### Watchers\n\n[**182**\nwatching](/ItzCrazyKns/Perplexica/watchers)\n\n### Forks\n\n[**3.4k**\nforks](/ItzCrazyKns/Perplexica/forks)\n\n[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FItzCrazyKns%2FPerplexica&report=ItzCrazyKns+%28user%29)\n\n## [Releases 33](/ItzCrazyKns/Perplexica/releases)\n\n[v1.12.1\n\nLatest\n\nDec 31, 2025](/ItzCrazyKns/Perplexica/releases/tag/v1.12.1)\n\n[+ 32 releases](/ItzCrazyKns/Perplexica/releases)\n\n### Uh oh!\n\nThere was an error while loading. Please reload this page.\n\n## [Contributors 44](/ItzCrazyKns/Perplexica/graphs/contributors)\n\n* [![@ItzCrazyKns](https://avatars.githubusercontent.com/u/95534749?s=64&v=4)](https://github.com/ItzCrazyKns)\n* [![@WanQuanXie](https://avatars.githubusercontent.com/u/8021137?s=64&v=4)](https://github.com/WanQuanXie)\n* [![@OmarElKadri](https://avatars.githubusercontent.com/u/118303871?s=64&v=4)](https://github.com/OmarElKadri)\n* [![@sjiampojamarn](https://avatars.githubusercontent.com/u/18257803?s=64&v=4)](https://github.com/sjiampojamarn)\n* [![@cubic-dev-ai[bot]](https://avatars.githubusercontent.com/in/1082092?s=64&v=4)](https://github.com/apps/cubic-dev-ai)\n* [![@skoved](https://avatars.githubusercontent.com/u/17677175?s=64&v=4)](https://github.com/skoved)\n* [![@tuxthepenguin84](https://avatars.githubusercontent.com/u/12042822?s=64&v=4)](https://github.com/tuxthepenguin84)\n* [![@ramkrishna2910](https://avatars.githubusercontent.com/u/12814146?s=64&v=4)](https://github.com/ramkrishna2910)\n* [![@aiyogg](https://avatars.githubusercontent.com/u/15699954?s=64&v=4)](https://github.com/aiyogg)\n* [![@ericdachen](https://avatars.githubusercontent.com/u/54382303?s=64&v=4)](https://github.com/ericdachen)\n* [![@haddadrm](https://avatars.githubusercontent.com/u/121486289?s=64&v=4)](https://github.com/haddadrm)\n* [![@PSYEONE](https://avatars.githubusercontent.com/u/154057250?s=64&v=4)](https://github.com/PSYEONE)\n* [![@QuietlyChan](https://avatars.githubusercontent.com/u/8343216?s=64&v=4)](https://github.com/QuietlyChan)\n* [![@wellCh4n](https://avatars.githubusercontent.com/u/13273026?s=64&v=4)](https://github.com/wellCh4n)\n\n[+ 30 contributors](/ItzCrazyKns/Perplexica/graphs/contributors)\n\n## Languages\n\n* [TypeScript\n  98.7%](/ItzCrazyKns/Perplexica/search?l=typescript)\n* Other\n  1.3%\n\n## Footer\n\n© 2026 GitHub,\xa0Inc.\n\n### Footer navigation\n\n* [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)\n* [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)\n* [Security](https://github.com/security)\n* [Status](https://www.githubstatus.com/)\n* [Community](https://github.community/)\n* [Docs](https://docs.github.com/)\n* [Contact](https://support.github.com?tags=dotcom-footer)\n* Manage cookies\n* Do not share my personal information\n\n\n\nYou can’t perform that action at this time.', 'is_citable': True, 'prompt_context_metadata': {'content_type': 'html', 'mime_type': 'text/html; charset=utf-8', 'destination_url': 'https://github.com/ItzCrazyKns/Perplexica'}}
Here's a complete guide to installing and running **Perplexica** locally on Linux for free:

---

## 🔍 What is Perplexica?

Perplexica is a privacy-focused AI answering engine that runs entirely on your own hardware. It combines internet search with support for local LLMs (via Ollama) and cloud providers, delivering answers with cited sources while keeping your searches private.

---

## ✅ Prerequisites

Before starting, make sure you have:
- **Docker** installed (recommended method)
- **Git** installed
- **Ollama** (if you want 100% free, local AI — no API keys needed)

---

## 🐳 Method 1: Docker (Easiest — Recommended)

### Step 1: Pull & Run with one command

```bash
docker run -d -p 3000:3000 \
  -v perplexica-data:/home/perplexica/data \
  --name perplexica \
  itzcrazykns1337/perplexica:latest
```

This pulls and starts Perplexica with the bundled SearxNG search engine. No additional setup is required.

### Step 2: Open in browser

Go to **http://localhost:3000** and complete the setup screen.

---

## 🛠️ Method 2: Build from Source (Docker)

```bash
# 1. Clone the repo
git clone https://github.com/ItzCrazyKns/Perplexica.git
cd Perplexica

# 2. Build the image
docker build -t perplexica .

# 3. Run it
docker run -d -p 3000:3000 \
  -v perplexica-data:/home/perplexica/data \
  --name perplexica perplexica
```

Then open **http://localhost:3000**.

---

## 💻 Method 3: Without Docker (Manual Install)

```bash
# 1. Install SearXNG (required for web search)
# Enable JSON format and Wolfram Alpha engine in SearXNG settings

# 2. Clone the repo
git clone https://github.com/ItzCrazyKns/Perplexica.git
cd Perplexica

# 3. Install dependencies
npm i

# 4. Build
npm run build

# 5. Start
npm run start
```

Then open **http://localhost:3000**.

---

## 🤖 Running 100% Free with Ollama (No API Keys)

To use Perplexica completely free with a local LLM:

**Step 1 — Install Ollama:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Step 2 — Pull a free model:**
```bash
ollama pull llama3       # or mistral, phi3, gemma, etc.
```

**Step 3 — Expose Ollama to Docker network (Linux-specific):**

On Linux, inside `/etc/systemd/system/ollama.service`, add `Environment="OLLAMA_HOST=0.0.0.0:11434"`, then reload and restart with `systemctl daemon-reload` and `systemctl restart ollama`.

**Step 4 — In Perplexica settings at http://localhost:3000:**
- Set Ollama API URL to: `http://<your-private-ip>:11434`
- Select your downloaded model (e.g., `llama3`)

On Linux, use `http://<private_ip_of_host>:11434` as the Ollama URL (not `localhost` or `127.0.0.1`, as Docker can't reach those from inside a container).

---

## 🔍 Use as a Browser Search Engine (Optional)

Add a new site search in your browser with the URL `http://localhost:3000/?q=%s` to use Perplexica directly from your browser's search bar.

---

## 🧩 Quick Troubleshooting

| Problem | Fix |
|---|---|
| Ollama not connecting | Use `http://<private_ip>:11434`, not `localhost` |
| No models showing | Make sure Ollama is running: `systemctl status ollama` |
| Port 3000 in use | Change to `-p 3001:3000` and visit `:3001` |
| SearXNG issues | Ensure JSON format is enabled in SearXNG settings |

---

**Docker is the easiest path** — one command and you're up. Pair it with Ollama for a fully free, private, local AI search engine!

---

### 🧑 You

with docker step by step

---

### 🤖 Claude

Here's the complete step-by-step Docker installation guide for Perplexica on Linux:

---

## Step 1: Install Docker

```bash
# Update your system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com | sh

# Add your user to the docker group (so you don't need sudo every time)
sudo usermod -aG docker $USER

# Apply group change (or log out and back in)
newgrp docker

# Verify Docker is working
docker --version
```

---

## Step 2: Install Ollama (for free local AI)

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Then pull a free model (pick one based on your RAM):

| RAM | Recommended Model |
|---|---|
| 4GB | `ollama pull phi3` |
| 8GB | `ollama pull llama3` |
| 16GB+ | `ollama pull llama3:70b` |

```bash
# Example — pull llama3 (good balance of speed & quality)
ollama pull llama3
```

---

## Step 3: Expose Ollama to Docker (Linux-specific — critical!)

```bash
# Open the Ollama service file
sudo nano /etc/systemd/system/ollama.service
```

Find the `[Service]` section and add this line:
```
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

It should look like this:
```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
ExecStart=/usr/local/bin/ollama serve
...
```

Save (`Ctrl+O`, `Enter`, `Ctrl+X`), then reload and restart:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama

# Verify Ollama is running and listening
curl http://localhost:11434
# Should return: "Ollama is running"
```

---

## Step 4: Get your private IP address

```bash
hostname -I | awk '{print $1}'
```

Note this IP — you'll need it in Step 6 (e.g. `192.168.1.105`).

---

## Step 5: Run Perplexica with Docker

```bash
docker run -d \
  -p 3000:3000 \
  -v perplexica-data:/home/perplexica/data \
  --name perplexica \
  itzcrazykns1337/perplexica:latest
```

Check it started correctly:
```bash
docker ps
# You should see perplexica listed as "Up"
```

If you need to check logs:
```bash
docker logs perplexica
```

---

## Step 6: Configure Perplexica in the browser

1. Open your browser and go to **http://localhost:3000**
2. You'll see a setup screen — fill it in:
   - **Chat Model Provider** → select `Ollama`
   - **Ollama API URL** → `http://YOUR_PRIVATE_IP:11434` (from Step 4, e.g. `http://192.168.1.105:11434`)
   - **Chat Model** → select `llama3` (or whichever you pulled)
   - **Embedding Model Provider** → `Ollama`
   - **Embedding Model** → select any available model
3. Click **Save** — you're done! 🎉

---

## Step 7: Test it

Type any question in the search bar and hit Enter. Perplexica will search the web via SearxNG and answer using your local Ollama model — **100% free, no API keys needed**.

---

## Useful Docker management commands

```bash
# Stop Perplexica
docker stop perplexica

# Start it again
docker start perplexica

# Restart it
docker restart perplexica

# Remove and reinstall (keeps your data volume)
docker rm -f perplexica
docker run -d -p 3000:3000 -v perplexica-data:/home/perplexica/data --name perplexica itzcrazykns1337/perplexica:latest

# Update to latest version
docker pull itzcrazykns1337/perplexica:latest
docker rm -f perplexica
docker run -d -p 3000:3000 -v perplexica-data:/home/perplexica/data --name perplexica itzcrazykns1337/perplexica:latest
```

---

That's the full setup! The key Linux gotcha is **Step 3** — Ollama must be bound to `0.0.0.0` (not just `localhost`) so Docker can reach it from inside the container.

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12  ❯ ollama pull phi3 pulling manifest  pulling 633fc5be925f: 100% ▕████████████████████████████████████████████████████████████████████████▏ 2.2 GB                          pulling fa8235e5b48f: 100% ▕████████████████████████████████████████████████████████████████████████▏ 1.1 KB                          pulling 542b217f179c: 100% ▕████████████████████████████████████████████████████████████████████████▏  148 B                          pulling 8dde1baf1db0: 100% ▕████████████████████████████████████████████████████████████████████████▏   78 B                          pulling 23291dc44752: 100% ▕████████████████████████████████████████████████████████████████████████▏  483 B                          verifying sha256 digest  writing manifest  success  ~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12 took 3s  ❯ # Open the Ollama service file sudo nano /etc/systemd/system/ollama.service ``` Find the `[Service]` section and add this line: ``` Environment="OLLAMA_HOST=0.0.0.0:11434" [sudo] password for sunny77:  Command 'Find' not found, did you mean:  command 'find' from deb findutils (4.8.0-1ubuntu3) Try: sudo apt install <deb name> section: command not found [Service]: command not found ~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12  ❯

---

### 🤖 Claude

It looks like you accidentally pasted the instruction text into your terminal instead of just the `sudo nano` command. No worries! Let's fix it step by step.

---

## Fix the Ollama service file

**Step 1: Open the file correctly** — just run this single command:

```bash
sudo nano /etc/systemd/system/ollama.service
```

**Step 2:** Once the file opens in nano, look for the `[Service]` section. It will look something like this:

```ini
[Unit]
Description=Ollama Service
...

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
...
```

**Step 3:** Add this line right under `[Service]`:

```
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

So it becomes:

```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
ExecStart=/usr/local/bin/ollama serve
```

**Step 4:** Save and exit nano:
- Press `Ctrl + O` → then `Enter` (to save)
- Press `Ctrl + X` (to exit)

---

## Reload and restart Ollama

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

## Verify it's working

```bash
curl http://localhost:11434
```

Should print: `Ollama is running`

---

Then continue with **Step 4** from the guide — get your private IP:

```bash
hostname -I | awk '{print $1}'
```

Let me know what you see after opening the nano editor and I'll help you place the line correctly!

---


---

## 🔗 Related Notes

- [[2025-08-08_ai-skin-lesion-diagnosis-website-design|Ai-Skin-Lesion-Diagnosis-Website-Design]]
- [[2026-02-11_epstein-files-chatbot-prompt|Epstein-Files-Chatbot-Prompt]]
- [[2025-11-06_rust-toolchain-installation-failure-during-pip-install|Rust-Toolchain-Installation-Failure-During-Pip-Install]]
- [[2026-02-26_claude-code-login-method-selection|Claude-Code-Login-Method-Selection]]
- [[2025-07-21_automated-daily-phone-call-reminder-script|Automated-Daily-Phone-Call-Reminder-Script]]
