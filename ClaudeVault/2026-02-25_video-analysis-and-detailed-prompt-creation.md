---
title: "Video analysis and detailed prompt creation"
date: 2026-02-25
tags:
  - sql
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - job-search
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

# Video analysis and detailed prompt creation

> **Conversation Overview**

The person is building a project called WorldView Geospatial Intelligence, a futuristic cyberpunk-aesthetic geospatial dashboard inspired by military command centers and platforms like Palantir. The project uses React 19 with TypeScript, D3.js for geospatial rendering, Motion (formerly Framer Motion) for UI transitions, Tailwind CSS 4.0, and Lucide React icons. The conversation began with the person sharing a YouTube video link for analysis, which Claude could not directly access. Claude requested the transcript or a description instead, then proceeded to generate detailed image prompts, video prompts, and a 10-scene animation prompt pack based on the video's described content about a Palantir-inspired geospatial platform built in a weekend.

The person then described their own WorldView implementation in detail, prompting Claude to build a full React JSX single-file component featuring an orthographic globe with drag-to-rotate, toggleable data layers (satellites, commercial flights, military aircraft, seismic activity), three visual filter modes (Standard, NVG, FLIR), animated CRT scanlines and flicker effects, live UTC clock, signal spectrum visualizers, camera presets, and a seismic event detail panel. When the person asked to make it "actually functional," Claude began building a more advanced version incorporating real API integrations: USGS earthquake feed, OpenSky Network for live flights, CelesTrak for satellite TLE data with simplified SGP4 propagation, and Natural Earth TopoJSON for real country borders.

The person then requested a comprehensive prompt rather than direct code generation, and Claude produced a detailed master build prompt covering the full technical stack, four real data sources with exact API URLs and data schemas, globe rendering specifications using D3 geoOrthographic, visual filter implementation details, CSS grid layout specifications, data layer rendering details, performance optimization strategies, and error handling with fallback data. The person subsequently requested feature expansion prompts for six additional capabilities: space debris tracking with satellite footprint visualization, maritime AIS vessel tracking, real-time weather and NASA FIRMS wildfire data, a Web Audio API immersive soundscape system, historical time-machine playback with snapshot buffering, and a responsive tactical mobile layout. Claude delivered each as a self-contained, paste-ready prompt with exact API endpoints, rendering specifications, fallback strategies, and implementation notes, concluding with a master integration prompt to unify all modules.

