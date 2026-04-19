---
title: "Correcting AionUi Docker filenames for v1.8.26"
date: 2026-03-13
tags:
  - python
  - sql
  - machine-learning
  - llm-ai
  - linux
  - obsidian
  - job-search
  - buddhism
  - history
  - geopolitics
  - stock-market
  - research
  - creative
  - web-dev
  - game-design
source: claude-export
---

# Correcting AionUi Docker filenames for v1.8.26

> **Conversation Overview**

The person was working on deploying AionUi (from the GitHub repository iOfficeAI/AionUi) in a Docker container on what appears to be a Linux system. The conversation focused on troubleshooting the Docker setup, specifically around correct release filenames for v1.8.26, and then shifted to resolving a login authentication issue with the running container.

The person successfully built and ran the AionUi Docker container using an AppImage approach with Xvfb for virtual display, exposing port 25808. The container stores its data in a Docker volume mounted at `/root/.config/AionUi`. When attempting to sign in, they encountered a 401 authentication error. Through iterative debugging, the team identified that the SQLite database is located at `/root/.config/AionUi/aionui/aionui.db`, contains a `users` table with a `password_hash` column using bcrypt (`$2a$12$` format), and has a single user with `id: system_default_user`, `username: admin`, and no email set.

The solution involved installing `python3-pip` inside the container, then using the `bcrypt` Python library to generate a new hash and update the database directly via SQLite to reset the admin password to `admin123`. The final command to accomplish this was: `docker exec aionui sh -c "apt-get install -q -y python3-pip 2>/dev/null && pip install bcrypt -q --break-system-packages && python3 -c ..."` with an inline Python script performing the bcrypt hash generation and SQLite update.