**Date:** 2026-02-25  
**Topics:** [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[Job-Search]] · [[History]] · [[Geopolitics]] · [[Stock-Market]] · [[Research]] · [[Creative]] · [[Finance]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

https://youtu.be/rXvU7bPJ8n4?si=LHzP3NrHNFASceOF   analysis this video and provide me complete in detail prompt

---

### 🤖 Claude

{'type': 'text', 'text': '{"error_type": "PERMISSIONS_ERROR", "error_message": "This URL cannot be fetched because it was not provided by the user nor did it appear in any search/fetch results"}', 'uuid': 'b2e0d82a-fcaf-496f-a7bc-9cb712054cb4'}


{'type': 'knowledge', 'title': 'About YouTube - YouTube', 'url': 'https://about.youtube/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'about.youtube', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=about.youtube', 'site_name': 'YouTube'}, 'is_missing': False, 'text': 'YouTube’s mission is to give everyone a voice and show them the world. Learn about our brand, community, careers and more.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://about.youtube/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Cправка - YouTube', 'url': 'https://support.google.com/youtube/?hl=ru', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'google.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=google.com', 'site_name': 'Google Support'}, 'is_missing': False, 'text': 'Официальный справочный центр YouTube, где можно найти советы и руководства по использованию продукта, а также ответы на часто задаваемые вопросы.\n\nCправка - YouTube · Войти · Справка Google · Справочный центр · Сообщество · YouTube · Политика конфиденциальности · Условия использования YouTube · Отправить отзыв · Тема отзыва · Информация в текущем разделе Справочного центра · Общие впечатления о Справочном центре Google · Далее · Справочный центр · Сообщество · Советы авторам · YouTube · Уведомление · Читайте команду @TeamYouTube в X (бывшем Твиттере), чтобы узнавать последние новости и ответы на ваши вопросы на французском и русском языках.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://support.google.com/youtube/?hl=ru', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Troubleshoot YouTube video errors - YouTube Help', 'url': 'https://support.google.com/youtube/answer/3037019?hl=en', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'google.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=google.com', 'site_name': 'Google Support'}, 'is_missing': False, 'text': "Learn more about the process and what data is available. Try closing the YouTube app or rebooting your device. You can also uninstall and reinstall the YouTube app. Try updating your browser or clear your browser&#x27;s cache and cookies. Check your extensions, including ad blockers · Check whether ...\n\nTroubleshoot problems playing videosTroubleshoot account issuesFix upload problemsGet help with the YouTube Partner ProgramLearn about recent updates on YouTubeGet help with YouTube ... Find videos to watchChange video settingsWatch videos on different devicesComment, subscribe, & connect with creatorsSave or share videos & playlistsTroubleshoot problems playing videosPurchase & manage movies, TV shows & products on YouTube ... Sign up and manage your accountManage account settingsManage privacy settingsManage ad settingsManage accessibility settingsTroubleshoot account issuesYouTube updates ... Join YouTube PremiumYouTube Premium benefitsManage your Premium membershipManage Premium billing & paymentsFix YouTube Premium issues ... Upload videosEdit videos & video settingsCreate ShortsEdit videos with YouTube CreateCustomize & manage your channelAnalyze performance with analyticsTranslate videos, subtitles, & captionsManage your posts & commentsLive stream on YouTubeYouTube Creator Comm\n\nYouTube Partner ProgramMake money on YouTubeGet paidUnderstand ads and related policiesGet help with the YouTube Partner ProgramYouTube for Content Managers ... If you’re having problems playing your YouTube video, try these troubleshooting steps to solve your issue. ... If you get an error message while watching a video, you can try these possible solutions. Restart your internet connection. Run an internet speed test to make sure your internet can support the selected video resolution. Using multiple devices on the same network may reduce the speed that your device gets. You can also change the quality of your video to improve your experience. Check the YouTube video’s resolution and the recommended speed needed to play the video. The table below shows the approximate speeds recommended to play each video resolution. If you're interested in seeing more info on how your videos are played back, check out Stats for Nerds.\n\nCheck your device settings to make sure you turned on data usage for YouTube on your device. ... Make sure you’re signed in to YouTube. In order to protect the YouTube community, we may prevent signed-out users from accessing YouTube videos when they’re attempting to download material for offline use. If you're a researcher trying to access YouTube data for your academic research, you can apply to YouTube’s researcher program. Learn more about the process and what data is available. Try closing the YouTube app or rebooting your device. You can also uninstall and reinstall the YouTube app. Try updating your browser or clear your browser's cache and cookies. Check your extensions, including ad blockers · Check whether your browser extensions that block ads are affecting video playback. As another option, try opening YouTube in an incognito window with all extensions disabled and check if the issue continues.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://support.google.com/youtube/answer/3037019?hl=en', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'YouTube Downloader - Download YouTube Videos in HD | YTDown', 'url': 'https://app.ytdown.to/en7/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'ytdown.to', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=ytdown.to', 'site_name': 'Ytdown'}, 'is_missing': False, 'text': "After pasting the link and clicking Download, you&#x27;re then presented with the Download page to select various formats for your video, you&#x27;ll then find the option to convert your YouTube video to MP3 (when available). 3. How long does it take to download videos using YTDown? The time it takes to download videos from YTDown is determined by the file size and video quality you pick. For HD or 4K videos, it may take a few minutes. However, YTDown&#x27;s fast servers ensure that the download procedure, whether MP3 or MP4, runs quickly and smoothly. 4. Is it safe to download YouTube videos with YTDown? Yes, the YTDown YouTube Video Downloader is entirely safe to use. We value user privacy and security. When you download videos from YTDown, you do not have to worry about data security or malware. Our downloader provides the finest user experience while maintaining strong security requirements.\n\nYTDown is one of the best YouTube video downloaders for MP3 and MP4 formats. It offers a free, easy-to-use tool that allows you to save videos (up to 1080p), Shorts, and images from YouTube with just one click. Whether you want to download a high-resolution video, a YouTube Shorts clip, or simply save a photo from a YouTube post, YTDown makes the process fast and simple. Just enter the YouTube link, select the desired quality, and download it directly to your device. ... Once you've downloaded a YouTube video using YTDown.com, it's usually stored in the default 'Downloads' folder on your device. To access this folder, simply go to your device's file manager or browser settings, and you should find a section labeled 'Downloads'. If you've chosen a specific location to save downloads during the process, please navigate to that location to find your downloaded videos.\n\nAfter pasting the link and clicking Download, you're then presented with the Download page to select various formats for your video, you'll then find the option to convert your YouTube video to MP3 (when available). 3. How long does it take to download videos using YTDown? The time it takes to download videos from YTDown is determined by the file size and video quality you pick. For HD or 4K videos, it may take a few minutes. However, YTDown's fast servers ensure that the download procedure, whether MP3 or MP4, runs quickly and smoothly. 4. Is it safe to download YouTube videos with YTDown? Yes, the YTDown YouTube Video Downloader is entirely safe to use. We value user privacy and security. When you download videos from YTDown, you do not have to worry about data security or malware. Our downloader provides the finest user experience while maintaining strong security requirements.\n\nDownloading YouTube videos has never been faster with YTDown. In just a few seconds, you can save your favorite videos to your device without needing to download any apps or create an account. ... Whether you're using an Android or an iPhone, YTDown makes downloading YouTube videos straightforward. Simply paste the video URL, select your preferred format, and your videos will be saved to your device with a few simple clicks. ... YTDown allows you to download YouTube videos in HD quality in seconds.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://app.ytdown.to/en7/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'YouTube throwing "Content not available" on nearly every video for some', 'url': 'https://piunikaweb.com/2026/01/23/youtube-content-unavailable-message-appears-on-nearly-every-video-for-some-users-potential-workarounds-inside/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'piunikaweb.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=piunikaweb.com', 'site_name': 'PiunikaWeb'}, 'is_missing': False, 'text': 'Home YouTube “Content unavailable” message appears on nearly every video for some users, potential workarounds inside ... Update 27/01/26 – 11:16 am (IST): AdGuard support has officially acknowledged the issue, confirming that their filter team is currently investigating the cause. As a temporary solution, they recommend enabling the AdGuard Experimental filter within the extension’s settings, noting that this step is sufficient to resolve the error in most cases. For users on the Manifest V3 (MV3) architecture, simple filter updates might not be enough. Developers have provided specific script snippets that need to be manually added to the “User Rules” section of the extension to bypass the detection.\n\nHome YouTube “Content unavailable” message appears on nearly every video for some users, potential workarounds inside ... Update 27/01/26 – 11:16 am (IST): AdGuard support has officially acknowledged the issue, confirming that their filter team is currently investigating the cause. As a temporary solution, they recommend enabling the AdGuard Experimental filter within the extension’s settings, noting that this step is sufficient to resolve the error in most cases. For users on the Manifest V3 (MV3) architecture, simple filter updates might not be enough. Developers have provided specific script snippets that need to be manually added to the “User Rules” section of the extension to bypass the detection.\n\nwww.youtube.com#@%#(()=>{const t={construct:(t,e,c)=>{try{const n=e[0];let o=e[1]?.body;if(!n?.includes("youtubei")||location.href.includes("/shorts/")||location.href.includes("youtube.com/tv")||location.href.includes("youtube.com/embed/")||!o)return Reflect.construct(t,e,c);if(o.includes(\'"contentPlaybackContext"\')||o.includes(\'"adSignalsInfo"\')){const n=JSON.parse(o);if(!n.context?.client)return Reflect.construct(t,e,c);n.playbackContext&&(n.playbackContext.adPlaybackContext={pyv:!0}),n.playerRequest&&(n.playerRequest.playbackContext.adPlaybackContext={pyv:!0}),o=JSON.stringify(n),e[1].body=o}}catch(t){}return Reflect.construct(t,e,c)}};window.Request=new Proxy(window.Request,t)})(); www.youtube.com#@%#(()=>{const e={apply:(e,t,n)=>{if(location.href.includes("/shorts/")||location.href.includes("youtube.com/tv")||location.href.includes("youtube.com/embed/"))return Reflect.apply(e,t,n);try{let o=n[0];if(o&&(o.includes(\'"contentPlaybackContext"\')||o.includes(\'"adSignalsInfo"\'))){const c', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://piunikaweb.com/2026/01/23/youtube-content-unavailable-message-appears-on-nearly-every-video-for-some-users-potential-workarounds-inside/', 'search_provider': 'anthropic', 'age': '1 month ago'}} {'type': 'knowledge', 'title': '🚨 [FIXED] Issues accessing YouTube - YouTube Community', 'url': 'https://support.google.com/youtube/thread/410904426/%F0%9F%9A%A8-fixed-issues-accessing-youtube?hl=en', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'google.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=google.com', 'site_name': 'Google Support'}, 'is_missing': False, 'text': 'YouTube Help · Sign in · Google Help · Help Center · Fix a problem · Watch videos · Manage your account &amp; settings · Supervised experiences on YouTube · YouTube Premium · Create &amp; grow your channel · Monetize with the YouTube Partner Program · Policy, safety, &amp; copyright · Community · YouTube · Privacy Policy · YouTube Terms of Service · Submit feedback · Send feedback on... This help content &amp; information · General Help Center experience · Next · Help Center · Community · Creator Tips · YouTube · false · Search · Clear search · Close search · Google apps · Main menu · 6400346349766976397 · true · Search Help Center · false · true · true · true · true · true · 59 · false ·', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://support.google.com/youtube/thread/410904426/%F0%9F%9A%A8-fixed-issues-accessing-youtube?hl=en', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Free YouTube Video Downloader 2025 – 4K & 1080p, No Ads', 'url': 'https://www.clipto.com/media-downloader/youtube-downloader', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'clipto.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=clipto.com', 'site_name': 'Clipto'}, 'is_missing': False, 'text': "Yes. With Clipto&#x27;s YouTube Video Downloader, you can easily and safely download YouTube videos on iPhone or Android. Simply copy the YouTube link, paste it into the downloader, choose your preferred format, and start the download. Once saved, the video will appear on your phone and can be watched ...\n\nYouTube Video DownloaderTikTok Video DownloaderInstagram Video DownloaderTwitter(X.com) Video Downloader ... Download and save YouTube videos for free with Clipto YouTube Video Downloader. Convert YouTube to MP4 or MP3 in 1080p, 4K or 8K. No ads. No watermark. Ultra-fast. Please make sure the files you download comply with copyright laws. This tool cannot be used to download copyrighted music. ... Convert YouTube videos to high-quality MP3 effortlessly with Clipto AI. ... A video-to-text transcription tool automatically converts video or audio content into accurate text. ... Download TikTok videos without watermark. Fast, free, no sign up needed. ... Easily download Twitter videos in high quality with our free Twitter video downloader. ... Save Facebook videos in high quality for free with our easy-to-use Facebook downloader. ... Easily download Instagram videos in high quality with our free Instagram video downloader.\n\nUsing our free YouTube video downloader is quick and easy. Simply copy the URL of the video you want to download from YouTube, and paste it into the input box of our downloader. The tool will automatically process the video, and once it’s ready, you can click to download it directly to your device.\\n\\nIf you also need a text version of the video, tools like Clipto Transcription can convert the audio into written content for easier reference. In some cases, using a YouTube video downloader is legal. You can safely download videos that are copyright-free, have a Creative Commons license, or when you have permission from the creator. To stay compliant, avoid downloading copyrighted content without authorization and always follow YouTube’s Terms of Service and copyright policies. No, you don’t need to install any software! Our YouTube downloader is fully web-based, allowing you to download videos directly from your browser.\n\nYes, our YouTube video downloader is 100% free, with no hidden fees or download limits. You can download videos anytime without restrictions and without needing to sign up.\\n\\nIf you need to convert YouTube videos into text, tools like Clipto Transcription can help. It offers a 7-day free trial and can transcribe videos into subtitles, notes, or full transcripts. Download times vary depending on the video length, your internet speed, and server load. Shorter videos download faster, but even longer videos can be processed quickly with our optimized system. You don't need to install any additional software or browser extensions to download YouTube videos online with Clipto.AI. Simply paste the video URL into the input field, choose your preferred format and quality, and start the download instantly. Everything happens right in your browser, making it a fast, safe, and hassle-free option.\n\nYes. With Clipto's YouTube Video Downloader, you can easily and safely download YouTube videos on iPhone or Android. Simply copy the YouTube link, paste it into the downloader, choose your preferred format, and start the download. Once saved, the video will appear on your phone and can be watched anytime, even without an internet connection. With a trusted third-party tool like Clipto.AI, you can save videos directly to your device in just a few steps. Copy the YouTube link, paste it into the downloader, select your preferred format and quality, and download the file. Once saved, the video will be available on your device for offline viewing anytime, without requiring an internet connection. Yes, Clipto.AI offers a 100% safe video downloader that allows you to download YouTube videos for free in a secure and reliable manner. The platform is ad-free and works directly in your browser.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.clipto.com/media-downloader/youtube-downloader', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Download YouTube Videos | Mydowndown Video Download Tool', 'url': 'https://en.mydowndown.com/y2', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'mydowndown.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=mydowndown.com', 'site_name': 'Mydowndown'}, 'is_missing': False, 'text': 'Mydowndown is an online tool for downloading Facebook, Youtube, Dailymotion, Twitter, Tumblr, Instagram, Vimeo, and Xuite videos without installing any software. It helps you find and save any videos you want to keep or record.\n\n支援 facebook(含私人), Youtube, Dailymotion, Twitter, Tumblr, Instagram, Vimeo, Vine, Xuite · 97速借網 全台最大借款平台： 借貸, 借錢, 信貸, 車貸, 房貸, 企業貸款, 小額借款, 支票, ...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://en.mydowndown.com/y2', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': "YouTube's More Affordable Premium Lite Plan Gets New Perks - MacRumors", 'url': 'https://www.macrumors.com/2026/02/24/youtube-lite-plan-upgrade/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'macrumors.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=macrumors.com', 'site_name': 'MacRumors'}, 'is_missing': False, 'text': 'Probably the only subscription where I feel I&#x27;m getting the most value for my money is YouTube Premium. Nothing comes even close. I just hope we&#x27;re not in the honeymoon phase and then they go for the kill like most subscription services do. ... Step 1. Ratchet ads to the point that the service becomes unusable. Step 2. Charge to make it barely usable again. Step 3. Repeat. ... YT Premium is probably the most bang for the buck in my entire subscription life. No ADs on YT and YT Music combo is exceptional value that I use the HECK out of. ... YouTube Premium Lite in theUS starts at $10.99 not $7.99 Maybe if you&#x27;re trying to subscribe through the Apple app store. It&#x27;s definitely $7.99 on the website. ... I would pay extra to disable shorts. Their existence makes YouTube insufferable. ... Our comprehensive guide highlighting every major new addition in iOS 26, plus how-tos that walk you through using the new features.\n\nYouTube today updated its Premium Lite subscription plan with new features, including background play and downloads. Subscribers will be able to watch most videos ad-free offline and in the background. Prior to now, downloads and background play were features that were limited to the more expensive Premium plan. YouTube Premium Lite is priced at $7.99 per month in the U.S., while YouTube Premium is priced at $13.99 per month. YouTube Premium Lite removes ads from most, but not all videos, and it does not include ad-free access to the YouTube Music app. Most non-music content is ad-free with YouTube Premium Lite, though Shorts still have ads. YouTube Premium removes ads from all videos, including music content, plus it has extra features like jump ahead, queuing, and continue watching. YouTube says that background play and downloads are rolling out to Premium Lite subscribers starting today, but it may take a few weeks for everyone to get access to the new features.\n\nIn his Power On newsletter today, Bloomberg\'s Mark Gurman said Apple will have a three-day stretch of product announcements from Monday, March 2 through Wednesday, March 4. In total, he expects Apple to introduce "at least five products." Subscribe to the MacRumors YouTube channel for more videos. A week ago, Apple invited selected journalists and content creators to an "Apple Experience" in... ... Apple\'s software engineers are testing iOS 26.3.1, according to the MacRumors visitor logs, which have been a reliable indicator of upcoming iOS versions. iOS 26.3.1 should be a minor update that fixes bugs and/or security vulnerabilities, and it will likely be released within the next two weeks. Last month, Apple released iOS 26.2.1 with bug fixes and support for the second-generation... ... The special new color that Apple is considering for the iPhone 18 Pro and iPhone 18 Pro Max this year is red, according to Bloomberg\'s Mark Gurman.\n\nProbably the only subscription where I feel I\'m getting the most value for my money is YouTube Premium. Nothing comes even close. I just hope we\'re not in the honeymoon phase and then they go for the kill like most subscription services do. ... Step 1. Ratchet ads to the point that the service becomes unusable. Step 2. Charge to make it barely usable again. Step 3. Repeat. ... YT Premium is probably the most bang for the buck in my entire subscription life. No ADs on YT and YT Music combo is exceptional value that I use the HECK out of. ... YouTube Premium Lite in theUS starts at $10.99 not $7.99 Maybe if you\'re trying to subscribe through the Apple app store. It\'s definitely $7.99 on the website. ... I would pay extra to disable shorts. Their existence makes YouTube insufferable. ... Our comprehensive guide highlighting every major new addition in iOS 26, plus how-tos that walk you through using the new features.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.macrumors.com/2026/02/24/youtube-lite-plan-upgrade/', 'search_provider': 'anthropic', 'age': '6 hours ago'}} {'type': 'knowledge', 'title': 'Youtube Downloader HD 線上影片下載及轉檔', 'url': 'https://www.youtubedownloaderhd.com/index-ch.html', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'youtubedownloaderhd.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=youtubedownloaderhd.com', 'site_name': 'Youtube Downloader HD'}, 'is_missing': False, 'text': 'Youtube Downloader HD 是可以將YouTube影片下載到本機電腦的免費工具，下載的影片可以轉成AVI或MP4格式（與iPhone或iPad相容）。 ... 現在你可以從YouTube下載高畫質(High Quality)、HD(High Definition)及Full HD影片，更棒的是 - Youtube Downloader ...\n\nYoutube Downloader HD 是可以將YouTube影片下載到本機電腦的免費工具，下載的影片可以轉成AVI或MP4格式（與iPhone或iPad相容）。 ... 現在你可以從YouTube下載高畫質(High Quality)、HD(High Definition)及Full HD影片，更棒的是 - Youtube Downloader HD 是免費軟體！ ...\n\nYoutube Downloader HD是完全免費的軟體，絕對不含廣告軟體、間諜軟體、註冊視窗、彈出視窗、惡意軟體或其他令人厭惡的軟體。 Youtube Downloader HD僅為個人下載用途所設計，在取得任何資源時，請尊重版權所有人的權利。\n\nYoutube Downloader HD 是可以將YouTube影片下載到本機電腦的免費工具，下載的影片可以轉成AVI或MP4格式（與iPod或iPhone相容）。', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.youtubedownloaderhd.com/index-ch.html', 'search_provider': 'anthropic'}}

Unfortunately, I'm not able to directly watch or analyze YouTube videos — I can't access video content or audio from YouTube links. My tools allow me to fetch web pages and search the internet, but not stream or process video/audio media.

Here's what I **can** do to help you get a detailed prompt from that video:

**Option 1 — Share the transcript**
Copy the video's auto-generated transcript (click the three dots under the video → "Show transcript") and paste it here. I'll analyze it and write a detailed prompt.

**Option 2 — Share screenshots/frames**
Take screenshots of key moments in the video and upload them here. I can analyze the images and build a prompt from them.

**Option 3 — Describe the video**
Tell me what the video is about (topic, style, visuals, purpose), and I'll craft a detailed, comprehensive prompt based on your description.

Which approach works best for you?

---

### 🤖 Claude

Great — you've already got the full analysis! Here's a clean, organized breakdown of everything you need:

---

## 🎬 Video Summary

**"Ex-Google Maps PM Vibe Coded Palantir In a Weekend"** by Bilawal Sidhu (ex-Google Maps PM)

He built **WorldView** — a real-time geospatial intelligence platform combining:
- **CesiumJS + Google 3D Tiles** (photorealistic globe)
- **Live public data feeds** (OpenSky, ADS-B Exchange, USGS, OSM, Austin CCTV)
- Built in **3 days** using parallel AI agents (Gemini 1.5 Pro + Claude Sonnet + CodeX)

---

## 🖼️ Master Image Prompt (Copy-Paste Ready)

```
A hyper-realistic screenshot of a futuristic geospatial intelligence 
dashboard called "WorldView" running in a Chrome browser window on a 
completely black background, 8K screen capture, sharp UI, cinematic lighting.

Main viewport: photorealistic 3D globe rendered with Google Earth 3D Tiles 
photogrammetry, ultra-detailed terrain, cities, and buildings at night. 
The globe is slightly tilted, showing North America and Europe.

Real-time data overlays (all glowing with subtle bloom and scanline effects):
- Hundreds of white glowing satellite dots with thin orbital path trails 
  and small NORAD ID labels.
- 6,700+ commercial airplane icons in electric blue with tiny contrails.
- Military aircraft icons in bright safety-orange.
- Dense glowing green particle systems simulating live street traffic 
  flowing along real OpenStreetMap road networks.
- Multiple live CCTV video feeds from Austin, Texas, seamlessly projected 
  and texture-mapped onto actual 3D building geometry and sidewalks — 
  real pedestrians and cars visible in the video feeds.
- Pulsing red seismic activity dots and concentric wave circles across the globe.

Active visual filter: mixed CRT + Night Vision + FLIR hybrid — phosphor 
green tint, subtle horizontal scanlines, mild chromatic aberration, retro 
CRT curvature, thermal color accents on heat sources, film grain, vignette.

UI elements (clean cyberpunk HUD style):
- Left sidebar: "Data Layers" panel with toggles — Satellites (Live), 
  Flights (OpenSky), Military (ADS-B Exchange), Traffic, CCTV (Austin), 
  Seismic (USGS).
- Top bar: "WorldView" logo in futuristic sans-serif, UTC time, zoom level, 
  coordinates.
- Right panel: Camera Presets — "Burj Khalifa", "London Bridge", 
  "Times Square", "Area 51", "Sydney Opera House".
- Bottom HUD: mini-map, icon legend, FPS counter 87, 
  "6,742 aircraft tracked", "183 satellites visible".

Overall atmosphere: dark cyberpunk military command center, high-tech 
surveillance aesthetic, Palantir Gotham meets Google Earth on steroids, 
neon cyan and orange glows, volumetric god rays from data points, 
ultra-sharp 8K, cinematic color grading, dramatic rim lighting on UI panels, 
slight screen reflection and dust particles for realism.

Photorealistic screen capture, no text blur, perfect pixel alignment, 
high-end monitor, aspect ratio 16:9

--ar 16:9 --stylize 250 --v 6
```

---

## 🎨 4 Alternate Mood Variants

| Mode | Append This to the Prompt |
|------|--------------------------|
| **Night Vision** | `night vision mode active, strong green monochrome palette, heavy digital noise, green phosphor glow, crosshair overlay` |
| **FLIR Thermal** | `FLIR thermal imaging active, white-hot vehicles and people, deep blue cold background, heat signatures glowing orange-red, thermal color grading` |
| **CRT Retro** | `heavy CRT filter, curved screen, thick scanlines, phosphor burn-in, 240p retro computer aesthetic, RGB color separation` |
| **Austin CCTV Zoom** | Replace globe with: `extreme close-up on Austin Texas at night, live CCTV feeds mapped onto 3D buildings, pedestrians on crosswalks visible, orange military aircraft overhead` |

---

## ⏱️ Key Timestamps Reference

| Time | What's Shown |
|------|-------------|
| 0:49 | Cyberpunk UI + CRT/Night Vision/FLIR filters |
| 2:23 | All satellites in orbit (NORAD trails) |
| 3:12 | 6,700+ commercial flights (blue icons) |
| 4:25 | Military aircraft (orange icons) |
| 5:26 | Traffic as glowing particle systems |
| 6:37 | Live CCTV projected onto 3D buildings |
| 8:02 | Global earthquake/seismic pulsing dots |

---

Want me to also generate a **video prompt** (for Runway / Kling / Luma) or a **full 10-scene animation prompt pack** based on these timestamps?

---

### 🤖 Claude

You've got everything you need right there! Here's a clean, organized final version of both deliverables:

---

## 🎥 Single Video Prompt (Runway / Kling / Luma)

```
A hyper-realistic, cinematic 15-second video demo of a futuristic 
geospatial intelligence dashboard called "WorldView" running in a 
Chrome browser on a completely black background, 8K resolution, 
sharp UI, dynamic lighting with bloom and god rays.

Start with a slow orbiting camera around a photorealistic 3D globe 
(Google Earth 3D Tiles photogrammetry), ultra-detailed night-time 
terrain. Gradually activate real-time data overlays:

- White satellite dots tracing orbital paths with NORAD ID labels
- 6,700+ electric blue airplane icons with contrails moving in real-time
- Bright orange military aircraft icons blinking on
- Green particle systems flowing as street traffic on OSM road networks
- Live CCTV feeds from Austin TX projected onto 3D building geometry 
  with pedestrians and cars visible
- Pulsing red seismic dots with concentric wave ripples

Visual filter evolves: CRT + Night Vision + FLIR hybrid at start → 
full Night Vision at 5s → FLIR Thermal by end.

UI animates in cyberpunk HUD style: sidebar toggles activate, 
WorldView logo glows neon, UTC clock ticks, camera presets trigger 
fly-to Burj Khalifa, stats update live ("6,742 aircraft tracked").

Dark cyberpunk military command center atmosphere, Palantir Gotham 
meets Google Earth, neon cyan/orange glows, volumetric god rays, 
dramatic rim lighting, screen reflections, dust motes.

--ar 16:9 --stylize 250 --v 6 --duration 15 --loop
```

---

## 📽️ 10-Scene Animation Prompt Pack

### Scene 1 — Intro: UI Activation (0:00–0:10)
```
Dark Chrome browser opens on black background, WorldView dashboard 
loads with cinematic fade-in. Photorealistic 3D globe spins into view 
(Google Earth tiles, night cities glowing). CRT/Night Vision/FLIR 
hybrid filter activates: green phosphor tint, scanlines flicker on. 
UI panels slide in, sidebar glows, top bar logo pulses neon. Slow 
camera orbit. Cyberpunk atmosphere, cyan glows, screen dust.
--ar 16:9 --stylize 250
```

### Scene 2 — Satellites in Orbit (0:10–0:20)
```
Hundreds of white satellite dots populate with bloom, thin orbital 
trails trace like comet paths, NORAD ID labels fade in/out. Night 
Vision green monochrome deepens with digital noise. HUD updates: 
"183 satellites visible." Volumetric god rays from each dot.
--ar 16:9 --stylize 250
```

### Scene 3 — Commercial Flights (0:20–0:30)
```
6,700+ electric blue airplane icons appear with contrails streaking 
in real-time arcs. Camera pans over North America/Europe showing 
density. Thermal filter adds orange engine heat glows. Stats update: 
"6,742 aircraft tracked." Dramatic rim lighting on trails.
--ar 16:9 --stylize 250
```

### Scene 4 — Military Aircraft (0:30–0:40)
```
Bright orange military icons pop in, camera briefly chases one in a 
zoom. FLIR filter activates: white-hot signatures on aircraft. "Area 
51" camera preset button glows on right panel. FPS counter at 87. 
High-tech surveillance vibe intensifies.
--ar 16:9 --stylize 250
```

### Scene 5 — Street Traffic Particles (0:40–0:50)
```
Camera zooms to city-scale over Europe. Dense green particle systems 
flow like glowing rivers along OpenStreetMap roads, pulsing with 
traffic density, particles accelerate and decelerate. CRT scanlines 
thicken, vignette darkens edges. Traffic layer toggle activates.
--ar 16:9 --stylize 250
```

### Scene 6 — Live CCTV Projection (0:50–1:00)
```
Extreme close-up on Austin Texas at night. Live CCTV feeds 
texture-mapped onto 3D buildings and sidewalks — pedestrians walking 
crosswalks, cars driving with motion blur. Orange military aircraft 
flies overhead. Full FLIR thermal: heat signatures glow on people and 
vehicles. Realistic screen reflection on panel frames.
--ar 16:9 --stylize 250
```

### Scene 7 — Global Seismic Activity (1:00–1:10)
```
Camera pulls back to full globe. Red seismic dots pulse and erupt 
with concentric wave circles rippling outward, clustering in hotspots. 
Seismic USGS toggle pulses in sync. Hybrid filter with vignette and 
grain. Cyberpunk god rays intensify across the globe.
--ar 16:9 --stylize 250
```

### Scene 8 — Camera Presets Fly-Through (1:10–1:20)
```
Rapid montage of fly-to presets: Burj Khalifa glowing, London Bridge 
with traffic particles, Times Square with dense CCTV overlays, Area 51 
with military clustering, Sydney Opera House with seismic waves. 
Smooth cinematic transitions, filter cycles Night Vision/FLIR/CRT. 
HUD coordinates update live each destination.
--ar 16:9 --stylize 250
```

### Scene 9 — Full Data Fusion Climax (1:20–1:30)
```
All layers simultaneously active: satellites, flights, military, 
traffic, CCTV, seismic overlapping in chaotic harmony. Camera orbits 
dynamically, maximum bloom and scanlines. Neon cyan and orange at 
peak intensity. UI fully lit, stats ticking rapidly. Maximum cyberpunk 
military command center aesthetic.
--ar 16:9 --stylize 250
```

### Scene 10 — Outro Loop (1:30–1:40)
```
Fade to stable global view, all elements pulsing gently. WorldView 
logo centers with final glow. CRT retro filter settles: curved screen, 
phosphor burn-in, RGB separation. Bottom caption: "Built in 3 days 
with AI agents." Slow infinite orbit loop. Cinematic color grading, 
dust particles, high-end monitor realism.
--ar 16:9 --stylize 250 --loop
```

---

## 🛠️ Quick Tool Guide

| Tool | Best Scenes | Tips |
|------|-------------|------|
| **Runway Gen-3** | All 10 scenes | Use storyboard mode, chain with cuts |
| **Kling AI** | Scenes 6, 8, 9 | Enable "Dynamic" motion |
| **Luma Dream Machine** | Scenes 1, 10 | Select "Cinematic" style |
| **Midjourney** | Any scene as still | Add `--v 6 --stylize 250` |

Stitch all 10 scenes in **CapCut** or **DaVinci Resolve** with 0.3s cross-fades for a seamless ~90-second reel. Want me to write the audio/music brief or a voiceover script to go along with it?

---

### 🧑 You

I have built WorldView Geospatial Intelligence, a futuristic, high-fidelity geospatial dashboard inspired by advanced military command centers and cyberpunk aesthetics.
Key Features:
3D Interactive Globe: A custom-built orthographic projection using D3.js and TopoJSON, featuring smooth rotation and real-time data mapping.
Dynamic Data Layers:
Orbital Assets: Real-time tracking of simulated satellites with NORAD ID labels.
Global Air Traffic: Simultaneous monitoring of commercial (blue) and strategic military (orange) aircraft.
Seismic Activity: Live USGS-style earthquake monitoring with pulsing magnitude indicators.
Advanced Visual Modes:
Standard: High-contrast digital interface.
Night Vision (NVG): Green phosphor tint with increased contrast and digital noise.
FLIR Thermal: Heat-signature simulation with white-hot signatures for strategic assets.
Cyberpunk HUD: A complex, glass-morphism interface featuring:
Live UTC telemetry and coordinate tracking.
Interactive layer toggles and view mode switching.
Real-time signal and bandwidth visualization.
CRT scanlines, vignettes, and screen flicker effects for maximum immersion.
Technical Stack:
Frontend: React 19 with TypeScript.
Visualization: D3.js for geospatial rendering.
Animation: Motion (formerly Framer Motion) for UI transitions.
Styling: Tailwind CSS 4.0 with custom cyberpunk themes and SVG filters.
Icons: Lucide-React for crisp, technical iconography.
The application is fully responsive and designed to feel like a "crafted" specialist tool rather than a standard web app. All systems are online and monitoring global telemetry.