**Date:** 2026-03-13  
**Topics:** [[Python]] · [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Linux]] · [[Obsidian]] · [[Job-Search]] · [[Buddhism]] · [[History]] · [[Geopolitics]] · [[Stock-Market]] · [[Research]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

I see the issue - **version 1.8.26 also doesn't exist**! The search results were misleading. Let me check the actual latest version from the GitHub releases page directly.    
   I can see the actual latest version is **v1.8.27** (not 1.8.26). Let me check what files are actually available in the latest release.    
   I can see from the search results that **v1.8.26** actually exists with files named:
- `AionUi-1.8.26-linux-amd64.deb`
- `AionUi-1.8.26-linux-x86_64.AppImage`
The naming convention is different from what we tried! Let me create the correct Dockerfile:
## Fixed Dockerfile with Correct Filenames
```bash
cd ~/aionui-docker
# Stop and remove old container
docker stop aionui 2>/dev/null && docker rm aionui 2>/dev/null
# Create updated Dockerfile with CORRECT filenames
cat > Dockerfile << 'EOF'
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:99
ENV PORT=25808
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    libgtk-3-0 \
    libnotify4 \
    libnss3 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    libatspi2.0-0 \
    libuuid1 \
    libsecret-1-0 \
    libgbm1 \
    libasound2 \
    xvfb \
    libfuse2 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
# Download AppImage with CORRECT filename (v1.8.26)
RUN wget https://github.com/iOfficeAI/AionUi/releases/download/v1.8.26/AionUi-1.8.26-linux-x86_64.AppImage  -O AionUi.AppImage && \
    chmod +x AionUi.AppImage
# Create startup script
RUN echo '#!/bin/bash\n\
Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &\n\
sleep 3\n\
cd /app\n\
./AionUi.AppImage --appimage-extract-and-run --webui --remote --no-sandbox --port=${PORT}\n' > /start.sh && chmod +x /start.sh
EXPOSE 25808
CMD ["/start.sh"]
EOF
# Clean up old images
docker rmi aionui:latest 2>/dev/null || true
# Build
docker build --no-cache -t aionui:latest .
# Run
docker run -d \
  --name aionui \
  -p 25808:25808 \
  -v aionui-data:/root/.config/AionUi \
  -e PORT=25808 \
  --restart unless-stopped \
  aionui:latest
# Watch logs
docker logs -f aionui
```
## Alternative: Use .deb Package (v1.8.26)
If you prefer the .deb package:
```bash
cat > Dockerfile << 'EOF'
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:99
ENV PORT=25808
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    libgtk-3-0 \
    libnotify4 \
    libnss3 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    libatspi2.0-0 \
    libuuid1 \
    libsecret-1-0 \
    libappindicator3-1 \
    fonts-liberation \
    libgbm1 \
    libasound2 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
# Download and install .deb with CORRECT filename (v1.8.26)
RUN wget https://github.com/iOfficeAI/AionUi/releases/download/v1.8.26/AionUi-1.8.26-linux-amd64.deb  -O aionui.deb && \
    dpkg -i aionui.deb || apt-get install -f -y && \
    rm aionui.deb
# Create startup script
RUN echo '#!/bin/bash\n\
Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &\n\
sleep 2\n\
# Find binary\n\
if [ -f /opt/AionUi/aionui ]; then\n\
  /opt/AionUi/aionui --webui --remote --no-sandbox --port=${PORT}\n\
elif [ -f /usr/bin/aionui ]; then\n\
  /usr/bin/aionui --webui --remote --no-sandbox --port=${PORT}\n\
else\n\
  find /usr /opt -name "aionui" -type f -executable | head -1 | xargs -I {} {} --webui --remote --no-sandbox --port=${PORT}\n\
fi\n' > /start.sh && chmod +x /start.sh
EXPOSE 25808
CMD ["/start.sh"]
EOF
```
## Key Changes Made
The correct filenames for v1.8.26 are:
- **AppImage**: `AionUi-1.8.26-linux-x86_64.AppImage` (not `AionUi-1.8.26.AppImage`)
- **.deb**: `AionUi-1.8.26-linux-amd64.deb` (not `AionUi_1.8.26_amd64.deb`)
Try the first AppImage version now - it should work! The build will take a few minutes.

---

### 🤖 Claude

It looks like this message contains notes and code you've been working through yourself — but there's no question or request directed at me here!

What would you like me to help with? For example:

- Should I run one of these Dockerfiles in my environment and test it?
- Do you want me to verify the actual latest AionUi release and correct filenames from GitHub?
- Are you hitting a specific error you need help debugging?

Let me know where you're stuck!

---

### 🧑 You

how to sign in

---

### 🤖 Claude

AionUi is running successfully at `localhost:25808` — great job getting it working!

For the default login credentials, let me check quickly.

{'type': 'knowledge', 'title': 'AIO default user and password for first login - ℹ️ Support - Nextcloud community', 'url': 'https://help.nextcloud.com/t/aio-default-user-and-password-for-first-login/179171', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'nextcloud.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=nextcloud.com', 'site_name': 'Nextcloud'}, 'is_missing': False, 'text': 'I deployed docker AIO and opened port 80:80 and 443:443 in router firewall and map to internal ip but after downloading container i get to login screen and ask user and password that i didnt setup during install process.…\n\nI deployed docker AIO and opened port 80:80 and 443:443 in router firewall and map to internal ip but after downloading container i get to login screen and ask user and password that i didnt setup during install process.…', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://help.nextcloud.com/t/aio-default-user-and-password-for-first-login/179171', 'search_provider': 'anthropic', 'age': 'January 16, 2024'}} {'type': 'knowledge', 'title': 'Default Credentials - Web Safety', 'url': 'https://www.diladele.com/websafety/docs/faq/admin_ui/default_credentials/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'diladele.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=diladele.com', 'site_name': 'Diladele'}, 'is_missing': False, 'text': 'Default login for Admin UI is admin and password is Passw0rd as shown on the following screenshot. It is recommended to immediately change these default values after installation/deployment to something more appropriate for your network. To change the password from Admin UI, click on the admin ...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.diladele.com/websafety/docs/faq/admin_ui/default_credentials/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'What is the username/password?', 'url': 'https://community.ui.com/questions/What-is-the-username-password/abbbed07-9db0-4844-8ab4-798c384b0f08', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'ui.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=ui.com', 'site_name': 'Ui'}, 'is_missing': False, 'text': 'Loading Ubiquiti Community', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://community.ui.com/questions/What-is-the-username-password/abbbed07-9db0-4844-8ab4-798c384b0f08', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'default userid and password windows network controller', 'url': 'https://community.ui.com/questions/default-userid-and-password-windows-network-controller/64b999ae-e1a6-485d-b4c8-d926e41e8a4a', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'ui.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=ui.com', 'site_name': 'Ui'}, 'is_missing': False, 'text': 'Loading Ubiquiti Community', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://community.ui.com/questions/default-userid-and-password-windows-network-controller/64b999ae-e1a6-485d-b4c8-d926e41e8a4a', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'aion login :: AION Free-to-Play General Discussion', 'url': 'https://steamcommunity.com/app/261430/discussions/0/357287304424372548/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'steamcommunity.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=steamcommunity.com', 'site_name': 'Steam Community'}, 'is_missing': False, 'text': 'This is why the games dead as they cant even get the bloody logins to work.. ... yup tried everything possible checking files reinstall and stuff checking with 2 new fresh acc and stuff not working at all i give up ;p ... Ok I have worked this out, if you make an account @ https://en.aion.gameforge.com/website/register/ It does not work, however if you make an account @ https://en.aion.gameforge.com/website/landing/long/ (CLICK REG BUTTON) it works just fine. Hope this helps someone else.. ... Originally posted by |SOH|Drago:Ok I have worked this out, if you make an account @ https://en.aion.gameforge.com/website/register/ It does not work, however if you make an account @ https://en.aion.gameforge.com/website/landing/long/ (CLICK REG BUTTON) it works just fine. Hope this helps someone else.. lol works thanks ur the mvp now my lil brother can play the game :P ... Originally posted by Mystery G man:correct username, wrong password.\n\nThis is why the games dead as they cant even get the bloody logins to work.. ... yup tried everything possible checking files reinstall and stuff checking with 2 new fresh acc and stuff not working at all i give up ;p ... Ok I have worked this out, if you make an account @ https://en.aion.gameforge.com/website/register/ It does not work, however if you make an account @ https://en.aion.gameforge.com/website/landing/long/ (CLICK REG BUTTON) it works just fine. Hope this helps someone else.. ... Originally posted by |SOH|Drago:Ok I have worked this out, if you make an account @ https://en.aion.gameforge.com/website/register/ It does not work, however if you make an account @ https://en.aion.gameforge.com/website/landing/long/ (CLICK REG BUTTON) it works just fine. Hope this helps someone else.. lol works thanks ur the mvp now my lil brother can play the game :P ... Originally posted by Mystery G man:correct username, wrong password.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://steamcommunity.com/app/261430/discussions/0/357287304424372548/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Log in', 'url': 'https://mypassword.aoins.com/itim/uihelp/en/ui/ref_ui_login.html', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'aoins.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=aoins.com', 'site_name': 'Aoins'}, 'is_missing': False, 'text': 'You can use the Identity Manager Service Center to administer access and manage your activities. You must provide a valid user ID and password to authenticate to the system before you can perform any activities on the Identity Manager Service Center.\n\nIf your password is expired, you must specify a new password. Depending on how your administrator configured the system, you might be required to change your password after your first login. Depending on how your administrator configured the system, you might be logged off after a specific period of inactivity. The default timeout setting for Identity Manager is 30 minutes.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://mypassword.aoins.com/itim/uihelp/en/ui/ref_ui_login.html', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'What is the default username and password for ION/SPM/PME components? | Schneider Electric USA', 'url': 'https://www.se.com/us/en/faqs/FA226215/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'se.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=se.com', 'site_name': 'Schneider Electric'}, 'is_missing': False, 'text': 'IssueWhat is the login credentials for ION/SPM/PME componentsProduct LineION EnterpriseStruxureWare Power MonitoringPower Monitoring ExpertEnvironmentSchneider Electric…', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.se.com/us/en/faqs/FA226215/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'x-ui default credentials · GitHub', 'url': 'https://gist.github.com/imkarimkarim/adb6c5911d22460963b319b81c018942', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'x-ui default credentials. GitHub Gist: instantly share code, notes, and snippets.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://gist.github.com/imkarimkarim/adb6c5911d22460963b319b81c018942', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Default Username and Password for Real-Time Controller or Network Chassis - NI', 'url': 'https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000YGxSCAW', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'ni.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=ni.com', 'site_name': 'NI'}, 'is_missing': False, 'text': 'Home Support Default Username and Password for Real-Time Controller or Network Chassis\n\nHome Support Default Username and Password for Real-Time Controller or Network Chassis', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000YGxSCAW', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Auto Login · Issue #2 · xan105/Aion-Launcher', 'url': 'https://github.com/xan105/Aion-Launcher/issues/2', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Hey, just a short Question, you said: *2 Equivalent of using command line parameter -user -password. Launcher will keep your credentials crypted (aes-256-cbc) on your computer but they will be pass...\n\nHey, just a short Question, you said: *2 Equivalent of using command line parameter -user -password. Launcher will keep your credentials crypted (aes-256-cbc) on your computer but they will be passed clearly to aion.bin so use this at your own risk. so if i used it it will passed to the Aion bin , so how can i remove it from the bin? also WHICH bin file ^^\' i Use Steam Aion and simply tested this feature, but i am also Aware to my data :D · so in short: is there a way to delete my "Login Info" if yes how ^^ ...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/xan105/Aion-Launcher/issues/2', 'search_provider': 'anthropic', 'age': 'April 8, 2019'}}

{'type': 'text', 'text': '{"error_type": "PERMISSIONS_ERROR", "error_message": "This URL cannot be fetched because it was not provided by the user nor did it appear in any search/fetch results"}', 'uuid': '21535918-a8a6-49b8-ac0c-757614a4bbff'}

{'type': 'knowledge', 'title': 'GitHub - iOfficeAI/AionUi: Free, local, open-source 24/7 Cowork app and OpenClaw for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it!', 'url': 'https://github.com/iOfficeAI/AionUi', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Your 24/7 AI assistant — access AionUi from any device, anywhere. WebUI Mode — access via browser from phone, tablet, or any computer. Supports LAN, cross-network, and server deployment. QR code or password login. ... Setup: AionUi Settings → WebUI Settings → Channel, configure the Bot Token. Remote control &amp; monitor your agent — Claude, Gemini, Codex. Use from browser or phone, same as Claude Code remote. ... Set it up once, the AI agent runs automatically on schedule — truly 24/7 unattended operation. Natural Language — tell the agent what to do, just like chatting · Flexible Scheduling — daily, weekly, monthly, or custom cron expressions · Use Cases: scheduled data aggregation, report generation, file organization, reminders ... Conversation-Bound — Each scheduled task is bound to a conversation, maintaining context and history ·\n\nYour 24/7 AI assistant — access AionUi from any device, anywhere. WebUI Mode — access via browser from phone, tablet, or any computer. Supports LAN, cross-network, and server deployment. QR code or password login. ... Setup: AionUi Settings → WebUI Settings → Channel, configure the Bot Token. Remote control & monitor your agent — Claude, Gemini, Codex. Use from browser or phone, same as Claude Code remote. ... Set it up once, the AI agent runs automatically on schedule — truly 24/7 unattended operation. Natural Language — tell the agent what to do, just like chatting · Flexible Scheduling — daily, weekly, monthly, or custom cron expressions · Use Cases: scheduled data aggregation, report generation, file organization, reminders ... Conversation-Bound — Each scheduled task is bound to a conversation, maintaining context and history ·\n\nIf you already use Claude Code, Codex, or Qwen Code, AionUi auto-detects them and lets you Cowork with all of them — alongside the built-in agent. Supported Agents: Built-in Agent (zero setup) • Claude Code • Codex • Qwen Code • Goose AI • OpenClaw • Augment Code • iFlow CLI • CodeBuddy • Kimi CLI • OpenCode • Factory Droid • GitHub Copilot • Qoder CLI • Mistral Vibe • Nanobot and more · Auto Detection — automatically recognizes installed CLI tools · Unified Interface — one Cowork platform for all your AI agents · Parallel Sessions — run multiple agents simultaneously with independent context · MCP Unified Management — configure MCP (Model Context Protocol) tools once, automatically sync to all agents — no need to configure each agent separately · Other AI apps give you a chatbox with your API key. AionUi gives you a full Cowork agent.\n\nSame agent capabilities — file read/write, web search, image generation, tool use — regardless of which model powers it. AionUi supports 20+ AI platforms including cloud services and local deployments. ... Chinese Platforms — Dashscope (Qwen), Zhipu, Moonshot (Kimi), Qianfan (Baidu), Hunyuan (Tencent), Lingyi, ModelScope, InfiniAI, Ctyun, StepFun · International Platforms — DeepSeek, MiniMax, OpenRouter, SiliconFlow, xAI, Ark (Volcengine), Poe · Local Models — Ollama, LM Studio (via Custom platform with local API endpoint) AionUi also supports NewAPI gateway service — a unified AI model hub that aggregates and distributes various LLMs. Flexibly switch between different models in the same interface to meet various task requirements. Extensible assistant system with 12 built-in professional assistants and custom skill support. Create and manage your own assistants and skills.\n\nAionUi includes 12 professional assistants with predefined capabilities, extendable through custom skills: 🤝 Cowork — Autonomous task execution (file operations, document processing, workflow planning) 📊 PPTX Generator — Generate PPTX presentations ... 📋 Planning with Files — File-based planning for complex tasks (Manus-style persistent markdown planning) 🧭 HUMAN 3.0 Coach — Personal development coach · 📣 Social Job Publisher — Job posting and publishing · 🦞 moltbook — Zero-deployment AI agent social networking · 📈 Beautiful Mermaid — Flowcharts, sequence diagrams, and more · 🔧 OpenClaw Setup — Setup and configuration assistant for OpenClaw integration · 📖 Story Roleplay — Immersive story roleplay with character cards and world info (SillyTavern compatible) Custom Skills: Create skills in the skills/ directory, enable/disable skills for assistants to extend AI capabilities.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/iOfficeAI/AionUi', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'WebUI Configuration Guide · iOfficeAI/AionUi Wiki · GitHub', 'url': 'https://github.com/iOfficeAI/AionUi/wiki/WebUI-Configuration-Guide/79b22fb8c249783fd1f4829ba3f80cb7bc07bcf7', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': '======================================== Username: admin Password: [random-password] 🌐 Access URL: http://localhost:25808 ======================================== Important: Copy the password immediately - you&#x27;ll need it to log in!\n\nFree, local, open-source 24/7 Cowork app and OpenClaw for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it! - iOfficeAI/AionUi\n\nThis guide covers how to configure and use AionUi in WebUI mode, enabling browser-based access and remote connections to your local AI assistant. ... Remote Control Your AI Assistant: Access AionUi from any device on your network! Whether you\'re on your phone, tablet, or another computer, just open a web browser and connect to your AionUi instance running on your main machine · Secure Login Required: Your AI conversations and data are protected with user authentication. You\'ll need to create a login account and password to access WebUI mode, ensuring only authorized users can use your AI assistant · Works on Servers Too: Perfect for running AionUi on Linux servers without a desktop environment. Your AI assistant can now run 24/7 on your server and you can access it remotely from anywhere · Smart Network Detection: The system automatically detects and displays the best network address for you to connect.\n\nwget https://github.com/iOfficeAI/AionUi/releases/download/v1.5.2/AionUi_1.5.2_arm64.deb apt install -y ./AionUi_*.deb which AionUi ... Note: The --no-sandbox flag is required in Termux/proot environments. ... [WARNING] Could not connect to session bus... [ERROR] Failed to connect to the bus... [WARNING] Multiple instances of the app detected... These errors are related to D-Bus and X server, which are not needed for WebUI mode. ... Simply open this URL in your browser. The application will automatically open your default browser when started. On first launch, you\'ll see your initial credentials: ======================================== ✅ Default admin user created! ======================================== Username: admin Password: [random-password] 🌐 Access URL: http://localhost:25808 ======================================== Important: Copy the password immediately - you\'ll need it to log in!\n\n[Unit] Description=AionUi WebUI Service After=network.target [Service] Type=simple User=YOUR_USERNAME WorkingDirectory=/home/YOUR_USERNAME ExecStart=/usr/bin/AionUi --webui --remote Restart=on-failure RestartSec=10 [Install] WantedBy=multi-user.target · Important: Replace YOUR_USERNAME with your actual username, and /usr/bin/AionUi with the actual installation path of AionUi. ... # Reload systemd configuration sudo systemctl daemon-reload # Enable auto-start on boot sudo systemctl enable aionui-webui.service # Start the service sudo systemctl start aionui-webui.service # Check service status sudo systemctl status aionui-webui.service ... After the service starts, the terminal will display the access address. You can also check through logs: sudo journalctl -u aionui-webui.service | grep "WebUI" ... 🚀 Local access / 本地访问: http://localhost:25808 🚀 Network access / 网络访问: http://YOUR_SERVER_IP:25808 ·', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/iOfficeAI/AionUi/wiki/WebUI-Configuration-Guide/79b22fb8c249783fd1f4829ba3f80cb7bc07bcf7', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Remote Internet Access Guide · iOfficeAI/AionUi Wiki · GitHub', 'url': 'https://github.com/iOfficeAI/AionUi/wiki/Remote-Internet-Access-Guide', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Enter Chat Interface: After successful login, you&#x27;ll enter the AionUi chat interface. Now you can use AionUi on your phone · Start Conversation: After starting a conversation, you can begin chatting with AionUi ... On first access, the browser may show a security warning, which is normal - click &quot;Continue&quot; to proceed · If you prefer using the command line to start WebUI, you can use the following commands on the computer running AionUi: ... After starting successfully, the terminal will display the access URL and initial password. ... If you have a cloud server (e.g., AWS, Alibaba Cloud, Tencent Cloud, etc.), you can deploy AionUi directly on the server for public internet access. ... [Unit] Description=AionUi WebUI Service After=network.target [Service] Type=simple User=YOUR_USERNAME WorkingDirectory=/home/YOUR_USERNAME ExecStart=/usr/bin/AionUi --webui --remote Restart=on-failure RestartSec=10 [Install] WantedBy=multi-user.target ·\n\nFree, local, open-source 24/7 Cowork and OpenClaw for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it! - iOfficeAI/AionUi\n\n📱 Convenient Login: Support QR code scan for one-click login, no need to remember complex passwords · ⚡ Quick Setup: Complete configuration and start using in just 3-5 minutes · Whether accessing your home server while traveling or enabling remote collaboration for team members, it\'s all easy to achieve! ... AionUi supports three remote connection methods. Choose based on your use case: ... 💡 Video Tutorial: The video above demonstrates the complete configuration process. If the video cannot play, please refer to the text steps below. On the computer running AionUi, open the AionUi application and start the WebUI service from the interface: ... 💡 Tip: If you prefer using the command line, you can also start with --webui --remote parameter (see "Alternative: Command Line Start" below). Visit download page: https://tailscale.com/download ...\n\nEnter Chat Interface: After successful login, you\'ll enter the AionUi chat interface. Now you can use AionUi on your phone · Start Conversation: After starting a conversation, you can begin chatting with AionUi ... On first access, the browser may show a security warning, which is normal - click "Continue" to proceed · If you prefer using the command line to start WebUI, you can use the following commands on the computer running AionUi: ... After starting successfully, the terminal will display the access URL and initial password. ... If you have a cloud server (e.g., AWS, Alibaba Cloud, Tencent Cloud, etc.), you can deploy AionUi directly on the server for public internet access. ... [Unit] Description=AionUi WebUI Service After=network.target [Service] Type=simple User=YOUR_USERNAME WorkingDirectory=/home/YOUR_USERNAME ExecStart=/usr/bin/AionUi --webui --remote Restart=on-failure RestartSec=10 [Install] WantedBy=multi-user.target ·\n\n💡 Tip: Replace YOUR_USERNAME and /usr/bin/AionUi with actual values. If AionUi is not in /usr/bin/, use the full path. sudo systemctl daemon-reload sudo systemctl enable aionui-webui.service sudo systemctl start aionui-webui.service sudo systemctl status aionui-webui.service ... # Ubuntu/Debian (ufw) sudo ufw allow 25808/tcp sudo ufw reload # CentOS/RHEL (firewalld) sudo firewall-cmd --permanent --add-port=25808/tcp sudo firewall-cmd --reload ... <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> <plist version="1.0"> <dict> <key>Label</key> <string>com.aionui.webui</string> <key>ProgramArguments</key> <array> <string>/Applications/AionUi.app/Contents/MacOS/AionUi</string> <string>--webui</string> <string>--remote</string> </array> <key>RunAtLoad</key> <true/> <key>KeepAlive</key> <true/> </dict> </plist> launchctl load ~/Library/LaunchAgents/com.aionui.webui.plist launchctl start com.aionui.webu', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/iOfficeAI/AionUi/wiki/Remote-Internet-Access-Guide', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'AionUi/WEBUI_GUIDE.md at main · iOfficeAI/AionUi', 'url': 'https://github.com/iOfficeAI/AionUi/blob/main/WEBUI_GUIDE.md', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Login with the new password shown in the terminal · If you&#x27;re in a development environment with Node.js, you can also use: # In the project directory npm run --resetpass # Or for a specific user npm run --resetpass username · Main README · 中文说明 · 日本語ドキュメント · GitHub Issues · If you encounter any issues: Check the Troubleshooting section · Search existing issues · Create a new issue with: Your OS and version · AionUi version · Steps to reproduce · Error messages or logs · Happy using AionUi in WebUI mode!\n\nLogin with the new password shown in the terminal · If you\'re in a development environment with Node.js, you can also use: # In the project directory npm run --resetpass # Or for a specific user npm run --resetpass username · Main README · 中文说明 · 日本語ドキュメント · GitHub Issues · If you encounter any issues: Check the Troubleshooting section · Search existing issues · Create a new issue with: Your OS and version · AionUi version · Steps to reproduce · Error messages or logs · Happy using AionUi in WebUI mode!\n\nFree, local, open-source 24/7 Cowork and Clawdbot for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it! - iOfficeAI/AionUi\n\nIf you forgot your admin password in WebUI mode, you can reset it using the --resetpass command. IMPORTANT: The --resetpass command resets the password and generates a new random one. All existing JWT tokens will be invalidated. ... # Using full path "C:\\Program Files\\AionUi\\AionUi.exe" --resetpass # Or for a specific user "C:\\Program Files\\AionUi\\AionUi.exe" --resetpass username ... # Using full path /Applications/AionUi.app/Contents/MacOS/AionUi --resetpass # Or for a specific user /Applications/AionUi.app/Contents/MacOS/AionUi --resetpass username ... # Using system path aionui --resetpass # Or for a specific user aionui --resetpass username # Or using full path /opt/AionUi/aionui --resetpass ...\n\n[Unit] Description=AionUi WebUI Service After=network.target [Service] Type=simple User=YOUR_USERNAME ExecStart=/opt/AionUi/aionui --webui --remote Restart=on-failure RestartSec=10 [Install] WantedBy=multi-user.target ... sudo systemctl daemon-reload sudo systemctl enable aionui-webui.service sudo systemctl start aionui-webui.service # Check status sudo systemctl status aionui-webui.service · Important Note: Electron desktop mode is not supported on Android. However, you can run AionUi in WebUI mode using Termux with a prooted Linux environment. Community Contribution: This guide is contributed by @Manamama. Special thanks for making AionUi accessible on Android devices! 🙏 · Original Tutorial: Running AionUi WebUI on Android via Termux + Proot Ubuntu ... # Install Ubuntu rootfs proot-distro install ubuntu # Login to Ubuntu environment proot-distro login ubuntu ·', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/iOfficeAI/AionUi/blob/main/WEBUI_GUIDE.md', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Configuration Guides · iOfficeAI/AionUi Wiki · GitHub', 'url': 'https://github.com/iOfficeAI/AionUi/wiki/Configuration-Guides', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': "Start WebUI mode · Remote access configuration · Authentication and security setup · Background service deployment · Password management · Common issues and solutions · Installation problems · Configuration issues · Performance troubleshooting · Feature-specific questions · Application Cases: Use Cases Overview - See AionUi in action · Community: GitHub Discussions · Issues: Report Problems · Updates: GitHub Releases · Start Simple: Begin with Google login for Gemini - it&#x27;s the easiest way to get started · Read the Prerequisites: Each guide lists what you need before starting · Check Troubleshooting: If something doesn&#x27;t work, check the FAQ first · Join the Community: Get help from other users in GitHub Discussions · Need help? Check our FAQ or report an issue! Welcome to the comprehensive AionUi documentation! Find everything you need to configure, use, and master AionUi.\n\nFree, local, open-source 24/7 Cowork and OpenClaw for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it! - iOfficeAI/AionUi\n\nStart WebUI mode · Remote access configuration · Authentication and security setup · Background service deployment · Password management · Common issues and solutions · Installation problems · Configuration issues · Performance troubleshooting · Feature-specific questions · Application Cases: Use Cases Overview - See AionUi in action · Community: GitHub Discussions · Issues: Report Problems · Updates: GitHub Releases · Start Simple: Begin with Google login for Gemini - it's the easiest way to get started · Read the Prerequisites: Each guide lists what you need before starting · Check Troubleshooting: If something doesn't work, check the FAQ first · Join the Community: Get help from other users in GitHub Discussions · Need help? Check our FAQ or report an issue! Welcome to the comprehensive AionUi documentation! Find everything you need to configure, use, and master AionUi.\n\nWelcome to AionUi's comprehensive configuration and usage guides! This section provides detailed tutorials for setting up and using all AionUi features. ... Need help? Check our FAQ or report an issue! Welcome to the comprehensive AionUi documentation! Find everything you need to configure, use, and master AionUi.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/iOfficeAI/AionUi/wiki/Configuration-Guides', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'iOfficeAI/AionUi v1.4.0 on GitHub', 'url': 'https://newreleases.io/project/github/iOfficeAI/AionUi/release/v1.4.0', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'newreleases.io', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=newreleases.io', 'site_name': 'New Releases'}, 'is_missing': False, 'text': '# Launch WebUI /Applications/AionUi.app/Contents/MacOS/AionUi --webui # Reset Password (quit AionUi first) /Applications/AionUi.app/Contents/MacOS/AionUi --resetpass admin · # Launch WebUI (right-click desktop shortcut → &quot;Open file location&quot; to copy path) &quot;C:\\Program Files\\AionUi\\AionUi.exe&quot; --webui # Reset Password &quot;C:\\Program Files\\AionUi\\AionUi.exe&quot; --resetpass admin ... # Local Access AionUi --webui # Network Access (LAN) AionUi --webui --remote # Reset Password AionUi --resetpass ... # Local Access sudo AionUi --webui --no-sandbox # Network Access (LAN) sudo AionUi --webui --remote --no-sandbox # Reset Password sudo AionUi --resetpass --no-sandbox · feat: upgrade to aioncli v0.8.1 with MCP integration by @goworm in #192 · fix: Fix the issue of duplicate images pasted in the conversation box. by @kuishou68 in #194 · fix: update version from V1.3.1 to V1.3.2 by @IceyLiu in #196 ...\n\nRemote Control Your AI Assistant - Now you can access AionUi from any device on your network! Whether you\'re on your phone, tablet, or another computer, just open a web browser and connect to your AionUi instance running on your main machine. Secure Login Required - Your AI conversations and data are protected with user authentication. You\'ll need to create a login account and password to access WebUI mode, ensuring only authorized users can use your AI assistant. Works on Servers Too - Perfect for running AionUi on Linux servers without a desktop environment. Your AI assistant can now run 24/7 on your server and you can access it remotely from anywhere. Smart Network Detection - The system automatically detects and displays the best network address for you to connect. On servers, it shows your public IP; on local machines, it shows your local network address.\n\n# Launch WebUI /Applications/AionUi.app/Contents/MacOS/AionUi --webui # Reset Password (quit AionUi first) /Applications/AionUi.app/Contents/MacOS/AionUi --resetpass admin · # Launch WebUI (right-click desktop shortcut → "Open file location" to copy path) "C:\\Program Files\\AionUi\\AionUi.exe" --webui # Reset Password "C:\\Program Files\\AionUi\\AionUi.exe" --resetpass admin ... # Local Access AionUi --webui # Network Access (LAN) AionUi --webui --remote # Reset Password AionUi --resetpass ... # Local Access sudo AionUi --webui --no-sandbox # Network Access (LAN) sudo AionUi --webui --remote --no-sandbox # Reset Password sudo AionUi --resetpass --no-sandbox · feat: upgrade to aioncli v0.8.1 with MCP integration by @goworm in #192 · fix: Fix the issue of duplicate images pasted in the conversation box. by @kuishou68 in #194 · fix: update version from V1.3.1 to V1.3.2 by @IceyLiu in #196 ...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://newreleases.io/project/github/iOfficeAI/AionUi/release/v1.4.0', 'search_provider': 'anthropic', 'age': 'October 23, 2025'}} {'type': 'knowledge', 'title': 'Getting Started · iOfficeAI/AionUi Wiki · GitHub', 'url': 'https://github.com/iOfficeAI/AionUi/wiki/Getting-Started', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': "Welcome to AionUi - the free, open-source, Cowork app with AI Agents! This guide will help you install, configure, and start using AionUi in just 5 minutes. AionUi ships with a complete AI agent engine built in, so it works the moment you install it - no CLI tools to install, no complex setup required. ... After installation, launch AionUi. You&#x27;ll see the welcome interface on first startup: The default interface you see is AionUi&#x27;s built-in Agent (used by default after installation). AionUi also supports Multi-Agent Mode, which allows you to integrate external CLI tools if you already have them installed. For detailed information, please refer to the Multi-Agent Mode Configuration Tutorial. ... Reference Documentation: For advanced authentication options, refer to the LLM Configuration Tutorial. If you prefer using API keys, you can configure multiple platforms: ...\n\nFree, local, open-source 24/7 Cowork app and OpenClaw for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it! - iOfficeAI/AionUi\n\nWelcome to AionUi - the free, open-source, Cowork app with AI Agents! This guide will help you install, configure, and start using AionUi in just 5 minutes. AionUi ships with a complete AI agent engine built in, so it works the moment you install it - no CLI tools to install, no complex setup required. ... After installation, launch AionUi. You'll see the welcome interface on first startup: The default interface you see is AionUi's built-in Agent (used by default after installation). AionUi also supports Multi-Agent Mode, which allows you to integrate external CLI tools if you already have them installed. For detailed information, please refer to the Multi-Agent Mode Configuration Tutorial. ... Reference Documentation: For advanced authentication options, refer to the LLM Configuration Tutorial. If you prefer using API keys, you can configure multiple platforms: ...\n\nWelcome to the comprehensive AionUi documentation! Find everything you need to configure, use, and master AionUi.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/iOfficeAI/AionUi/wiki/Getting-Started', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Releases · iOfficeAI/AionUi', 'url': 'https://github.com/iOfficeAI/AionUi/releases', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Support for the aionui:// URL scheme to pre-fill New-API provider settings, so external links can open AionUi with API config pre-filled. Confirmation dialogs now support keyboard shortcuts so you can confirm or cancel quickly from the keyboard. Slash commands are implemented and supported in the chat interface. WebUI dev-mode proxy is available so slash commands work when developing against the WebUI server. readme remote oinline gif by @ringringlin in #1081 · fix: DashScope Coding Plan model list and WebUI dev server proxy by @kuishou68 in #1087 ... fix(models): update Gemini model references to 3.1 and sync bun.lock with aioncli-core 0.30.0 by @audichuang in #1091 · fix(sendbox): preserve user input during AI reply in Codex/Nanobot/OpenClaw by @cdxiaodong in #1076 · feat: add aionui:// deep link protocol for new-api provider pre-fill by @kuishou68 in #1097 ·\n\nFree, local, open-source 24/7 Cowork app and OpenClaw for Gemini CLI, Claude Code, Codex, OpenCode, Qwen Code, Goose CLI, Auggie, and more | 🌟 Star if you like it! - iOfficeAI/AionUi\n\nSupport for the aionui:// URL scheme to pre-fill New-API provider settings, so external links can open AionUi with API config pre-filled. Confirmation dialogs now support keyboard shortcuts so you can confirm or cancel quickly from the keyboard. Slash commands are implemented and supported in the chat interface. WebUI dev-mode proxy is available so slash commands work when developing against the WebUI server. readme remote oinline gif by @ringringlin in #1081 · fix: DashScope Coding Plan model list and WebUI dev server proxy by @kuishou68 in #1087 ... fix(models): update Gemini model references to 3.1 and sync bun.lock with aioncli-core 0.30.0 by @audichuang in #1091 · fix(sendbox): preserve user input during AI reply in Codex/Nanobot/OpenClaw by @cdxiaodong in #1076 · feat: add aionui:// deep link protocol for new-api provider pre-fill by @kuishou68 in #1097 ·\n\nfix(webui): prevent infinite redirect loop on login page by @kuishou68 in #1106 · fix(build): apply ad-hoc signing for unsigned macOS arm64 builds by @kuishou68 in #1115 · feat(model): 实现模型健康检测、启停开关和开发者调试功能 by @Asunfly in #1085 · fix: address multiple issues found in v1.8.20 audit by @kuishou68 in #1112 · feat(cdp): Add Chrome DevTools Protocol support for AI-assisted debugging by @loonghao in #1002 · fix(webui): open external links on client browser instead of server by @Jassy930 in #1121 · fix(css): 修复设置返回对话页后主题回退问题 by @taekchef in #1109 · fix(webui): resolve multiple WebUI issues (#977, #1075, #1082, #1083, #1113) by @kuishou68 in #1124 · fix(acp): surface relay model_not_found errors to UI by @kuishou68 in #1122 · chore: bump version to 1.8.21 and fix slash command dropdown spacing by @kuishou68 in #1126 ...\n\nfix(build): fix Windows NSIS installer missing AionUi.exe by @kaizhou-lab in #973 ... There was an error while loading. Please reload this page.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/iOfficeAI/AionUi/releases', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'iOfficeAI/AionUi.git:', 'url': 'https://gitee.com/zhouwd/AionUi', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'gitee.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=gitee.com', 'site_name': 'Gitee'}, 'is_missing': False, 'text': 'Username for &#x27;https://gitee.com&#x27;: userName · Password for &#x27;https://userName@gitee.com&#x27;: # Private Token · New file Create Diagram file · New submodule · Upload file · Branches 121 · Tags 116 · contribute · Sync branch · Create Pull ...\n\nWhen using the HTTPS protocol, the command line will prompt for account and password verification as follows. For security reasons, Gitee recommends configure and use personal access tokens instead of login passwords for cloning, pushing, and other operations. Username for \'https://gitee.com\': userName · Password for \'https://userName@gitee.com\': # Private Token · New file Create Diagram file · New submodule · Upload file · Branches 121 · Tags 116 · contribute · Sync branch · Create Pull Request · known more · See difference Through Pull Request Sync · Sync branch · Through Pull Request Sync · A Pull Request will be created to the current branch and will be merged in to complete the sync · 瓦砾 Merge pull request #795 from iOfficeAI/doc... b3ee53c · 2295 commits · .aionui · Save Cancel · .claude/skills/i18n · Save Cancel · .gemini · Save Cancel ·\n\nWhen using the HTTPS protocol, the command line will prompt for account and password verification as follows. For security reasons, Gitee recommends configure and use personal access tokens instead of login passwords for cloning, pushing, and other operations. ... Apache License Version 2.0, January 2004 http://www.apache.org/licenses/ TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION 1. Definitions. "License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document. "Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License. "Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwi\n\nThis operation requires login to the code cloud account. Please log in before operating. ... No account.\n\nHowever, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability. END OF TERMS AND CONDITIONS APPENDIX: How to apply the Apache License to your work. To apply the Apache License to your work, attach the following boilerplate notice, with the fields enclosed by brackets "[]" replaced with your own identifying information. (Don\'t include the brackets!) The text should be enclosed in the appropriate comment syntax for the file format. We also recommend that a file or class name and description of purpose be included on the same "printed page" as the copyright notice for easier identification within third-party archives. Copyright 2025 AionUi (aionui.com) Licensed under the Apache Licen', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://gitee.com/zhouwd/AionUi', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'AionUi download | SourceForge.net', 'url': 'https://sourceforge.net/projects/aionui.mirror/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'sourceforge.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=sourceforge.net', 'site_name': 'SourceForge'}, 'is_missing': False, 'text': 'This is an exact mirror of the AionUi project, hosted at https://github.com/iOfficeAI/AionUi. SourceForge is not affiliated with AionUi. ... AionUi is an open-source, cross-platform graphical interface that turns command-line AI tools into a unified coworking desktop for interacting with multiple local AI agents and CLI models like Gemini CLI, Claude Code, Codex, Qwen Code, and others. Instead of forcing users to work in separate terminals for each tool, AionUi automatically detects installed CLI tools and provides a central visual workspace where sessions can run in parallel, contexts are preserved, and conversations are saved locally without sending data to external servers. It enhances productivity by offering smart file management features like batch renaming, automatic organization, and intelligent file classification, thereby reducing manual overhead when working with large datasets or complex document structures. AionUi also supports a remote WebUI mode, allowing users to access\n\nThis is an exact mirror of the AionUi project, hosted at https://github.com/iOfficeAI/AionUi. SourceForge is not affiliated with AionUi. ... AionUi is an open-source, cross-platform graphical interface that turns command-line AI tools into a unified coworking desktop for interacting with multiple local AI agents and CLI models like Gemini CLI, Claude Code, Codex, Qwen Code, and others. Instead of forcing users to work in separate terminals for each tool, AionUi automatically detects installed CLI tools and provides a central visual workspace where sessions can run in parallel, contexts are preserved, and conversations are saved locally without sending data to external servers. It enhances productivity by offering smart file management features like batch renaming, automatic organization, and intelligent file classification, thereby reducing manual overhead when working with large datasets or complex document structures. AionUi also supports a remote WebUI mode, allowing users to access', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://sourceforge.net/projects/aionui.mirror/', 'search_provider': 'anthropic'}}
Found it! The password is **randomly generated on first launch** and printed in the Docker container logs. Run this to find it:

```bash
docker logs aionui | grep -A5 "admin user created\|Password\|Username"
```

You should see output like:
```
✅ Default admin user created!
Username: admin
Password: [some-random-password]
```

**Username:** `admin`  
**Password:** check the logs with the command above

If the password isn't visible in the logs (because the container started before you were watching), **reset it** with:

```bash
docker exec aionui /app/AionUi.AppImage --appimage-extract-and-run --resetpass admin
```

Then check the logs again:
```bash
docker logs aionui | tail -20
```

It will print a new random password. Copy it and use it to log in!

---

### 🤖 Claude

The logs show your login attempt returned **401**, meaning wrong credentials. The password isn't printed in the logs — it's stored in the app's database. Let me help you find or reset it.

The AionUi data is stored in the Docker volume. Run this to find and reset the admin password directly in the database:

```bash
# Find the database file in the volume
docker exec aionui find /root/.config -name "*.db" -o -name "*.sqlite" 2>/dev/null
```

If that finds a database, then:

```bash
# Check what's in the users table
docker exec aionui sh -c "find /root/.config -name '*.db' | xargs -I{} sqlite3 {} 'SELECT * FROM users;' 2>/dev/null || find /root/.config -name '*.sqlite' | xargs -I{} sqlite3 {} 'SELECT * FROM users;' 2>/dev/null"
```

Alternatively, look for any config/credential files:

```bash
docker exec aionui find /root/.config/AionUi -type f | head -30
docker exec aionui cat /root/.config/AionUi/config.json 2>/dev/null || true
docker exec aionui ls /root/.config/AionUi/
```

Also scroll up in the full logs to catch the very first startup (when the user was created):

```bash
docker logs aionui 2>&1 | grep -i "password\|admin\|user\|created\|init" | head -20
```

The default credentials are likely stored somewhere in that volume. Once you find the db file, we can either read the password or reset it with a known hash. Share the output and I'll give you the exact next step!

---

### 🤖 Claude

The database exists but `sqlite3` returned no results — it's probably not installed in the container. Let's install it and query directly:

```bash
# Install sqlite3 in the container and query the users table
docker exec aionui sh -c "apt-get install -q -y sqlite3 2>/dev/null && sqlite3 /root/.config/AionUi/aionui/aionui.db '.tables'"
```

Then see the users:

```bash
docker exec aionui sqlite3 /root/.config/AionUi/aionui/aionui.db "SELECT id, username, password FROM users;"
```

Once we see the password hash, we can reset it. Run this to set the password to `admin123`:

```bash
# Generate a bcrypt hash for "admin123" and update it
docker exec aionui sh -c "apt-get install -q -y python3 2>/dev/null && python3 -c \"
import hashlib, os
# Try simple hash first - check what format existing password uses
import sqlite3
conn = sqlite3.connect('/root/.config/AionUi/aionui/aionui.db')
cur = conn.cursor()
cur.execute('SELECT username, password FROM users')
rows = cur.fetchall()
for r in rows:
    print('User:', r[0], '| Hash:', r[1][:50], '...')
conn.close()
\""
```

This will show us the username and what hashing format is used, then I can give you the exact command to reset it to a known password.

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ # Install sqlite3 in the container and query the users table docker exec aionui sh -c "apt-get install -q -y sqlite3 2>/dev/null && sqlite3 /root/.config/AionUi/aionui/aionui.db '.tables'" Reading package lists... Building dependency tree... Reading state information... ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ docker exec aionui sqlite3 /root/.config/AionUi/aionui/aionui.db "SELECT id, username, password FROM users;" OCI runtime exec failed: exec failed: unable to start container process: exec: "sqlite3": executable file not found in $PATH ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ # Generate a bcrypt hash for "admin123" and update it docker exec aionui sh -c "apt-get install -q -y python3 2>/dev/null && python3 -c \" import hashlib, os # Try simple hash first - check what format existing password uses import sqlite3 conn = sqlite3.connect('/root/.config/AionUi/aionui/aionui.db') cur = conn.cursor() cur.execute('SELECT username, password FROM users') rows = cur.fetchall() for r in rows:    print('User:', r[0], '| Hash:', r[1][:50], '...') conn.close() \"" Reading package lists... Building dependency tree... Reading state information... python3 is already the newest version (3.10.6-1~22.04.1). python3 set to manually installed. 0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded. Traceback (most recent call last):  File "<string>", line 7, in <module> sqlite3.OperationalError: no such column: password ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯

---

### 🤖 Claude

Good progress! The column isn't called `password`. Let's check the actual schema:

```bash
docker exec aionui python3 -c "
import sqlite3
conn = sqlite3.connect('/root/.config/AionUi/aionui/aionui.db')
cur = conn.cursor()
# List all tables
cur.execute(\"SELECT name FROM sqlite_master WHERE type='table'\")
print('Tables:', cur.fetchall())
# Show users table schema
cur.execute(\"PRAGMA table_info(users)\")
print('Users columns:', cur.fetchall())
conn.close()
"
```

This will show us the exact column names. Share the output and I'll give you the reset command immediately!

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ docker exec aionui python3 -c " import sqlite3 conn = sqlite3.connect('/root/.config/AionUi/aionui/aionui.db') cur = conn.cursor() # List all tables cur.execute(\"SELECT name FROM sqlite_master WHERE type='table'\") print('Tables:', cur.fetchall()) # Show users table schema cur.execute(\"PRAGMA table_info(users)\") print('Users columns:', cur.fetchall()) conn.close() " Tables: [('users',), ('messages',), ('assistant_users',), ('assistant_sessions',), ('assistant_pairing_codes',), ('cron_jobs',), ('assistant_plugins',), ('conversations',)] Users columns: [(0, 'id', 'TEXT', 0, None, 1), (1, 'username', 'TEXT', 1, None, 0), (2, 'email', 'TEXT', 0, None, 0), (3, 'password_hash', 'TEXT', 1, None, 0), (4, 'avatar_path', 'TEXT', 0, None, 0), (5, 'jwt_secret', 'TEXT', 0, None, 0), (6, 'created_at', 'INTEGER', 1, None, 0), (7, 'updated_at', 'INTEGER', 1, None, 0), (8, 'last_login', 'INTEGER', 0, None, 0)] ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯

---

### 🤖 Claude

The column is `password_hash`. Now let's see the existing user and hash format, then reset it:

```bash
docker exec aionui python3 -c "
import sqlite3
conn = sqlite3.connect('/root/.config/AionUi/aionui/aionui.db')
cur = conn.cursor()
cur.execute('SELECT id, username, email, password_hash FROM users')
rows = cur.fetchall()
for r in rows:
    print('ID:', r[0])
    print('Username:', r[1])
    print('Email:', r[2])
    print('Hash:', r[3])
conn.close()
"
```

Then reset the password to `admin123`:

```bash
docker exec aionui python3 -c "
import sqlite3, hashlib, os
# Install bcrypt if needed
import subprocess
subprocess.run(['pip3', 'install', 'bcrypt', '-q', '--break-system-packages'])
import bcrypt
new_hash = bcrypt.hashpw(b'admin123', bcrypt.gensalt()).decode('utf-8')
conn = sqlite3.connect('/root/.config/AionUi/aionui/aionui.db')
cur = conn.cursor()
cur.execute('UPDATE users SET password_hash = ? WHERE username = ?', (new_hash, 'admin'))
conn.commit()
print('Updated rows:', cur.rowcount)
conn.close()
print('Password reset to: admin123')
"
```

After that, log in with **username: `admin`** and **password: `admin123`**. If `rowcount` shows 0, share the username from the first command and I'll adjust!

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ docker exec aionui python3 -c " import sqlite3 conn = sqlite3.connect('/root/.config/AionUi/aionui/aionui.db') cur = conn.cursor() cur.execute('SELECT id, username, email, password_hash FROM users') rows = cur.fetchall() for r in rows:    print('ID:', r[0])    print('Username:', r[1])    print('Email:', r[2])    print('Hash:', r[3]) conn.close() " ID: system_default_user Username: admin Email: None Hash: $2a$12$zWdSHfHLQw2eBM/sOk1O/uzC4EbJI12HmfpMGmu2nVv4X1qmEMQFy ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ docker exec aionui python3 -c " import sqlite3, hashlib, os # Install bcrypt if needed import subprocess subprocess.run(['pip3', 'install', 'bcrypt', '-q', '--break-system-packages']) import bcrypt new_hash = bcrypt.hashpw(b'admin123', bcrypt.gensalt()).decode('utf-8') conn = sqlite3.connect('/root/.config/AionUi/aionui/aionui.db') cur = conn.cursor() cur.execute('UPDATE users SET password_hash = ? WHERE username = ?', (new_hash, 'admin')) conn.commit() print('Updated rows:', cur.rowcount) conn.close() print('Password reset to: admin123') " Traceback (most recent call last):  File "<string>", line 5, in <module>  File "/usr/lib/python3.10/subprocess.py", line 503, in run    with Popen(*popenargs, **kwargs) as process:  File "/usr/lib/python3.10/subprocess.py", line 971, in __init__    self._execute_child(args, executable, preexec_fn, close_fds,  File "/usr/lib/python3.10/subprocess.py", line 1863, in _execute_child    raise child_exception_type(errno_num, err_msg, err_filename) FileNotFoundError: [Errno 2] No such file or directory: 'pip3' ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯

---

### 🤖 Claude

The hash starts with `$2a$12$` — that's bcrypt. Let's install pip properly first:

```bash
docker exec aionui sh -c "apt-get install -q -y python3-pip 2>/dev/null && pip install bcrypt -q --break-system-packages && python3 -c \"
import sqlite3, bcrypt
new_hash = bcrypt.hashpw(b'admin123', bcrypt.gensalt()).decode('utf-8')
conn = sqlite3.connect('/root/.config/AionUi/aionui/aionui.db')
cur = conn.cursor()
cur.execute('UPDATE users SET password_hash = ? WHERE username = ?', (new_hash, 'admin'))
conn.commit()
print('Updated rows:', cur.rowcount)
conn.close()
print('Done! Login with: admin / admin123')
\""
```

Then try logging in at `http://localhost:25808` with:
- **Username:** `admin`
- **Password:** `admin123`

---