---

### 🤖 Claude

{'type': 'text', 'text': '     1\t---\n     2\tname: frontend-design\n     3\tdescription: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.\n     4\tlicense: Complete terms in LICENSE.txt\n     5\t---\n     6\t\n     7\tThis skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.\n     8\t\n     9\tThe user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.\n    10\t\n    11\t## Design Thinking\n    12\t\n    13\tBefore coding, understand the context and commit to a BOLD aesthetic direction:\n    14\t- **Purpose**: What problem does this interface solve? Who uses it?\n    15\t- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.\n    16\t- **Constraints**: Technical requirements (framework, performance, accessibility).\n    17\t- **Differentiation**: What makes this UNFORGETTABLE? What\'s the one thing someone will remember?\n    18\t\n    19\t**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.\n    20\t\n    21\tThen implement working code (HTML/CSS/JS, React, Vue, etc.) that is:\n    22\t- Production-grade and functional\n    23\t- Visually striking and memorable\n    24\t- Cohesive with a clear aesthetic point-of-view\n    25\t- Meticulously refined in every detail\n    26\t\n    27\t## Frontend Aesthetics Guidelines\n    28\t\n    29\tFocus on:\n    30\t- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend\'s aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.\n    31\t- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.\n    32\t- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.\n    33\t- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.\n    34\t- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.\n    35\t\n    36\tNEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.\n    37\t\n    38\tInterpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.\n    39\t\n    40\t**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.\n    41\t\n    42\tRemember: Claude is capable of extraordinary creative work. Don\'t hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.\n    43\t', 'uuid': '0921a43f-1177-47ee-af7b-ef478a96c320'}
Now let me build this. This is a complex, maximalist cyberpunk dashboard — I'll go all-in.

{'type': 'text', 'text': 'File created successfully: /mnt/user-data/outputs/worldview.jsx', 'uuid': 'e548ba87-c691-4e68-90af-d39dcf296f6d'}

{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/worldview.jsx', 'name': 'worldview', 'mime_type': None, 'uuid': '2bea2e05-7736-471f-ae4f-3013aa8d255b'}
Here's your **WorldView Geospatial Intelligence Dashboard** — a fully functional React artifact built from scratch. Here's what's packed in:

**🌍 Globe**
- Custom orthographic projection (pure math, no D3 dependency needed in artifact) with lat/lng grid, equator highlight, and atmosphere glow
- Drag to rotate, auto-rotates when idle

**📡 Data Layers (all toggleable)**
- 180 orbital satellites with pulsing ping animations and NORAD IDs
- 120 commercial flights (blue) + 22 military assets (orange) rendered as directional aircraft icons
- 10 USGS-style seismic events with pulsing magnitude rings

**🎛️ Visual Modes**
- **STD** — cyan/blue cyberpunk command center
- **NVG** — green phosphor night vision with noise
- **FLIR** — thermal orange/white-hot palette

**HUD Features**
- Live UTC Zulu clock ticking every second
- Real-time signal spectrum + bandwidth visualizers (animated)
- Camera preset fly-to buttons (New York, Burj Khalifa, Tokyo, Area 51, Pacific)
- Seismic event detail panel (click any event)
- CRT scanline sweep, corner brackets, screen flicker effects
- Bottom threat board with all seismic events at a glance

---

### 🧑 You

give me code to make it actually functional

---

### 🤖 Claude

Let me look at what we have and then build a fully functional version with real APIs and proper D3/CesiumJS-style rendering.

{'type': 'text', 'text': '     1\timport { useState, useEffect, useRef, useCallback } from "react";\n     2\t\n     3\t// ─── Constants ───────────────────────────────────────────────────────────────\n     4\tconst SATELLITES = Array.from({ length: 180 }, (_, i) => ({\n     5\t  id: `NOA-${10000 + i}`,\n     6\t  lat: (Math.random() - 0.5) * 160,\n     7\t  lng: Math.random() * 360 - 180,\n     8\t  alt: 400 + Math.random() * 1200,\n     9\t  speed: 0.02 + Math.random() * 0.04,\n    10\t  inclination: Math.random() * 90,\n    11\t  active: Math.random() > 0.15,\n    12\t}));\n    13\t\n    14\tconst COMMERCIAL_FLIGHTS = Array.from({ length: 120 }, (_, i) => ({\n    15\t  id: `FL${1000 + i}`,\n    16\t  lat: (Math.random() - 0.5) * 120,\n    17\t  lng: Math.random() * 360 - 180,\n    18\t  heading: Math.random() * 360,\n    19\t  speed: 0.05 + Math.random() * 0.08,\n    20\t  altitude: 30000 + Math.random() * 10000,\n    21\t  type: "commercial",\n    22\t}));\n    23\t\n    24\tconst MILITARY_FLIGHTS = Array.from({ length: 22 }, (_, i) => ({\n    25\t  id: `MIL-${200 + i}`,\n    26\t  lat: (Math.random() - 0.5) * 140,\n    27\t  lng: Math.random() * 360 - 180,\n    28\t  heading: Math.random() * 360,\n    29\t  speed: 0.08 + Math.random() * 0.12,\n    30\t  altitude: 50000 + Math.random() * 20000,\n    31\t  type: "military",\n    32\t}));\n    33\t\n    34\tconst EARTHQUAKES = [\n    35\t  { id: "EQ001", lat: 35.6, lng: 139.7, mag: 5.2, depth: 42, region: "Honshu, Japan" },\n    36\t  { id: "EQ002", lat: -33.4, lng: -70.6, mag: 4.8, depth: 67, region: "Chile" },\n    37\t  { id: "EQ003", lat: 37.7, lng: -122.4, mag: 3.1, depth: 12, region: "California, USA" },\n    38\t  { id: "EQ004", lat: 28.6, lng: 77.2, mag: 4.4, depth: 35, region: "Northern India" },\n    39\t  { id: "EQ005", lat: -6.2, lng: 106.8, mag: 5.7, depth: 80, region: "Java, Indonesia" },\n    40\t  { id: "EQ006", lat: 19.4, lng: -155.2, mag: 3.8, depth: 28, region: "Hawaii, USA" },\n    41\t  { id: "EQ007", lat: 38.7, lng: -27.0, mag: 4.2, depth: 15, region: "Azores, Portugal" },\n    42\t  { id: "EQ008", lat: -17.7, lng: 178.3, mag: 6.1, depth: 560, region: "Fiji" },\n    43\t  { id: "EQ009", lat: 51.2, lng: -178.4, mag: 4.9, depth: 22, region: "Alaska, USA" },\n    44\t  { id: "EQ010", lat: 0.5, lng: 101.4, mag: 5.3, depth: 55, region: "Sumatra, Indonesia" },\n    45\t];\n    46\t\n    47\tconst CAMERA_PRESETS = [\n    48\t  { name: "NEW YORK", lat: 40.7, lng: -74.0, zoom: 3 },\n    49\t  { name: "BURJ KHL", lat: 25.2, lng: 55.3, zoom: 3 },\n    50\t  { name: "TOKYO", lat: 35.7, lng: 139.7, zoom: 3 },\n    51\t  { name: "AREA 51", lat: 37.2, lng: -115.8, zoom: 4 },\n    52\t  { name: "PACIFIC", lat: 0, lng: -160, zoom: 1 },\n    53\t];\n    54\t\n    55\t// ─── Utils ───────────────────────────────────────────────────────────────────\n    56\tfunction toRad(d) { return d * Math.PI / 180; }\n    57\t\n    58\tfunction projectOrtho(lat, lng, centerLat, centerLng, scale) {\n    59\t  const φ = toRad(lat), λ = toRad(lng);\n    60\t  const φ0 = toRad(centerLat), λ0 = toRad(centerLng);\n    61\t  const cosC = Math.sin(φ0) * Math.sin(φ) + Math.cos(φ0) * Math.cos(φ) * Math.cos(λ - λ0);\n    62\t  if (cosC < 0.01) return null;\n    63\t  const x = Math.cos(φ) * Math.sin(λ - λ0);\n    64\t  const y = Math.cos(φ0) * Math.sin(φ) - Math.sin(φ0) * Math.cos(φ) * Math.cos(λ - λ0);\n    65\t  return { x: x * scale, y: -y * scale, depth: cosC };\n    66\t}\n    67\t\n    68\tfunction formatUTC() {\n    69\t  return new Date().toISOString().replace("T", " ").slice(0, 19) + " UTC";\n    70\t}\n    71\t\n    72\t// ─── Globe SVG Component ──────────────────────────────────────────────────────\n    73\tfunction Globe({ layers, viewMode, centerLat, centerLng, scale }) {\n    74\t  const r = scale;\n    75\t\n    76\t  const getColor = (base) => {\n    77\t    if (viewMode === "nvg") return "#00ff41";\n    78\t    if (viewMode === "flir") return "#ff6b00";\n    79\t    return base;\n    80\t  };\n    81\t\n    82\t  const projectedSatellites = layers.satellites\n    83\t    ? SATELLITES.map(s => {\n    84\t        const p = projectOrtho(s.lat, s.lng, centerLat, centerLng, r);\n    85\t        return p ? { ...s, ...p } : null;\n    86\t      }).filter(Boolean).sort((a, b) => b.depth - a.depth)\n    87\t    : [];\n    88\t\n    89\t  const projectedFlights = layers.flights\n    90\t    ? COMMERCIAL_FLIGHTS.map(f => {\n    91\t        const p = projectOrtho(f.lat, f.lng, centerLat, centerLng, r);\n    92\t        return p ? { ...f, ...p } : null;\n    93\t      }).filter(Boolean)\n    94\t    : [];\n    95\t\n    96\t  const projectedMilitary = layers.military\n    97\t    ? MILITARY_FLIGHTS.map(f => {\n    98\t        const p = projectOrtho(f.lat, f.lng, centerLat, centerLng, r);\n    99\t        return p ? { ...f, ...p } : null;\n   100\t      }).filter(Boolean)\n   101\t    : [];\n   102\t\n   103\t  const projectedEarthquakes = layers.seismic\n   104\t    ? EARTHQUAKES.map(eq => {\n   105\t        const p = projectOrtho(eq.lat, eq.lng, centerLat, centerLng, r);\n   106\t        return p ? { ...eq, ...p } : null;\n   107\t      }).filter(Boolean)\n   108\t    : [];\n   109\t\n   110\t  const globeFill = viewMode === "nvg"\n   111\t    ? "url(#nvgGlobe)"\n   112\t    : viewMode === "flir"\n   113\t    ? "url(#flirGlobe)"\n   114\t    : "url(#globeGrad)";\n   115\t\n   116\t  return (\n   117\t    <svg viewBox={`${-r * 1.05} ${-r * 1.05} ${r * 2.1} ${r * 2.1}`} style={{ width: "100%", height: "100%", overflow: "visible" }}>\n   118\t      <defs>\n   119\t        <radialGradient id="globeGrad" cx="35%" cy="30%">\n   120\t          <stop offset="0%" stopColor="#0a2040" />\n   121\t          <stop offset="40%" stopColor="#051530" />\n   122\t          <stop offset="100%" stopColor="#020a18" />\n   123\t        </radialGradient>\n   124\t        <radialGradient id="nvgGlobe" cx="35%" cy="30%">\n   125\t          <stop offset="0%" stopColor="#003300" />\n   126\t          <stop offset="60%" stopColor="#001a00" />\n   127\t          <stop offset="100%" stopColor="#000800" />\n   128\t        </radialGradient>\n   129\t        <radialGradient id="flirGlobe" cx="35%" cy="30%">\n   130\t          <stop offset="0%" stopColor="#1a0800" />\n   131\t          <stop offset="60%" stopColor="#0d0400" />\n   132\t          <stop offset="100%" stopColor="#050100" />\n   133\t        </radialGradient>\n   134\t        <radialGradient id="atmosphereGrad" cx="50%" cy="50%">\n   135\t          <stop offset="70%" stopColor="transparent" />\n   136\t          <stop offset="100%" stopColor={viewMode === "nvg" ? "#00ff4122" : viewMode === "flir" ? "#ff6b0022" : "#00d4ff22"} />\n   137\t        </radialGradient>\n   138\t        <filter id="glow">\n   139\t          <feGaussianBlur stdDeviation="2" result="blur" />\n   140\t          <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>\n   141\t        </filter>\n   142\t        <filter id="strongGlow">\n   143\t          <feGaussianBlur stdDeviation="4" result="blur" />\n   144\t          <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>\n   145\t        </filter>\n   146\t        <clipPath id="globeClip">\n   147\t          <circle r={r} />\n   148\t        </clipPath>\n   149\t      </defs>\n   150\t\n   151\t      {/* Globe base */}\n   152\t      <circle r={r} fill={globeFill} />\n   153\t\n   154\t      {/* Latitude/longitude grid */}\n   155\t      <g clipPath="url(#globeClip)" opacity={viewMode === "nvg" ? 0.4 : 0.15}>\n   156\t        {[-60, -30, 0, 30, 60].map(lat => {\n   157\t          const points = [];\n   158\t          for (let lng = -180; lng <= 180; lng += 3) {\n   159\t            const p = projectOrtho(lat, lng, centerLat, centerLng, r);\n   160\t            if (p) points.push(`${p.x},${p.y}`);\n   161\t          }\n   162\t          return points.length > 2 ? (\n   163\t            <polyline key={lat} points={points.join(" ")}\n   164\t              fill="none" stroke={getColor("#00d4ff")} strokeWidth="0.4" />\n   165\t          ) : null;\n   166\t        })}\n   167\t        {[-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180].map(lng => {\n   168\t          const points = [];\n   169\t          for (let lat = -90; lat <= 90; lat += 3) {\n   170\t            const p = projectOrtho(lat, lng, centerLat, centerLng, r);\n   171\t            if (p) points.push(`${p.x},${p.y}`);\n   172\t          }\n   173\t          return points.length > 2 ? (\n   174\t            <polyline key={lng} points={points.join(" ")}\n   175\t              fill="none" stroke={getColor("#00d4ff")} strokeWidth="0.4" />\n   176\t          ) : null;\n   177\t        })}\n   178\t      </g>\n   179\t\n   180\t      {/* Equator highlight */}\n   181\t      <g clipPath="url(#globeClip)">\n   182\t        {(() => {\n   183\t          const points = [];\n   184\t          for (let lng = -180; lng <= 180; lng += 2) {\n   185\t            const p = projectOrtho(0, lng, centerLat, centerLng, r);\n   186\t            if (p) points.push(`${p.x},${p.y}`);\n   187\t          }\n   188\t          return points.length > 2 ? (\n   189\t            <polyline points={points.join(" ")} fill="none"\n   190\t              stroke={getColor("#00d4ff")} strokeWidth="1.2" opacity="0.5" />\n   191\t          ) : null;\n   192\t        })()}\n   193\t      </g>\n\t< truncated lines 194-552 >\n   553\t          pointerEvents: "none", zIndex: 5,\n   554\t        }} />\n   555\t\n   556\t        {/* Globe */}\n   557\t        <div style={{ width: "70%", maxWidth: 520, aspectRatio: "1" }}>\n   558\t          <Globe layers={layers} viewMode={viewMode}\n   559\t            centerLat={rotation.lat} centerLng={rotation.lng} scale={scale} />\n   560\t        </div>\n   561\t\n   562\t        {/* Corner brackets */}\n   563\t        {[\n   564\t          { top: 12, left: 12 }, { top: 12, right: 12 },\n   565\t          { bottom: 12, left: 12 }, { bottom: 12, right: 12 }\n   566\t        ].map((pos, i) => (\n   567\t          <div key={i} style={{\n   568\t            position: "absolute", ...pos, width: 20, height: 20,\n   569\t            borderTop: i < 2 ? `2px solid ${C.accent}88` : "none",\n   570\t            borderBottom: i >= 2 ? `2px solid ${C.accent}88` : "none",\n   571\t            borderLeft: i % 2 === 0 ? `2px solid ${C.accent}88` : "none",\n   572\t            borderRight: i % 2 === 1 ? `2px solid ${C.accent}88` : "none",\n   573\t          }} />\n   574\t        ))}\n   575\t\n   576\t        {/* Center crosshair */}\n   577\t        <div style={{\n   578\t          position: "absolute", pointerEvents: "none",\n   579\t          width: 30, height: 30,\n   580\t        }}>\n   581\t          <svg width="30" height="30" viewBox="0 0 30 30">\n   582\t            <line x1="15" y1="0" x2="15" y2="10" stroke={C.accent} strokeWidth="1" opacity="0.5" />\n   583\t            <line x1="15" y1="20" x2="15" y2="30" stroke={C.accent} strokeWidth="1" opacity="0.5" />\n   584\t            <line x1="0" y1="15" x2="10" y2="15" stroke={C.accent} strokeWidth="1" opacity="0.5" />\n   585\t            <line x1="20" y1="15" x2="30" y2="15" stroke={C.accent} strokeWidth="1" opacity="0.5" />\n   586\t            <circle cx="15" cy="15" r="3" fill="none" stroke={C.accent} strokeWidth="1" opacity="0.7" />\n   587\t          </svg>\n   588\t        </div>\n   589\t\n   590\t        {/* Stats overlay bottom-center */}\n   591\t        <div style={{\n   592\t          position: "absolute", bottom: 16, left: "50%", transform: "translateX(-50%)",\n   593\t          display: "flex", gap: "20px",\n   594\t          background: `${C.panel}cc`, border: `1px solid ${C.dim}`,\n   595\t          padding: "6px 16px",\n   596\t        }}>\n   597\t          {[\n   598\t            { label: "AIRCRAFT", value: layers.flights ? (COMMERCIAL_FLIGHTS.length + (layers.military ? MILITARY_FLIGHTS.length : 0)).toString() : "0" },\n   599\t            { label: "SATELLITES", value: layers.satellites ? SATELLITES.filter(s => s.active).length.toString() : "0" },\n   600\t            { label: "SEISMIC", value: layers.seismic ? EARTHQUAKES.length.toString() : "0" },\n   601\t          ].map(stat => (\n   602\t            <div key={stat.label} style={{ textAlign: "center" }}>\n   603\t              <div style={{ color: C.accent, fontSize: "14px", fontWeight: 700 }}>{stat.value}</div>\n   604\t              <div style={{ color: C.text, fontSize: "8px", letterSpacing: "2px", opacity: 0.6 }}>{stat.label}</div>\n   605\t            </div>\n   606\t          ))}\n   607\t        </div>\n   608\t      </div>\n   609\t\n   610\t      {/* ══════════════ RIGHT PANEL ══════════════ */}\n   611\t      <div style={{\n   612\t        ...panelStyle,\n   613\t        padding: "12px 10px",\n   614\t        display: "flex", flexDirection: "column", gap: "8px",\n   615\t        borderLeft: `1px solid ${C.dim}`,\n   616\t        overflowY: "auto",\n   617\t      }}>\n   618\t        <div style={{ color: C.accent, fontSize: "9px", letterSpacing: "3px", opacity: 0.8, marginBottom: "4px" }}>\n   619\t          ▸ CAM PRESETS\n   620\t        </div>\n   621\t\n   622\t        {CAMERA_PRESETS.map(preset => (\n   623\t          <button key={preset.name} onClick={() => flyTo(preset)} style={{\n   624\t            padding: "8px 6px", cursor: "pointer",\n   625\t            background: "transparent",\n   626\t            border: `1px solid ${C.dim}`,\n   627\t            color: C.text, fontFamily: "inherit", fontSize: "10px",\n   628\t            letterSpacing: "1.5px", textAlign: "left",\n   629\t            transition: "all 0.15s",\n   630\t          }}\n   631\t            onMouseEnter={e => {\n   632\t              e.currentTarget.style.borderColor = C.accent;\n   633\t              e.currentTarget.style.color = C.accent;\n   634\t              e.currentTarget.style.background = `${C.accent}11`;\n   635\t            }}\n   636\t            onMouseLeave={e => {\n   637\t              e.currentTarget.style.borderColor = C.dim;\n   638\t              e.currentTarget.style.color = C.text;\n   639\t              e.currentTarget.style.background = "transparent";\n   640\t            }}\n   641\t          >\n   642\t            ▶ {preset.name}\n   643\t          </button>\n   644\t        ))}\n   645\t\n   646\t        <div style={{ height: 1, background: C.dim, margin: "4px 0" }} />\n   647\t\n   648\t        <div style={{ color: C.accent, fontSize: "9px", letterSpacing: "3px", opacity: 0.8 }}>\n   649\t          ▸ BANDWIDTH\n   650\t        </div>\n   651\t        <div style={{ display: "flex", alignItems: "flex-end", gap: "1.5px", height: "40px" }}>\n   652\t          {bandwidth.map((v, i) => (\n   653\t            <div key={i} style={{\n   654\t              flex: 1,\n   655\t              background: `linear-gradient(to top, ${C.accent}, ${C.accent}44)`,\n   656\t              height: `${v * 100}%`, transition: "height 0.15s",\n   657\t            }} />\n   658\t          ))}\n   659\t        </div>\n   660\t\n   661\t        <div style={{ height: 1, background: C.dim, margin: "4px 0" }} />\n   662\t\n   663\t        {/* Selected event detail */}\n   664\t        {selectedEvent && (\n   665\t          <div style={{ padding: "8px", border: `1px solid #ff4444`, background: "#ff000011" }}>\n   666\t            <div style={{ color: "#ff6666", fontSize: "9px", letterSpacing: "2px", marginBottom: "6px" }}>\n   667\t              ▸ EVENT DETAIL\n   668\t            </div>\n   669\t            <div style={{ color: "#ff8888", fontSize: "9px", lineHeight: "1.8" }}>\n   670\t              <div>ID: {selectedEvent.id}</div>\n   671\t              <div>MAG: M{selectedEvent.mag}</div>\n   672\t              <div>DEPTH: {selectedEvent.depth} km</div>\n   673\t              <div>LAT: {selectedEvent.lat}°</div>\n   674\t              <div>LNG: {selectedEvent.lng}°</div>\n   675\t              <div style={{ fontSize: "8px", opacity: 0.7, marginTop: 4 }}>{selectedEvent.region}</div>\n   676\t            </div>\n   677\t          </div>\n   678\t        )}\n   679\t\n   680\t        <div style={{ flex: 1 }} />\n   681\t\n   682\t        {/* System info */}\n   683\t        <div style={{ fontSize: "8px", color: C.text, opacity: 0.4, lineHeight: "1.8" }}>\n   684\t          <div>FPS: 60 ▸ STABLE</div>\n   685\t          <div>LATENCY: 42ms</div>\n   686\t          <div>UPTIME: 99.98%</div>\n   687\t          <div>BUILD: 2.4.1-alpha</div>\n   688\t        </div>\n   689\t      </div>\n   690\t\n   691\t      {/* ══════════════ BOTTOM BAR ══════════════ */}\n   692\t      <div style={{\n   693\t        gridColumn: "1 / -1",\n   694\t        ...panelStyle,\n   695\t        borderTop: `2px solid ${C.accent}44`,\n   696\t        display: "flex", alignItems: "center", gap: "16px", padding: "0 16px",\n   697\t        boxShadow: `0 -4px 24px ${C.accent}11`,\n   698\t      }}>\n   699\t        {/* Mini threat board */}\n   700\t        <div style={{ color: C.accent, fontSize: "9px", letterSpacing: "2px", minWidth: 80 }}>THREAT MAP</div>\n   701\t\n   702\t        {EARTHQUAKES.map(eq => (\n   703\t          <div key={eq.id} style={{\n   704\t            display: "flex", alignItems: "center", gap: "4px",\n   705\t            padding: "4px 8px", border: `1px solid ${eq.mag >= 5 ? "#ff2222" : C.dim}`,\n   706\t            background: eq.mag >= 5 ? "#ff000011" : "transparent",\n   707\t            cursor: "pointer",\n   708\t          }} onClick={() => { setSelectedEvent(eq); setRotation({ lat: eq.lat, lng: eq.lng }); setLayers(l => ({ ...l, seismic: true })); }}>\n   709\t            <div style={{\n   710\t              width: 6, height: 6, borderRadius: "50%",\n   711\t              background: eq.mag >= 5.5 ? "#ff2222" : eq.mag >= 5 ? "#ff6622" : "#ff9944",\n   712\t              boxShadow: eq.mag >= 5 ? `0 0 6px #ff2222` : "none",\n   713\t            }} />\n   714\t            <span style={{ color: eq.mag >= 5 ? "#ff8888" : C.text, fontSize: "9px" }}>\n   715\t              M{eq.mag} {eq.region.split(",")[0].toUpperCase()}\n   716\t            </span>\n   717\t          </div>\n   718\t        ))}\n   719\t\n   720\t        <div style={{ flex: 1 }} />\n   721\t\n   722\t        {/* Status indicators */}\n   723\t        <div style={{ display: "flex", gap: "20px", alignItems: "center" }}>\n   724\t          {[\n   725\t            { label: "ALL SYSTEMS", status: "NOMINAL", ok: true },\n   726\t            { label: "DATA FEEDS", status: "LIVE", ok: true },\n   727\t            { label: "ENCRYPTION", status: "AES-256", ok: true },\n   728\t          ].map(s => (\n   729\t            <div key={s.label} style={{ display: "flex", alignItems: "center", gap: "6px" }}>\n   730\t              <div style={{\n   731\t                width: 6, height: 6, borderRadius: "50%",\n   732\t                background: s.ok ? C.accent : "#ff2222",\n   733\t                boxShadow: `0 0 8px ${s.ok ? C.accent : "#ff2222"}`,\n   734\t              }} />\n   735\t              <span style={{ color: C.text, fontSize: "9px", letterSpacing: "1px" }}>\n   736\t                {s.label}: <span style={{ color: C.accent }}>{s.status}</span>\n   737\t              </span>\n   738\t            </div>\n   739\t          ))}\n   740\t        </div>\n   741\t      </div>\n   742\t    </div>\n   743\t  );\n   744\t}\n   745\t', 'uuid': '0808952b-5109-4a6a-abea-58db256d829a'}
Now I'll build a fully functional version — real USGS earthquake API, real OpenSky flight data via CORS proxy, real satellite TLE data, actual country borders rendered via TopoJSON, and live aircraft movement simulation with real heading math.

---

### 🧑 You

give me prompt to make it actually functional

---

### 🤖 Claude

Got it — here's the **exact prompt** you can paste directly into Claude, ChatGPT, Cursor, or any AI coding assistant to build a fully functional WorldView dashboard:

---

## 🧠 Master Build Prompt

```
Build a fully functional React single-file component called WorldView — 
a real-time geospatial intelligence dashboard with a cyberpunk military 
command center aesthetic.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECH STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- React 19 + TypeScript
- D3.js (geoOrthographic projection, geoPath renderer)
- world-atlas TopoJSON for real country borders
  (import from https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json)
- topojson-client to decode borders
- Tailwind CSS 4.0 for layout
- Lucide React for icons
- No backend. All data from public APIs.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REAL DATA SOURCES (implement all four)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. EARTHQUAKES — USGS GeoJSON Feed (no API key needed)
   URL: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson
   - Fetch on mount, refresh every 60 seconds
   - Use: feature.geometry.coordinates [lng, lat, depth]
         feature.properties.mag, .place, .time
   - Render as pulsing red rings, size = magnitude * 2px
   - Show last 24h only, filter mag >= 2.5

2. LIVE FLIGHTS — OpenSky Network REST API (no key needed, rate limited)
   URL: https://opensky-network.org/api/states/all
   - Fetch on mount, refresh every 15 seconds
   - Each state vector: [icao24, callsign, origin_country, 
     time_position, last_contact, longitude, latitude, 
     baro_altitude, on_ground, velocity, true_track, ...]
   - Filter: on_ground === false, lat/lng not null
   - Render blue airplane icons rotated to true_track heading
   - If OpenSky CORS-blocks, fall back to corsproxy.io or allorigins.win wrapper
   - Show max 300 flights for performance

3. SATELLITES — CelesTrak GP data (no key needed)
   URL: https://celestrak.org/SOCRATES/query.php — use this instead:
   URL: https://celestrak.org/SATCAT/records.csv — skip this too
   ACTUAL URL: https://celestrak.org/gp.php?GROUP=stations&FORMAT=json
   Also fetch: https://celestrak.org/gp.php?GROUP=starlink&FORMAT=json
   Also fetch: https://celestrak.org/gp.php?GROUP=gps-ops&FORMAT=json
   - Each record has: OBJECT_NAME, NORAD_CAT_ID, MEAN_MOTION (revs/day),
     INCLINATION, RA_OF_ASC_NODE, ARG_OF_PERICENTER, MEAN_ANOMALY, ECCENTRICITY
   - Propagate current position using simplified SGP4:
       meanMotionRad = MEAN_MOTION * 2π / 86400
       currentMA = MEAN_ANOMALY + meanMotionRad * secondsSinceEpoch
       // For near-circular orbits, true anomaly ≈ mean anomaly
       u = ARG_OF_PERICENTER + currentMA (in radians)
       lat = arcsin(sin(INCLINATION) * sin(u))
       lng = atan2(...) - earthRotation
       earthRotation = (secondsSinceEpoch / 86164) * 360°
   - Update positions every 5 seconds
   - Render as white glowing dots with NORAD ID tooltip on hover

4. WORLD BORDERS — Natural Earth via CDN
   URL: https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json
   - Use topojson.feature() to extract country polygons
   - Render with D3 geoPath + geoOrthographic projection
   - Clip to front hemisphere only (standard for orthographic)
   - Stroke: thin cyan lines, opacity 0.3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GLOBE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Use D3 geoOrthographic projection centered on [centerLng, centerLat]
- Render to SVG element (not Canvas) for crisp UI overlay
- Graticule grid lines every 30° using d3.geoGraticule()
- Country fill: very dark (#040e1c), stroke: cyan at 0.2 opacity
- Auto-rotate: lng += 0.015° per frame via requestAnimationFrame
- Drag to rotate: mousedown/mousemove delta updates [centerLat, centerLng]
- Touch support for mobile drag
- Globe radius: 45% of min(containerWidth, containerHeight)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VISUAL FILTER MODES (toggle in top bar)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Implement three modes using CSS SVG filters applied to the entire globe SVG:

STD (Standard):
  - No filter. Cyan/blue color palette. Normal colors.

NVG (Night Vision):
  - SVG filter: saturate(0) brightness(1.8) sepia(1) hue-rotate(90deg)
  - CSS overlay: mix-blend-mode multiply, green tint rgba(0,255,65,0.15)
  - Add CSS noise texture via ::before pseudo element
  - All accent colors shift to #00ff41

FLIR (Thermal):  
  - SVG filter: saturate(0) contrast(2) brightness(0.8) sepia(1) hue-rotate(330deg)
  - Aircraft and people hotspots render white-hot
  - Cold areas render deep blue
  - Accent colors shift to #ff8800

CRT effect (always on, subtle):
  - CSS repeating-linear-gradient scanlines over entire app, 2px/4px period, 4% opacity
  - Vignette: radial-gradient darkening corners
  - Random flicker: every ~8 seconds, briefly reduce opacity to 0.92 for 80ms

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYOUT (CSS Grid)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
grid-template-columns: 220px 1fr 200px
grid-template-rows: 52px 1fr 100px

[TOP BAR — spans all 3 columns]
  - WorldView logo + version
  - Live UTC Zulu clock (updates every second)
  - Current globe center coordinates (lat/lng)
  - System status pills: RADAR ● SIGINT ● SATLINK ● NETWORK (all green)
  - STD / NVG / FLIR toggle buttons

[LEFT PANEL]
  - "DATA LAYERS" section header
  - Toggle rows for each layer (satellites, flights, military, seismic)
    Each row: colored checkbox + label + live count badge
  - "SIGNAL SPECTRUM" animated bar chart
    32 bars, heights animate smoothly with Math.sin waves + noise
  - "SEISMIC LOG" — scrollable list of last 8 earthquakes
    Shows: mag badge (color-coded), place name, time ago

[CENTER — GLOBE]
  - SVG globe fills available space
  - Corner bracket decorations (pure CSS)
  - Scanning line sweeps top to bottom every 4 seconds
  - Bottom overlay: 3 stat chips (AIRCRAFT n | SATELLITES n | SEISMIC n)
  - Tooltip on hover over any data point (flight callsign, sat name, eq details)

[RIGHT PANEL]
  - "CAM PRESETS" — 8 buttons: Global, New York, London, Tokyo, 
    Dubai, Sydney, Area 51, Bermuda △
    Click animates globe center to that lat/lng over 800ms (lerp)
  - "BANDWIDTH" animated bar chart (24 bars)
  - "ACTIVE ASSET" panel — shows details of last clicked item
    (callsign/NORAD/magnitude, coordinates, altitude/depth, status)
  - System metrics: FPS counter (real), LATENCY 42ms, UPTIME, BUILD

[BOTTOM BAR — spans all 3 columns]
  - Horizontal scrolling seismic threat ticker
  - Each event: colored dot + M{mag} + location name
  - Click any event to fly globe to that location
  - Right side: ALL SYSTEMS NOMINAL | DATA FEEDS LIVE | AES-256

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATA LAYER RENDERING DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FLIGHTS:
  - SVG <polygon> arrow shape, rotated to true_track
  - Commercial: fill #44aaff, size 6px
  - Military (filter by origin_country + callsign patterns like 
    "RCH", "SPAR", "REACH", "IRON", "MOVER", or ICAO starting with "AE"):
    fill #ff7700, size 8px, extra glow ring
  - On hover: show tooltip with callsign, origin_country, altitude, speed
  - Positions update smoothly (lerp between refreshes using velocity*heading)

SATELLITES:
  - SVG <circle> r=2, fill white, opacity 0.85
  - Pulsing ring animation: expanding circle fades out every 2s
  - Color by type: Starlink=cyan, GPS=yellow, Weather=green, Station=white
  - On hover: show NORAD ID, object name, inclination, altitude estimate
  - Update every 5 seconds using propagated position

EARTHQUAKES:
  - SVG concentric rings, number of rings = floor(magnitude)
  - Inner dot: r=3, fill red
  - Outer rings: animate radius 0→mag*8px, opacity 1→0, duration 2s, staggered
  - Color: mag<4=#ff9944, mag<5=#ff6600, mag>=5=#ff2200
  - On hover: show place, magnitude, depth, time ago

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANIMATIONS & PERFORMANCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Single requestAnimationFrame loop drives:
    globe rotation, satellite position updates, flight position lerp,
    scan line sweep, FPS counter
- Throttle D3 path redraws: only recalculate SVG paths when 
  rotation changes by >0.5°
- Use React.memo on Globe SVG, useMemo for projected coordinates
- Cap flights at 300, satellites at 100 for render performance
- CSS transitions for panel interactions (not JS)
- Signal/bandwidth bars use CSS animation keyframes, not JS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ERROR HANDLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- If OpenSky fails/CORS error: 
    fall back to 40 hardcoded realistic flight positions 
    (major routes: JFK-LHR, LAX-NRT, SFO-FRA, DXB-LHR etc.)
    show "SIMULATED" badge on flights layer toggle
- If USGS fails: use 12 hardcoded recent earthquake records
- If CelesTrak fails: use 20 hardcoded TLE-propagated positions
- If TopoJSON fails: show globe with grid only, no borders
- Show last-updated timestamp for each layer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VISUAL DESIGN RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Font: 'JetBrains Mono', monospace — all UI text
Background: #020810 (near black, slight blue tint)
Panel bg: #071426 at 85% opacity (glass morphism)
Panel border: 1px solid #0d2a44, top: 2px solid #00d4ff44
Accent: #00d4ff (cyan)
Text: #7ab8d8 (muted blue)
Bright text: #e0f4ff

All glowing elements use:
  filter: drop-shadow(0 0 4px currentColor)
  or box-shadow: 0 0 12px color

No border-radius > 2px anywhere. Everything is sharp/angular.
No white backgrounds. No rounded cards.
Pure terminal/military aesthetic throughout.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Single .tsx file. All logic self-contained.
No external component libraries except those listed.
Include all TypeScript interfaces/types.
Component must render at 100vw × 100vh.
Export default WorldView.
```

---

## 🔧 Follow-up Prompts (use these if specific parts need fixing)

**If OpenSky flights don't load:**
```
The OpenSky API call is failing with CORS errors. 
Wrap the fetch URL in: https://corsproxy.io/?{encodeURIComponent(url)}
If that also fails, activate the fallback flight array immediately 
and show a "SIMULATED DATA" warning badge on the flights layer.
```

**If D3 globe isn't rendering borders:**
```
The TopoJSON borders aren't rendering. Make sure you're calling:
  topojson.feature(topoData, topoData.objects.countries)
Then pass each feature through d3.geoPath().projection(projection)
to get the SVG path string. Apply geoClipAntimeridian and 
geoClipCircle(90°) for proper hemisphere clipping.
```

**If satellite positions look wrong:**
```
Fix satellite propagation. Use this formula:
  const epoch = new Date(sat.EPOCH).getTime() / 1000
  const now = Date.now() / 1000
  const dt = now - epoch  // seconds since TLE epoch
  const meanMotionRadPerSec = sat.MEAN_MOTION * 2 * Math.PI / 86400
  const ma = (sat.MEAN_ANOMALY * DEG + meanMotionRadPerSec * dt) % (2*Math.PI)
  const u = sat.ARG_OF_PERICENTER * DEG + ma
  const inc = sat.INCLINATION * DEG
  const raan = sat.RA_OF_ASC_NODE * DEG
  const earthRot = (dt / 86164.1) * 2 * Math.PI
  const lat = Math.asin(Math.sin(inc) * Math.sin(u)) / DEG
  const lng = (Math.atan2(
    Math.cos(inc)*Math.sin(u)*Math.cos(raan) - Math.cos(u)*Math.sin(raan),
    Math.cos(inc)*Math.sin(u)*Math.sin(raan) + Math.cos(u)*Math.cos(raan)
  ) - earthRot) / DEG
  return { lat, lng: ((lng + 540) % 360) - 180 }
```

**If performance is bad:**
```
Optimize rendering performance:
1. Move globe SVG paths into a useMemo that only recalculates 
   when rotation changes by more than 0.3 degrees
2. Use CSS transform: rotate() for aircraft icons instead of 
   re-rendering SVG polygons
3. Batch satellite position updates in a web worker
4. Use React.memo on GlobeLayer, FlightLayer, SatelliteLayer, 
   SeismicLayer as separate memoized components
5. Limit rerender frequency to 30fps using a timestamp check 
   in the rAF loop
```

---

Paste the master prompt into **Claude**, **Cursor**, **ChatGPT o3**, or **Windsurf** and it will produce a fully working single-file component. The follow-up prompts handle the most common failure points you'll hit.

---

### 🧑 You

To take WorldView to the next level and make it feel like a truly professional-grade intelligence platform, here are several high-impact features we could implement:
1. 🛰️ Advanced Space Intelligence
Space Debris Tracking: Add a layer for tracked space debris (using CelesTrak's "debris" group) to show the density of objects in Low Earth Orbit.
Satellite Footprints: When you click a satellite, show its "cone of vision" (ground track) projected onto the globe to see what part of the Earth it's currently monitoring.
2. 🚢 Maritime Intelligence (AIS)
Global Shipping: Integrate maritime data to track cargo ships, tankers, and naval vessels. This would complete the "Land, Air, and Sea" intelligence trifecta.
3. ☁️ Real-time Weather & Environment
Cloud Cover Overlay: Use real-time satellite imagery or weather APIs to show current cloud formations over the globe.
Wildfire Tracking: Integrate NASA's FIRMS data to show active thermal hotspots and wildfires globally.
4. 🔊 Immersive Audio Design
Ambient Soundscape: Add a subtle, low-frequency "server room" hum and occasional short-wave radio static.
Interface Feedback: Add "mechanical" click sounds for buttons and "sonar pings" when new seismic events are detected.
5. 📜 Historical Playback (Time Machine)
Event Replay: A slider that allows you to "rewind" the last 24 hours to see how a seismic event unfolded or track the path a specific aircraft took.
6. 📱 Tactical Mobile View
Responsive HUD: A specialized "field agent" layout for mobile devices that prioritizes the most critical alerts and simplifies the globe controls for touch.

---

### 🤖 Claude

Here's your **complete feature expansion prompt pack** — each feature is a self-contained prompt you can paste directly into Claude, Cursor, or any AI coding assistant:

---

## 🛰️ FEATURE 1 — Space Debris + Satellite Footprints

```
Add two features to the existing WorldView satellite layer:

━━━ PART A: SPACE DEBRIS LAYER ━━━
New toggleable layer: "DEBRIS FIELD"

Data source:
  https://celestrak.org/gp.php?GROUP=cosmos-2251-debris&FORMAT=json
  https://celestrak.org/gp.php?GROUP=fengyun-1c-debris&FORMAT=json
  https://celestrak.org/gp.php?GROUP=iridium-33-debris&FORMAT=json
Fetch all three, merge into single debris array. Propagate positions 
using the same SGP4 simplified formula as existing satellites.

Rendering:
- Tiny dots, r=1px, color #ff4444 at 40% opacity
- Density heatmap mode: group debris into 5°×5° lat/lng cells,
  render as colored hex tiles on globe surface:
    0-5 objects: transparent
    5-20: yellow at 20% opacity  
    20-50: orange at 35% opacity
    50+: red at 50% opacity
- Toggle between "dots" and "density" view in layer controls
- Counter badge: "N OBJECTS TRACKED" in the layer toggle row

━━━ PART B: SATELLITE FOOTPRINT ━━━
When user clicks any satellite dot:

1. Calculate ground track (subsatellite point) — already have lat/lng
2. Calculate coverage cone angle:
   Half-angle θ = arccos(Re / (Re + altitude))
   where Re = 6371km, altitude derived from mean_motion:
   altitude = (398600 / (mean_motion * 2π/86400)²)^(1/3) - 6371 (km)
3. Render coverage circle on globe:
   - A geodesic circle of angular radius θ centered on subsatellite point
   - Generate 72 points around the circle using:
       for i in 0..72:
         bearing = i * 5°
         lat2 = arcsin(sin(lat)*cos(θ/Re) + cos(lat)*sin(θ/Re)*cos(bearing))
         lng2 = lng + atan2(sin(bearing)*sin(θ/Re)*cos(lat), cos(θ/Re)-sin(lat)*sin(lat2))
   - Stroke: cyan at 60% opacity, strokeDasharray="4 2"
   - Fill: cyan at 6% opacity
4. Side panel shows:
   - SAT NAME + NORAD ID
   - ALTITUDE: N km
   - COVERAGE AREA: N million km²  
   - COVERAGE RADIUS: N km
   - INCLINATION: N°
   - ORBITAL PERIOD: N min
   - GROUND SPEED: ~7.8 km/s (LEO) or calculated
5. Animate the coverage cone with a slow pulse (scale 0.97 → 1.03 → 0.97)
6. Show orbital ground track: next 1 orbit path as dashed line on globe
```

---

## 🚢 FEATURE 2 — Maritime Intelligence (AIS)

```
Add a MARITIME INTELLIGENCE layer to WorldView.

━━━ DATA SOURCE ━━━
Primary: aisstream.io WebSocket API (free tier, requires free API key)
  wss://stream.aisstream.io/v0/stream
  Send subscription message:
  {
    "APIKey": "{USER_API_KEY}",
    "BoundingBoxes": [[[-90, -180], [90, 180]]],
    "FilterMessageTypes": ["PositionReport"]
  }
  
Fallback (no key needed, REST polling):
  https://www.marinetraffic.com — blocked by CORS, so use:
  Simulated dataset of 80 realistic vessels on major shipping lanes:
  - Strait of Malacca (busy)
  - English Channel (very busy) 
  - Suez Canal approach
  - Panama Canal approach
  - Cape of Good Hope
  - US East Coast corridor
  - Mediterranean
  
Each vessel: { mmsi, name, lat, lng, heading, speed, shipType, flag, destination }

Ship type codes → categories:
  70-79: CARGO (blue-green #00ccaa)
  80-89: TANKER (orange-red #ff6622)
  35-36: MILITARY (bright orange #ff7700, same as military aircraft)
  60-69: PASSENGER (purple #aa66ff)
  30: FISHING (yellow #ffcc00)
  default: OTHER (gray #667788)

━━━ RENDERING ━━━
- SVG ship icon: elongated diamond/hull shape ◇ rotated to heading
  Military vessels: use triangle ▲ like aircraft but slightly wider
- Size by vessel type: tankers bigger (10px), fishing smaller (5px)
- Show wake trail: last 5 positions as fading dashed line
- On hover tooltip: vessel name, flag, type, speed (knots), destination

━━━ LAYER PANEL ━━━
Add to left panel DATA LAYERS section:
  Icon: ⚓  Label: "MARITIME AIS"  Color: #00ccaa
  Sub-badges: "CARGO N | TANKER N | NAVAL N"
  
━━━ CHOKEPOINT ALERTS ━━━
Automatically detect vessel density in known chokepoints:
  Strait of Hormuz (26°N, 56°E, radius 200km)
  Strait of Malacca (2°N, 104°E, radius 300km)
  Suez Canal (30°N, 32.5°E, radius 150km)
  Strait of Gibraltar (36°N, -5.5°E, radius 150km)
  
If >5 vessels in a chokepoint, render a yellow hexagon overlay 
with vessel count. If >15, render orange. If >30, render red.
Label the chokepoint name inside the hex.
Add to bottom threat ticker as: "⚓ MALACCA: 12 VESSELS TRACKED"
```

---

## ☁️ FEATURE 3 — Weather & Wildfire Intelligence

```
Add two environmental intelligence layers to WorldView:

━━━ PART A: WILDFIRE TRACKING (NASA FIRMS) ━━━
Data source (no API key for basic access):
  https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Global_24h.csv
  
Parse CSV columns: latitude, longitude, brightness, scan, track, 
acq_date, acq_time, satellite, confidence, frp (fire radiative power)

Rendering:
- Small flame icons or filled circles
- Color by FRP (fire radiative power):
    frp < 50:   yellow  #ffcc00, r=3px
    frp < 200:  orange  #ff8800, r=5px
    frp >= 200: red     #ff2200, r=7px
- Pulsing animation on high-FRP fires (>200 FRP)
- Flicker effect: random opacity 0.7-1.0 every 200ms to simulate flames
- On hover: show location name (reverse geocode with nominatim if possible,
  else show coordinates), FRP value, satellite, acquisition time

Layer toggle: Icon 🔥 Label "WILDFIRE (FIRMS)" Color #ff8800
Counter badge: "N ACTIVE HOTSPOTS"

━━━ PART B: CLOUD COVER OVERLAY ━━━
Data source: 
  OpenWeatherMap tile layer (free API key required — prompt user to enter it)
  URL pattern: https://tile.openweathermap.org/map/clouds_new/{z}/{x}/{y}.png?appid={KEY}
  
If no API key provided: use NASA Worldview GIBS tiles (no key needed):
  https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/
    MODIS_Terra_CorrectedReflectance_TrueColor/default/
    {YYYY-MM-DD}/250m/{z}/{y}/{x}.jpg
  Use today's date minus 1 day (imagery has ~6hr delay)

Implementation:
- Render weather tiles as a <image> element overlay on the globe SVG
- Apply the geoOrthographic projection to map tile coordinates to SVG space
- Alternatively: render as canvas element composited over SVG globe
- Opacity slider in the layer toggle: 0% to 60% (default 30%)
- Cloud layer should respect day/night terminator if possible:
    Terminator line: calculate solar subsolar point based on UTC time,
    render dark hemisphere overlay at 40% opacity

Layer toggle: Icon ☁ Label "CLOUD COVER" Color #aabbcc
Sub-label shows: "TODAY -1d | MODIS TERRA"
```

---

## 🔊 FEATURE 4 — Immersive Audio Design

```
Add a complete audio system to WorldView using the Web Audio API.
All audio is generated programmatically (no external audio files needed).

━━━ AMBIENT SOUNDSCAPE ━━━
Create on mount, play continuously at low volume (user can mute):

1. Server room hum:
   - OscillatorNode at 60Hz (fundamental)
   - + OscillatorNode at 120Hz (harmonic) at 30% gain
   - + OscillatorNode at 180Hz at 15% gain  
   - Run through BiquadFilterNode (lowpass, freq 200Hz)
   - Master gain: 0.03 (very subtle)

2. Shortwave radio static:
   - AudioBufferSourceNode filled with white noise:
     buffer[i] = Math.random() * 2 - 1
   - Run through BiquadFilterNode (bandpass, freq 800Hz, Q=0.5)
   - Very low gain: 0.01
   - Loop continuously

3. Low drone (tension):
   - OscillatorNode at 40Hz, type "sine"
   - Gain 0.015
   - Slow LFO modulation (0.1Hz) ±5Hz frequency sweep

━━━ UI INTERACTION SOUNDS ━━━
4. Button click (mechanical):
   - Create on each button click
   - OscillatorNode: 800Hz → 400Hz over 40ms (exponential ramp)
   - GainNode: 0.15 → 0 over 40ms
   - Short, snappy, like a relay clicking

5. Layer toggle on:
   - Two-tone beep: 880Hz for 30ms, then 1100Hz for 30ms
   - Gain: 0.1

6. Layer toggle off:
   - Reverse: 1100Hz then 880Hz, slightly lower gain 0.08

7. Camera preset fly-to:
   - Ascending sweep: 400Hz → 800Hz over 200ms
   - Gain envelope: 0 → 0.12 → 0 

8. Panel hover:
   - Very subtle: 2000Hz, 15ms, gain 0.04

━━━ EVENT-TRIGGERED SOUNDS ━━━
9. New earthquake detected (when refresh brings new event):
   - Sonar ping: 1200Hz sine, fast attack (5ms), slow decay (800ms)
   - Gain: 0 → 0.2 → 0 over 800ms
   - Add slight reverb via ConvolverNode (impulse response generated 
     programmatically: decaying noise)

10. High magnitude earthquake (M >= 5.5):
    - Three pings in sequence, 150ms apart
    - Lower frequency: 600Hz
    - Flash the seismic layer icon in the panel

11. New military aircraft detected:
    - Short radar sweep sound: 
      OscillatorNode sweep 200→600Hz over 300ms, sawtooth wave
      Gain: 0.08

━━━ AUDIO CONTROLS ━━━
- Mute/unmute button in top bar (speaker icon, Lucide)
- Master volume slider (0-100%, default 40%)
- Persist mute preference in localStorage
- Fade in audio on first user interaction (autoplay policy compliance):
  Add one-time 'click' event listener on document, then resume AudioContext
  and ramp master gain from 0 to target over 2 seconds

━━━ IMPLEMENTATION NOTES ━━━
- Single AudioContext instance (store in useRef)
- Create AudioContext lazily on first user interaction
- All gain nodes connect through a master GainNode for easy mute
- Use try/catch around all AudioContext calls for browser compatibility
- Offer "AUDIO: ON/OFF" toggle clearly in the UI
```

---

## 📜 FEATURE 5 — Historical Playback (Time Machine)

```
Add a TIME MACHINE playback system to WorldView.

━━━ DATA COLLECTION ━━━
On app load, begin recording a circular buffer of snapshots:
- Every 30 seconds, save a snapshot:
  {
    timestamp: Date.now(),
    earthquakes: [...currentEarthquakes],  // full array
    flights: [...currentFlights],           // positions at this moment
    satellites: [...currentSatellites],     // propagated positions
    vessels: [...currentVessels]            // if maritime enabled
  }
- Keep max 288 snapshots (288 × 30s = 144 minutes / ~2.4 hours)
- Store in useRef (not state, to avoid rerenders)

For earthquakes specifically:
- USGS API supports time ranges: add &starttime= &endtime= params
- Offer to fetch last 24h of quakes on demand:
  https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson
  (already covers 24h, no extra params needed)

━━━ TIME MACHINE UI ━━━
Add a collapsible TIME MACHINE panel at the bottom of the screen
(above the threat ticker). Toggle with a clock icon button.

When expanded, shows:
┌─────────────────────────────────────────────────────────────────┐
│ ⏱ TIME MACHINE          [LIVE]  [◀◀] [◀] [⏸/▶] [▶] [▶▶]     │
│ ████████████████████░░░░░░░░░░░░░░░░░░░░  14:32 UTC  -47 min  │
│ ▲ M5.2 Tokyo  ▲ M4.8 Chile                    ●●●● 12 events  │
└─────────────────────────────────────────────────────────────────┘

Controls:
- Timeline scrubber (input type=range)
  - Range: -144min to 0 (now)
  - Drag to scrub through recorded history
  - Shows timestamp below scrubber
- LIVE button: jump to present, resume live updates
- ◀◀ / ▶▶: jump ±10 minutes
- ◀ / ▶: step ±30 seconds
- ⏸/▶: auto-playback at 30× speed (each frame = 30s of history)

Event markers on timeline:
- Small colored triangles above scrubber for earthquake events
  Red = M5+, orange = M4-5, yellow = M3-4
- Clicking a triangle jumps to that moment and centers globe on event

━━━ PLAYBACK BEHAVIOR ━━━
When NOT at live position:
- Pause all live API polling
- Show "HISTORICAL — {timestamp}" badge replacing LIVE indicators
- Render the snapshot data for the selected timestamp
- Flight positions: interpolate between nearest snapshots
  lat = lerp(snap1.lat, snap2.lat, t)
  Same for lng, heading
- Show "LIVE DATA PAUSED" warning on each layer toggle
- Satellite positions: re-propagate using stored TLE + historical timestamp
- All live pulsing animations continue (they're cosmetic)

When returning to LIVE:
- Smooth transition: fade out historical data, fade in live data over 500ms
- Resume all API polling immediately
- Clear "HISTORICAL" badges

━━━ FLIGHT PATH REPLAY ━━━
When clicking an aircraft during historical playback:
- Show that aircraft's recorded path for the visible time window
- Render as a dashed curved line on the globe (great circle segments)
- Each path point colored by time: older=faded, recent=bright
- Show estimated origin and destination airports if callsign is known
  (use a lookup table of 50 major ICAO callsign → airline mappings)
```

---

## 📱 FEATURE 6 — Tactical Mobile View

```
Add a fully responsive "FIELD AGENT" mobile layout to WorldView.

━━━ BREAKPOINT DETECTION ━━━
const isMobile = window.innerWidth < 768
const isTablet = window.innerWidth >= 768 && window.innerWidth < 1024
Add resize event listener, update state.

━━━ MOBILE LAYOUT (< 768px) ━━━
Replace the 3-column CSS grid with a single-column stack:

[TOP BAR — compressed]
  Height: 44px
  Show: WorldView logo (small), UTC clock, mute button, menu burger
  Remove: coordinate display, system status pills
  Mode toggle: compact 3-button group (STD/NVG/FLIR) right-aligned

[GLOBE — full width, 55vh]
  Globe fills full screen width
  Touch drag: touchstart/touchmove/touchend events for rotation
  Two-finger pinch: zoom level (scale the globe radius)
  Double tap: zoom in on tapped location
  
[ALERT STRIP — horizontal scroll, 8vh]
  One line. Auto-scrolling marquee of active alerts:
  "● M6.1 FIJI  ●● 6,742 AIRCRAFT  ● 183 SATS  ⚠ 3 HIGH-MAG EVENTS"
  Red pulse on new events.

[TAB BAR — bottom, 10vh]
  4 tabs with icons:
  [🌍 MAP] [📡 LAYERS] [⚠ ALERTS] [⚙ SETTINGS]

[MAP TAB]
  Just the globe + alert strip. Full immersion.
  FAB button (floating action): cycle through camera presets

[LAYERS TAB]
  Full-screen panel replacing globe:
  ┌────────────────────────┐
  │ DATA LAYERS            │
  │ ◈ ORBITAL    [ON] 155 │
  │ ✈ COMMERCIAL [ON] 312 │
  │ ◆ MILITARY   [ON]  22 │
  │ ⊕ SEISMIC    [ON]  10 │
  │ ⚓ MARITIME   [OFF]    │
  │ 🔥 WILDFIRE  [OFF]    │
  └────────────────────────┘
  Large touch-friendly toggle switches (48px hit targets)
  Animated signal spectrum bar fills width of screen

[ALERTS TAB]
  Scrollable list of all active events, newest first
  Each alert card:
  ┌──────────────────────────────┐
  │ 🔴 SEISMIC  M6.1             │
  │ Fiji Islands — 560km depth   │
  │ 3 hours ago · -17.7, 178.3   │
  │                    [FLY TO ▶]│
  └──────────────────────────────┘
  Color coded left border: red=seismic, blue=flights, orange=military
  "FLY TO" button switches to MAP tab and animates globe to location

[SETTINGS TAB]
  - Audio: ON/OFF toggle + volume slider
  - Visual Mode: STD / NVG / FLIR large buttons  
  - Auto-rotate: ON/OFF
  - Refresh rate: 15s / 30s / 60s
  - Data density: LOW (100 items) / MEDIUM (300) / HIGH (500)
  - API Keys: OpenWeather key input field
  - "ABOUT WORLDVIEW v2.4" section

━━━ TABLET LAYOUT (768-1024px) ━━━
2-column grid:
  Left: Globe (60% width)
  Right: Tabbed panel (40% width) with LAYERS / ALERTS / DETAILS tabs
  Bottom bar: full threat ticker

━━━ TOUCH GESTURES (all screen sizes) ━━━
Implement using Pointer Events API (works mouse + touch + stylus):
- onPointerDown: start drag, record pointerId
- onPointerMove: update rotation (dx, dy → dlat, dlng)
- onPointerUp: end drag
- Inertia: on pointer up, record velocity, continue rotation 
  decaying exponentially: velocity *= 0.95 per frame until < 0.01
- Pinch zoom: track two pointers, distance change → globe scale
  Min scale: 0.6× (zoomed out), Max scale: 4× (zoomed in)
- Double tap: detect two taps within 300ms on same target
  → zoom to 2× centered on tapped coordinates

━━━ PERFORMANCE FOR MOBILE ━━━
- On mobile, automatically cap: flights=100, satellites=50, debris=off
- Reduce rAF target to 30fps on mobile
- Disable CRT scanlines on mobile (too GPU intensive)
- Simplify border rendering: use lower-resolution countries-50m.json
  https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json
  on desktop, countries-110m.json on mobile
- Disable vignette filter on mobile
```

---

## 🔗 Master Integration Prompt

Use this after implementing all features individually:

```
Integrate all WorldView feature modules into a single cohesive app.
Ensure:

1. All layer toggles in left panel include: satellites, flights, 
   military, seismic, maritime, debris, wildfire, clouds — 
   each with its own color, icon, and live count badge

2. The right panel "ACTIVE ASSET" section works for ALL entity types:
   clicking a satellite, flight, vessel, earthquake, or wildfire 
   all populate the same detail panel with type-appropriate fields

3. Audio system triggers on ALL new event types:
   - New wildfire hotspot detected: crackling sound
   - New vessel in chokepoint: sonar ping variant
   - Debris density threshold crossed: warning tone

4. Time Machine works across ALL layers simultaneously:
   Store and replay satellites, flights, vessels, earthquakes,
   wildfires all from the same snapshot buffer

5. Mobile layout includes all layers in the LAYERS tab

6. All API failures degrade gracefully with SIMULATED badges,
   never crashing or showing blank panels

7. Single master useWorldViewData() hook manages all data sources,
   refresh intervals, and the snapshot buffer

8. Performance budget: maintain 60fps on desktop, 30fps on mobile
   with all layers enabled simultaneously
```

---

Each prompt is fully self-contained — implement them one at a time and test before adding the next. Start with **Feature 2 (Maritime)** if you want the biggest visual impact, or **Feature 4 (Audio)** for the most immersive feel immediately.

---
