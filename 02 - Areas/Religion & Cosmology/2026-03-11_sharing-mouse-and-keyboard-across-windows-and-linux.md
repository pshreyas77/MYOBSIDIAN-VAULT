---
title: "Sharing mouse and keyboard across Windows and Linux"
date: 2026-03-11
tags:
  - python
  - sql
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - obsidian
  - job-search
  - history
  - geopolitics
  - stock-market
  - osint
  - research
  - creative
  - finance
  - web-dev
  - game-design
source: claude-export
---

# Sharing mouse and keyboard across Windows and Linux

> **Conversation Overview**

The person (username sunny77, running Feren OS Linux with Cinnamon/X11) sought help sharing a mouse and keyboard from a Windows machine to their Linux system over WiFi without any browser-based solution. Claude explained that software is required and walked through several options: LAN Mouse, Deskflow, Barrier, and Input Leap. The person's physical setup has the mouse and keyboard plugged into Windows, with Linux as the receiving machine.

The session involved extensive troubleshooting across multiple tools. For LAN Mouse v0.10.0, the correct Linux binary was downloaded via `wget` (no AppImage exists for that release), but X11 input capture is not implemented, making it non-functional as a sender on X11. Deskflow (installed as Flatpak `org.deskflow.deskflow`) was attempted next — it briefly worked previously but stopped connecting, with errors cycling between TLS certificate failures and connection timeouts. TLS was disabled on Linux via `~/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf` with `tlsEnabled=false`, but Windows-side TLS status remained unconfirmed. The session ended with a critical discovery: Linux IP is `192.168.29.215` and Windows IP was entered as `192.168.9.1`, but ping showed 100% packet loss, meaning the two machines are on different subnets and cannot communicate. The Windows machine's actual IP on the `192.168.29.x` subnet still needs to be confirmed via `ipconfig` on Windows.

A secondary issue was also addressed: the person's `~/.bashrc` had a syntax error (unclosed single quote on the `tor-check` alias around line 134) caused by previous fix attempts being pasted as literal text into the file. A Python script was used to cleanly replace lines 131–141 with correct OSINT tool aliases and functions. The person also has OSINT tools configured (theHarvester, sherlock, maigret, holehe) with a virtual environment at `~/osint/tools/osint_venv/` and an osint menu script at `~/osint/osint_menu.sh`.

**Date:** 2026-03-11  
**Topics:** [[Python]] · [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[Obsidian]] · [[Job-Search]] · [[History]] · [[Geopolitics]] · [[Stock-Market]] · [[OSINT]] · [[Research]] · [[Creative]] · [[Finance]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

can i connect my mouse and keywoard from my windows system to linux to use on both systems without any app using wifi and browser

---

### 🤖 Claude

{'type': 'knowledge', 'title': 'GitHub - deskflow/deskflow: Share a single keyboard and mouse between multiple computers. · GitHub', 'url': 'https://github.com/deskflow/deskflow', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': "Deskflow is a free and open source keyboard and mouse sharing app. Use the keyboard, mouse, or trackpad of one computer to control nearby computers, and work seamlessly between them.\n\nWe support all major operating systems, including Windows, macOS, Linux, and Unix-like BSD-derived. Windows 10 v1809 or higher is required. macOS 13 or higher is required to use our CI builds for Apple Silicon machines. macOS 12 or higher is required for Intel macs or local builds. Linux requires libei 1.3+ and libportal 0.8+ for the server/client. Additionally, Qt 6.7+ is required for the GUI. Linux users with systems not meeting these requirements should use flatpak in place of a native package. We officially support FreeBSD, and would also like to support: OpenBSD, NetBSD, DragonFly, Solaris. Repology monitors a huge number of package repositories and other sources comparing package versions across them and gathering other information. When you install Deskflow on macOS, you need to allow accessibility access (Privacy & Security) to both the Deskflow app and the deskflow process.\n\nYes! Wayland (the Linux display server protocol aimed to become the successor of the X Window System) is an important platform for us. The libei and libportal libraries enable Wayland support for Deskflow. We would like to give special thanks to Peter Hutterer, who is the author of libei, a major contributor to libportal, and the author of the Wayland implementation in Deskflow. Others such as Olivier Fourdan and Povilas Kanapickas helped with the Wayland implementation. Some features may be unavailable or broken on Wayland. Please see the known Wayland issues. Deskflow was first created as Synergy in 2001 by Chris Schoeneman. Read about the history of the project on our wiki. Synergy sponsors the Deskflow project by contributing code and providing financial support (learn more). Deskflow is made by possible by these contributors.\n\nDeskflow is a free and open source keyboard and mouse sharing app. Use the keyboard, mouse, or trackpad of one computer to control nearby computers, and work seamlessly between them. It's like a software KVM (but without the video). TLS encryption is enabled by default. Wayland is supported. Clipboard sharing is supported. ... Start a new discussion on our GitHub project. ... On Windows, you will need to install the Microsoft Visual C++ Redistributable. Download latest: vc_redist.x64.exe vc_redist.arm64.exe ... For macOS users, the easiest way to install and stay up to date is to use Homebrew with our homebrew-tap. macOS reports unsigned apps as damaged. This occurs because we do not use an Apple certificate for notarization. Clear the quarantine attribute to run the app: xattr -c Deskflow.app · To use Deskflow, download one of our packages, install deskflow (from your package repository), or build it from source.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/deskflow/deskflow', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Synergy - Share one mouse & keyboard across computers', 'url': 'https://symless.com/synergy', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'symless.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=symless.com', 'site_name': 'Synergy'}, 'is_missing': False, 'text': "Synergy works like a software KVM, but without video. Unlike hardware KVM switches, it does not require cables or physical setup, and avoids the lag and reliability issues common when switching between machines.Learn more · Control multiple ...\n\nSynergy works like a software KVM, but without video. Unlike hardware KVM switches, it does not require cables or physical setup, and avoids the lag and reliability issues common when switching between machines.Learn more · Control multiple computers with one mouse and keyboard. It's an idea so simple, you'll wonder how you ever worked across your devices without it.Get Synergy · Have any questions? Learn more about Synergy or get in touch. 🇺🇸 🇬🇧 🇨🇦 Designed in California, USA. Built and maintained in U.K. & Canada. ... Copyright © 2012-2026 Symless. All rights reserved.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://symless.com/synergy', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'ShareMouse Alternatives for Linux: Top 6 Mouse Sharing Utilities | AlternativeTo', 'url': 'https://alternativeto.net/software/sharemouse/?platform=linux', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'alternativeto.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=alternativeto.net', 'site_name': 'AlternativeTo'}, 'is_missing': False, 'text': "ShareMouse is not available for Linux but there are some alternatives that runs on Linux with similar functionality. The best Linux alternative is Barrier, which is both...\n\nSynergy combines your desktop devices together in to one cohesive experience. It's software for sharing your mouse and keyboard between multiple computers on your desk. It works on Windows, macOS and Linux.19 Synergy alternatives ... No file transfer, only basic clipboard sharing (no text formatting, no bitmaps), no profiles, no easy display configuration, no screensaver sync, no lock sync, no pre-login support. Synergy is Paid and ProprietaryShareMouse is Freemium and Proprietary ... Input Leap is software that mimics the functionality of a KVM switch, which historically would allow you to use a single keyboard and mouse to control multiple computers by physically turning a dial on the box to switch the machine you're controlling at any given moment.19 Input Leap alternatives ... Bluetooth Keyboard/Mouse Emulator: across makes a Bluetooth equipped PC or Mac work as a standard Bluetooth keyboard/mouse combo.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://alternativeto.net/software/sharemouse/?platform=linux', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Sharing Keyboard and Mouse across multiple devices | by Jayadeep KM | Medium', 'url': 'https://medium.com/@jayadeepkm/sharing-keyboard-and-mouse-across-multiple-devices-7c934e914592', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'medium.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=medium.com', 'site_name': 'Medium'}, 'is_missing': False, 'text': 'Let me show you how to configure barrier to share keyboard and mouse over wifi. First, make sure your main computer has a static IP. Most likely your router has an option to automatically assign a fixed ip to the computer.\n\nSharing Keyboard and Mouse across multiple devices My personal work setup consists of a Reddragon K552 mechanical keyboard, a Zebronics RGB Mouse and a 2K display. It isn’t much, but I love working …\n\nThis one is really tricky. I’m currently exploring Miraclecast to cast my mac over wifi to Linux machine. I’ll update this article if I find a good solution. For now, I’m just connecting both devices using multiple cables to the same display and just adjust the source in the monitor whenever I switch to the other device.\n\nInitially I thought of buying a KVM switch. But then I found this gem: https://github.com/debauchee/barrier. Let me show you how to configure barrier to share keyboard and mouse over wifi. First, make sure your main computer has a static IP. Most likely your router has an option to automatically assign a fixed ip to the computer. Or you can set a static IP in network connection setttings. Then install Barrier from the above link. You can find the installation steps for Linux, windows and Mac. In my case, it was easy (I’m running Arch linux) ... There is one step you need to do to get it to work :- setup ssl certificates. There is a bug in Barrier installation, so barrier doesn’t set it up by default, so I had to dig around and find a way to do it. Here is the github issue corresponding to the same: https://github.com/debauchee/barrier/issues/231 ...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://medium.com/@jayadeepkm/sharing-keyboard-and-mouse-across-multiple-devices-7c934e914592', 'search_provider': 'anthropic', 'age': 'August 8, 2022'}} {'type': 'knowledge', 'title': 'share mousey keyboardy thingy - Linux Mint Forums', 'url': 'https://forums.linuxmint.com/viewtopic.php?t=358946', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'linuxmint.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=linuxmint.com', 'site_name': 'Linux Mint Forums'}, 'is_missing': False, 'text': "sudo allow 24800 If you start the barrier Server on the machine the mouse and keyboard are connected to (ALL mine are Wireless - and worked) and if the &#x27;client&#x27; machine hangs at &#x27;Starting barrier&#x27;, you probably forgot to allow the port. Under Help in Barrier there is a Show logs option. If the port is closed it will show a timeout message, and the port number. I hope this is of some use to people with a number of computers (often on the floor) and screens on a desk or desks close together where they are sick of swapping from keyboard to keyboard, using the office chair like a skateboard! Last edited by LockBot on Wed Dec 28, 2022 7:16 am, edited 1 time in total. Reason: Topic automatically closed 6 months after creation. New replies are no longer allowed. Current main OS: MInt 21.3 with KDE Plasma 5.27 (using Compiz as WM) - Kernel: 6.5.0-15 on Lenovo m900 Tiny, i5-6400T (intel HD 530 graphics) 16GB RAM.\n\nFirst an apology for the Post Title. The forum doesn't recognise 'Share Mouse and Keyboard' as a legitimate search term. Ok, with that out of the way, Share Mouse and Keyboard probably belongs in Hardware and Periperals. Except that it ALSO belongs in Software! Now, I wrote a post about rediscovering VNC earlier this year, and although it was more about solving a different problem (allowing me to control several computers using one screen without having to switch using the remote and three separate keyboards and mouses) being able to use one mouse and keyboard does make for a less cluttered desk. I was discussing that with someone who visited last week and he pointed out that he more or less 'needs' several monitors - just as I did when I had my businesses, and that the lag in VNC defeated some of its advantages. I was looking for something in the Software Manager in the flatpak section this morning and I saw a program called Barrier.\n\nThe description intrigued me, so I installed it. It appeared that it is possible to control numerous computers with multiple monitors (I think this includes laptops) that share a LAN (and I did test it on Wireless, because that's all I have). It works. Flawlessly so far, except for some glitches if it is used concurrently on VNC ( doesn't like letting go of the mouse sometimes). So this post is just for people who: Have a few networked computers where they have several screens on a desk, each connected to a computer (and maybe a lappy in the mix). And have several mice and keyboards that they have to swap between, of one of those mouse/keyboard hub things that takes up desk space. The App is called Barrier. The description is: Barrier lets you easily share a single mouse and keyboard between multiple computers with different operating systems, each with its own display, without special hardware.\n\nI started using it over a decade ago when I first got into Mint. I had my main machine running my business on windows, and I had another laptop with Linux Mint 9, controlling them both with one set of wireless mouse/keyboard. Pretty cool to watch the cursor go off the left of one laptop, and show up on another. rossdv8 wrote: ⤴Mon Oct 11, 2021 12:14 am Barrier also merges the clipboards of all the systems into one, allowing cut-and-paste between systems. That is a nice bonus feature. Not that I use windows anymore it's cool that it works across different OSes. I remember in the beginning, none of the online instructions I found were quite complete, as a result I had quite a time getting it to work. HA. I even though it was BS software that didn't actually work. Yes, pretty handy software.\n\nsudo allow 24800 If you start the barrier Server on the machine the mouse and keyboard are connected to (ALL mine are Wireless - and worked) and if the 'client' machine hangs at 'Starting barrier', you probably forgot to allow the port. Under Help in Barrier there is a Show logs option. If the port is closed it will show a timeout message, and the port number. I hope this is of some use to people with a number of computers (often on the floor) and screens on a desk or desks close together where they are sick of swapping from keyboard to keyboard, using the office chair like a skateboard! Last edited by LockBot on Wed Dec 28, 2022 7:16 am, edited 1 time in total. Reason: Topic automatically closed 6 months after creation. New replies are no longer allowed. Current main OS: MInt 21.3 with KDE Plasma 5.27 (using Compiz as WM) - Kernel: 6.5.0-15 on Lenovo m900 Tiny, i5-6400T (intel HD 530 graphics) 16GB RAM.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://forums.linuxmint.com/viewtopic.php?t=358946', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Install Input Leap to share Mouse / Keyboard between Linux, Windows & macOS | UbuntuHandbook', 'url': 'https://ubuntuhandbook.org/index.php/2025/03/input-leap-share-mouse-keyboard/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'ubuntuhandbook.org', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=ubuntuhandbook.org', 'site_name': 'UbuntuHandbook'}, 'is_missing': False, 'text': 'It’s Input Leap a free open-source application forked from Barrier, allowing to use single mouse and keyboard to control multiple computers in same local network. Input Leap is a fork of barrier, by barrier’s active maintainers. One of the core Barrier developer has not been active for ...\n\nGot multiple computers/laptops but only one mouse & keyboard? Without buying a KVM switch, here’s a software can do the job sharing them between your computers. It’s Input Leap a free open-source application forked from Barrier, allowing to use single mouse and keyboard to control multiple computers in same local network. Input Leap is a fork of barrier, by barrier’s active maintainers. One of the core Barrier developer has not been active for a few years, and other maintainers do not have enough administrative access to maintain the project. So, the active maintainers of Barrier created the new Input Leap fork. Barrier is considered unmaintained currently, though Input Leap intends to maintain compatibility with older versions of Barrier. Input Leap has been made into many Linux Distributions’ system repositories, including Arch Linux, Fedora, Manjaro, and Solus.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://ubuntuhandbook.org/index.php/2025/03/input-leap-share-mouse-keyboard/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'How to share a single mouse and keyboard between a Windows PC and a Linux PC - Quora', 'url': 'https://www.quora.com/How-do-I-share-a-single-mouse-and-keyboard-between-a-Windows-PC-and-a-Linux-PC', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'quora.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=quora.com', 'site_name': 'Quora'}, 'is_missing': False, 'text': 'Answer (1 of 3): I just bought myself a Royal Kludge keyboard… three devices, via USB dongle/Bluetooth and you can add another Wired. Press 1. and it works with my Linux HTPC via USB wireless dongle. Press 2. and it works with my phone, saving me picking up the phone (so much effort) Press 3 a...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.quora.com/How-do-I-share-a-single-mouse-and-keyboard-between-a-Windows-PC-and-a-Linux-PC', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'How to share a mouse and keyboard across multiple computers | Opensource.com', 'url': 'https://opensource.com/life/16/10/synchrony', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'opensource.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=opensource.com', 'site_name': 'Opensource.com'}, 'is_missing': False, 'text': 'How do you share your mouse, keyboard, and monitor between several physical systems? Learn about Synergy, an open source software alternative for a physical KVM switch.\n\nEventually, I stopped using the KVM switch, and ended up with a mess of keyboards and mice strewn all over my desk. It was at this point, well over ten years ago now, that I discovered Synergy, an open source software replacement for a physical KVM switch. Back then it did not have any kind of graphical interface to configure your desktops, but it did have a simple text configuration file for the server where you expressed where each monitor was in relation to the others. I always used a simple layout, such as the one shown above, to share my keyboard and mouse. Each machine gets its own monitor(s), and the client machines connect to the server (which has the keyboard and mouse physically attached) to receive events. The interface in the screenshot above (taken on a Linux system) is all new, and it enables you to graphically layout your screens using a friendly Qt-based interface.\n\nFor me the graphical interface has some layout issues. I work on a 4k monitor under Linux and the initial view is quite squashed (see above), but that is easily fixed by resizing. The server configuration dialogs all work well, with an intuitive and well-thought-out layout. I think Synergy is the best software available for anyone who would like to run multiple physical machines that have their own monitors and share a mouse and keyboard. It has been for quite some time, and it has seen a number of improvements in the last few years. There is a great deal of value in cross-platform development in seeing your application as it performs natively on different operating systems, and on different hardware. The Pro version includes SSL support, but I have always used Synergy on a private switch between those systems and never really worried about it too much.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://opensource.com/life/16/10/synchrony', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Cursr - Share Mouse and Keyboard Across Computers. Customize Movement Between Displays', 'url': 'https://cursr.app/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'cursr.app', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=cursr.app', 'site_name': 'Cursr'}, 'is_missing': False, 'text': 'Share your mouse, keyboard and clipboard between computers. Create custom links between display borders for seamless transitions across different resolutions and display gaps. A solution for every multi-display and device setup. Available on Windows, macOS and Linux.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://cursr.app/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'GitHub - feschber/lan-mouse: mouse & keyboard sharing via LAN · GitHub', 'url': 'https://github.com/feschber/lan-mouse', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': '# example configuration # configure release bind release_bind = [ &quot;KeyA&quot;, &quot;KeyS&quot;, &quot;KeyD&quot;, &quot;KeyF&quot; ] # optional port (defaults to 4242) port = 4242 # list of authorized tls certificate fingerprints that # are accepted for incoming traffic [authorized_fingerprints] &quot;bc:05:ab:7a:a4:de:88:8c:2f:92:ac:bc:b8:49:b8:24:0d:44:b3:e6:a4:ef:d7:0b:6c:69:6d:77:53:0b:14:80&quot; = &quot;iridium&quot; # define a client on the right side with host name &quot;iridium&quot; [[clients]] # position (left | right | top | bottom) position = &quot;right&quot; # hostname hostname = &quot;iridium&quot; # activate this client immediately when lan-mouse is started activate_on_startup = true # optional list of (known) ip addresses ips = [&quot;192.168.178.156&quot;] # define a client on the left side with IP address 192.168.178.189 [[clients]] position = &quot;left&quot; # The hostname is optional: When no hostname is specified, # at least one ip address needs to be specified. hostname = &quot;thorium&quot; # ips for ethernet and wifi ips = [&quot;192.168.178.189&quot;, &quot;192.168.178.172&quot;] # optiona\n\nLan Mouse is a cross-platform mouse and keyboard sharing software similar to universal-control on Apple devices. It allows for using multiple PCs via a single set of mouse and keyboard. This is also known as a Software KVM switch. Goal of this project is to be an open-source alternative to proprietary tools like Synergy 2/3, Share Mouse and other open source tools like Deskflow or Input Leap (Synergy fork). Focus lies on performance, ease of use and a maintainable implementation that can be expanded to support additional backends for e.g. Android, iOS, ... in the future. ... Lan Mouse encrypts all network traffic using the DTLS implementation provided by WebRTC.rs. There are currently no mitigations in place for timing side-channel attacks. Most current desktop environments and operating systems are fully supported, this includes ... X11 currently only has support for input emulation, i.e.\n\nPrecompiled release binaries for Windows, MacOS and Linux are available in the releases section. For Windows, the depenedencies are included in the .zip file, for other operating systems see Installing Dependencies. Alternatively, the lan-mouse binary can be compiled from source (see below).\n\n# example configuration # configure release bind release_bind = [ "KeyA", "KeyS", "KeyD", "KeyF" ] # optional port (defaults to 4242) port = 4242 # list of authorized tls certificate fingerprints that # are accepted for incoming traffic [authorized_fingerprints] "bc:05:ab:7a:a4:de:88:8c:2f:92:ac:bc:b8:49:b8:24:0d:44:b3:e6:a4:ef:d7:0b:6c:69:6d:77:53:0b:14:80" = "iridium" # define a client on the right side with host name "iridium" [[clients]] # position (left | right | top | bottom) position = "right" # hostname hostname = "iridium" # activate this client immediately when lan-mouse is started activate_on_startup = true # optional list of (known) ip addresses ips = ["192.168.178.156"] # define a client on the left side with IP address 192.168.178.189 [[clients]] position = "left" # The hostname is optional: When no hostname is specified, # at least one ip address needs to be specified. hostname = "thorium" # ips for ethernet and wifi ips = ["192.168.178.189", "192.168.178.172"] # optiona', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/feschber/lan-mouse', 'search_provider': 'anthropic'}}
Unfortunately, there's **no way to do this without any app at all** — sharing input devices over WiFi requires software on both machines to relay the signals. There's no browser-based or zero-install solution for this.

That said, here are your best options, all **free and open-source**:

---

### ✅ Best Options (Software KVM over WiFi)

**1. Input Leap** *(recommended)*
Input Leap is a free open-source app forked from Barrier, allowing you to use a single mouse and keyboard to control multiple computers on the same local network. It works great on Windows + Linux together.

**2. Deskflow** *(newer, actively maintained)*
Deskflow is a free and open-source keyboard and mouse sharing app that supports all major OSes including Windows and Linux. It includes TLS encryption by default, Wayland support, and clipboard sharing.

**3. LAN Mouse** *(lightweight alternative)*
LAN Mouse is a cross-platform mouse and keyboard sharing software focused on performance and ease of use, with encrypted network traffic via DTLS.

---

### How it works (for all of them)
- Both PCs must be on the **same WiFi network**
- You install the app on **both** Windows and Linux
- One machine is the **server** (where keyboard/mouse is physically plugged in)
- The other is the **client** — your cursor slides from one screen to the other like magic
- Clipboard sharing is also usually included

---

### My recommendation for you (Feren OS)
Go with **Input Leap** — it's in many Linux distros' repos, so installation is straightforward:

```bash
sudo apt install input-leap   # on Feren OS / Ubuntu-based
```

Then install the Windows version from their GitHub releases and configure both sides with the server IP. That's all it takes.

---

### 🧑 You

lan mouse

---

### 🤖 Claude

{'type': 'knowledge', 'title': 'GitHub - feschber/lan-mouse: mouse & keyboard sharing via LAN · GitHub', 'url': 'https://github.com/feschber/lan-mouse', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Fedora You can install Lan Mouse from the [Terra Repository](https://terra.fyralabs.com). ... First make sure to install the necessary dependencies. Precompiled release binaries for Windows, MacOS and Linux are available in the releases section.\n\nLan Mouse encrypts all network traffic using the DTLS implementation provided by WebRTC.rs. There are currently no mitigations in place for timing side-channel attacks. Most current desktop environments and operating systems are fully supported, this includes ... X11 currently only has support for input emulation, i.e. can only be used on the receiving end. Sway / wlroots: Wlroots based compositors without libei support on the receiving end currently do not handle modifier events on the client side. This results in CTRL / SHIFT / ALT / SUPER keys not working with a sending device that is NOT using the layer-shell backend · Wayfire: If you are using Wayfire, make sure to use a recent version (must be newer than October 23rd) and add shortcuts-inhibit to the list of plugins in your wayfire config! Otherwise input capture will not work. Windows: The mouse cursor will be invisible when sending input to a Windows system if there is no real mouse connected to the machine.\n\nThe following sections detail the emulation and capture backends provided by lan-mouse and their support in desktop environments / operating systems. ... wlroots: This backend makes use of the wlr-virtual-pointer-unstable-v1 and virtual-keyboard-unstable-v1 protocols and is supported by most wlroots based compositors. libei: This backend uses libei and is supported by GNOME >= 45 or KDE Plasma >= 6.1. xdp: This backend uses the freedesktop remote-desktop-portal and is supported on GNOME and Plasma. ... layer-shell: This backend creates a single pixel wide window on the edges of Displays to capture the cursor using the layer-shell protocol.\n\nFedora You can install Lan Mouse from the [Terra Repository](https://terra.fyralabs.com). ... First make sure to install the necessary dependencies. Precompiled release binaries for Windows, MacOS and Linux are available in the releases section. For Windows, the depenedencies are included in the .zip file, for other operating systems see Installing Dependencies. Alternatively, the lan-mouse binary can be compiled from source (see below).\n\nBy default the gtk frontend will open when running lan-mouse. To connect a device you want to control, simply click the Add button and enter the hostname of the device. On the remote device, authorize your local device for incoming traffic using the Authorize button under the "Incoming Connections" section. The fingerprint for authorization can be found under the general section of your local device. It is of the form "aa:bb:cc:..." Authorized devices can be persisted using the configuration file (see Configuration). If the device still can not be entered, make sure you have UDP port 4242 (or the one selected) opened up in your firewall. ... The cli interface can be accessed by passing cli as a commandline argument. Use ... Lan Mouse can be launched in daemon mode to keep it running in the background (e.g. for use in a systemd-service). ... In order to start lan-mouse with a graphical session automatically, the systemd-service can be used: Copy the file to ~/.config/systemd/user/ and e', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/feschber/lan-mouse', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'User Guide | feschber/lan-mouse | DeepWiki', 'url': 'https://deepwiki.com/feschber/lan-mouse/5-user-guide', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'deepwiki.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=deepwiki.com', 'site_name': 'DeepWiki'}, 'is_missing': False, 'text': 'feschber/lan-mouse · Index your code with · DevinEdit WikiShare · Loading... Last indexed: 20 April 2025 (b8063a) Overview · System Architecture · Input Capture System · Input Emulation System · Client Management · Network Communication · Installation Guide · Configuration · User Guide · Developer Guide · Building from Source · Project Structure · CI/CD Pipeline · Platform-Specific Details · Linux Support · Windows Support · macOS Support · Troubleshooting · Menu · Relevant source files · README.md · lan-mouse-gtk/src/lib.rs · lan-mouse-gtk/src/window.rs · nix/hm-module.nix · service/lan-mouse.service · src/config.rs · src/main.rs · src/service.rs · This guide provides comprehensive instructions for using lan-mouse, a cross-platform mouse and keyboard sharing software that functions as a software KVM switch. It covers both the graphical (GTK) and command-line interfaces, configuration options, and common usage scenarios.\n\nfeschber/lan-mouse · Index your code with · DevinEdit WikiShare · Loading... Last indexed: 20 April 2025 (b8063a) Overview · System Architecture · Input Capture System · Input Emulation System · Client Management · Network Communication · Installation Guide · Configuration · User Guide · Developer Guide · Building from Source · Project Structure · CI/CD Pipeline · Platform-Specific Details · Linux Support · Windows Support · macOS Support · Troubleshooting · Menu · Relevant source files · README.md · lan-mouse-gtk/src/lib.rs · lan-mouse-gtk/src/window.rs · nix/hm-module.nix · service/lan-mouse.service · src/config.rs · src/main.rs · src/service.rs · This guide provides comprehensive instructions for using lan-mouse, a cross-platform mouse and keyboard sharing software that functions as a software KVM switch. It covers both the graphical (GTK) and command-line interfaces, configuration options, and common usage scenarios.\n\nlan-mouse can be configured through a TOML file located at $XDG_CONFIG_HOME/lan-mouse/config.toml (typically ~/.config/lan-mouse/config.toml on Linux or %LOCALAPPDATA%\\lan-mouse\\config.toml on Windows). ... When you move your mouse to the edge of the screen in the direction of a configured client, control will automatically transfer to that client. To return control to the source computer, you can: Move the mouse back to the edge of the screen toward the source computer · Press the release key combination (default: Ctrl+Shift+Super+Alt or the custom combination in your config) All network traffic is encrypted using DTLS. The fingerprint authorization system ensures that only approved devices can control your computer. ... You can configure commands to execute when you enter a client by adding an enter_hook in the configuration: This is useful for triggering notifications or custom scripts when you switch between computers.\n\nThis guide provides comprehensive instructions for using lan-mouse, a cross-platform mouse and keyboard sharing software that functions as a software KVM switch. It covers both the graphical (GTK) and command-line interfaces, configuration options, and common usage scenarios. For installation instructions, please refer to the Installation Guide. lan-mouse allows you to use a single mouse and keyboard to control multiple computers connected to the same local network. The software establishes a secure connection between machines and seamlessly transfers input control as you move your cursor across screen boundaries. ... Position: The relative location (left, right, top, bottom) of a destination computer in relation to the source · Capture: The process of detecting when your cursor moves to a screen edge · Emulation: The process of simulating mouse and keyboard input on the destination ·\n\nlan-mouse will try all listed IPs when attempting to connect.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://deepwiki.com/feschber/lan-mouse/5-user-guide', 'search_provider': 'anthropic', 'age': 'April 20, 2025'}} {'type': 'knowledge', 'title': 'Lan Mouse: open source cross-platform mouse and keyboard sharing software - gHacks Tech News', 'url': 'https://www.ghacks.net/2024/01/03/lan-mouse-open-source-cross-platform-mouse-and-keyboard-sharing-software/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'ghacks.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=ghacks.net', 'site_name': 'gHacks Tech News'}, 'is_missing': False, 'text': "Lan Mouse&#x27;s latest version can be downloaded from GitHub. Installation packages for Linux, macOS and Windows as well as the source code are provided there. The application has an interface but it can also be used from the command line.\n\nLan Mouse is an open source program for Windows, Linux and macOs that allows users to control multiple devices using one mouse and keyboard. Development focus is on Linux and the versions of macOS and Windows are somewhat limited at this point in development. The program is written entirely in Rust. Programs like Mouse Without Borders, Stardock's Multiplicity KVM, Input Leap, or ShareMouse offer similar functionality. The programs are either commercial or only available for specific platforms. The core idea of all of these programs is to control multiple devices, e.g. a Windows PC, a macBook and a Linux system, with the mouse and keyboard of one of these devices. Lan Mouse's latest version can be downloaded from GitHub. Installation packages for Linux, macOS and Windows as well as the source code are provided there. The application has an interface but it can also be used from the command line.\n\nThe application needs to run on the main system and all clients. Note that the default port is set to 4242 and that communication over this port may need to be allowed in the firewall before you may use mouse and keyboard across multiple systems. Performance was good during tests between different clients. The app sends all events via UDP without any acknowledgement at the moment for performance purposes. While that ensures a fast performance, there can be events that it discards because of a lack of acknowledgement. The roadmap lists several major improvements. Next to introducing input capture on the systems that don't support it yet, Windows, macOS and x11 for the most part, there will also be IP address switching functionality, Clipboard support and support for encryption for security. ... Lan Mouse is an interesting open source project to control multiple computers with a single mouse and keyboard.\n\nSoftware like TeamViewer or RustDesk has the option of controlling a computer, mouse and all. I think I can envision the program being used in the classroom–either for helping students or for putting an obstacle in their fun and games during study. FireWire said on January 6, 2024 at 10:07 pm Reply · TeamViewer is now bloated Electron garbage. Uninstalled that trash on my pcs. AnyDesk turned into nagware. RustDesk is the only good option nowadays. Apple to Launch AI Smart Glasses With Cameras and Silent Voice Control · Windows 11 Has 4 Powerful Features Most Users Never Turn On (But Should) Anthropic Launches Claude Inside PowerPoint for AI-Powered Slide Creation and Editing ·", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.ghacks.net/2024/01/03/lan-mouse-open-source-cross-platform-mouse-and-keyboard-sharing-software/', 'search_provider': 'anthropic', 'age': 'January 3, 2024'}} {'type': 'knowledge', 'title': 'Releases · feschber/lan-mouse', 'url': 'https://github.com/feschber/lan-mouse/releases', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Canceling the remote input popup no longer leaves lan-mouse in a non functioning state (it now asks again). Please feel free to open an issue if you encounter any bugs. Release lan-mouse version 0.7.0 (Ferdinand Schober) 9a75a76: fix duplicate creating of wl_pointer / wl_keyboard (#92) (Ferdinand Schober) #92 · 9e56c54: make release bind configurable (#95) (Ferdinand Schober) #95 · 9afe7da: Libei Input Capture (#94) (Ferdinand Schober) #94 ... There was an error while loading. Please reload this page. ... There was an error while loading. Please reload this page. ... Incoming request now only check for IP address, which makes it possible to use lan-mouse behind a NAT router · initial dns resolve was not working (Ferdinand Schober) Release lan-mouse version 0.6.0 (Ferdinand Schober) b598087: Modified .desktop file to conform with standard (#72) (CupricReki) #72 ·\n\nCanceling the remote input popup no longer leaves lan-mouse in a non functioning state (it now asks again). Please feel free to open an issue if you encounter any bugs. Release lan-mouse version 0.7.0 (Ferdinand Schober) 9a75a76: fix duplicate creating of wl_pointer / wl_keyboard (#92) (Ferdinand Schober) #92 · 9e56c54: make release bind configurable (#95) (Ferdinand Schober) #95 · 9afe7da: Libei Input Capture (#94) (Ferdinand Schober) #94 ... There was an error while loading. Please reload this page. ... There was an error while loading. Please reload this page. ... Incoming request now only check for IP address, which makes it possible to use lan-mouse behind a NAT router · initial dns resolve was not working (Ferdinand Schober) Release lan-mouse version 0.6.0 (Ferdinand Schober) b598087: Modified .desktop file to conform with standard (#72) (CupricReki) #72 ·\n\nYou signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. ... There was an error while loading. Please reload this page. ... This commit was created on GitHub.com and signed with GitHub’s verified signature. ... Learn about vigilant mode. ... There was an error while loading. Please reload this page. ... There was an error while loading. Please reload this page. ... There was an error while loading. Please reload this page. ... I had to re-release, sorry about that. For some reason the release job did not want to release :( ... There was an error while loading. Please reload this page. ... There was an error while loading. Please reload this page. ... There was an error while loading.\n\n4561c20: layer-shell: recreate windows, when output is removed / added (#62) (Ferdinand Schober) #62 ... There was an error while loading. Please reload this page. ... There was an error while loading. Please reload this page. ... There was an error while loading. Please reload this page.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/feschber/lan-mouse/releases', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Share Mouse and Keyboard Across Devices with Lan Mouse – Open Source Software for Windows, Linux & macOS - Tech Edu Byte', 'url': 'https://www.techedubyte.com/share-mouse-keyboard-across-devices-lan-mouse-open-source/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'techedubyte.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=techedubyte.com', 'site_name': 'Tech Edu Byte'}, 'is_missing': False, 'text': 'Getting started with Lan Mouse is straightforward. Follow these steps to install and configure it on your devices: Download the latest release from the official GitHub repository. Run the installer and follow the on-screen instructions.\n\nLan Mouse is designed to work across Windows, Linux, and macOS, making it a versatile tool for anyone looking to streamline their workflow. In this article, we’ll explore how Lan Mouse works, its key features, installation steps, and why it’s becoming a favorite among users seeking a lightweight, secure, and platform-agnostic solution. Lan Mouse is a free, open source application that allows you to control multiple computers using a single mouse and keyboard. Unlike commercial alternatives such as Synergy or Barrier, Lan Mouse focuses on simplicity, security, and cross-platform compatibility. It operates entirely over your local area network (LAN), meaning no internet connection is required, and your data stays private. The software is particularly useful for: – Developers working across different operating systems – Users with multi-monitor setups spanning multiple machines – Anyone looking to reduce desk clutter by eliminating extra peripherals ·\n\nGetting started with Lan Mouse is straightforward. Follow these steps to install and configure it on your devices: Download the latest release from the official GitHub repository. Run the installer and follow the on-screen instructions. Launch the application and configure it as either a server or client. Clone the repository or download the source code. Install dependencies (usually Python and required libraries). Run the setup script or execute the main program directly. Configure server/client settings as needed. Download the macOS package from the releases page. Open the .dmg file and drag the app to your Applications folder. Launch Lan Mouse and set up your network configuration. Ensure all devices are on the same subnet. Configure firewall settings to allow Lan Mouse traffic. Use a static IP for the server to avoid reconnection issues. Switching to Lan Mouse offers several advantages over traditional multi-computer setups: By eliminating the need to switch between keyboards and m\n\nLan Mouse stands out due to its robust feature set and ease of use. Here are some of its most notable capabilities: One of the biggest advantages of Lan Mouse is its compatibility with Windows, Linux, and macOS. This makes it ideal for mixed-OS environments where other solutions might fall short. Being open source means the code is publicly available for review, ensuring transparency and security. Users can verify that no hidden tracking or malicious code is present. Lan Mouse is designed to be resource-efficient, consuming minimal CPU and memory. This ensures smooth performance even on older hardware. Since Lan Mouse operates over your LAN, your data never leaves your local network. This reduces the risk of interception compared to cloud-based solutions. The software is designed with simplicity in mind. Even users with limited technical knowledge can get it up and running quickly.\n\nSince Lan Mouse is free and open source, you save money compared to commercial alternatives. Local networking means your data stays within your control, reducing exposure to potential breaches. Whether you’re using a mix of operating systems or just want a cleaner workspace, Lan Mouse adapts to your needs. While Lan Mouse is designed to be user-friendly, you might encounter occasional hiccups. Here are some common issues and solutions: Issue: Devices can’t find each other on the network. Solution: Check that all devices are on the same subnet and that firewalls aren’t blocking traffic. Issue: Mouse movement feels sluggish. Solution: Ensure your network is stable and consider using a wired connection for better performance. Issue: The app can’t access certain system resources. Solution: Run the application with appropriate permissions or adjust system settings.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.techedubyte.com/share-mouse-keyboard-across-devices-lan-mouse-open-source/', 'search_provider': 'anthropic', 'age': 'February 8, 2026'}} {'type': 'knowledge', 'title': 'Share Mouse & Keyboard Across Devices with Lan Mouse Open Source Software - Tech Edu Byte', 'url': 'https://www.techedubyte.com/share-mouse-keyboard-lan-mouse-open-source/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'techedubyte.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=techedubyte.com', 'site_name': 'Tech Edu Byte'}, 'is_missing': False, 'text': 'Setting up Lan Mouse open source ... guide: Step 1: Download the Software Visit the official Lan Mouse repository or website to download the appropriate version for your operating system....\n\nWith its active development community and regular updates, Lan Mouse continues to evolve and improve. The software’s open-source nature ensures transparency and gives users confidence in its security and reliability. If you’re tired of juggling multiple keyboards and mice across your devices, give Lan Mouse a try—you might wonder how you ever managed without it. Linux · Migrate from Windows to Linux Mint 22: A User-Friendly Alternative · Linux · Wine 10.0 Released with Better Windows App Support on Linux · Linux · End of 10 Project: Helping Windows 10 Users Extend PC Lifespan After 2025 · Linux · Fix Primary Display Issues on Linux: Set Your Monitor as Default · Linux · Windows-to-Linux Migration Tool in Development for Windows 10 Users · Linux · Linux Mint Cinnamon Gets Redesigned Start Menu and New System Info Tool · Limited Slots Available ·\n\nThe Lan Mouse open source software comes packed with features that make cross-device workflow management effortless: Seamless cursor movement between connected devices without any lag or delay. Clipboard sharing allows you to copy text or files on one machine and paste them on another. Multi-monitor support for setups with several displays on each connected computer. Cross-platform compatibility works with Windows, macOS, and Linux systems. Customizable hotkeys for quick actions like locking the cursor to a specific screen or disconnecting from the network. Password protection ensures only authorized devices can connect to your setup. Setting up Lan Mouse open source software is straightforward, even for users with limited technical experience. Here’s a step-by-step guide: Step 1: Download the Software Visit the official Lan Mouse repository or website to download the appropriate version for your operating system.\n\nIn today’s multi-device world, managing multiple computers can quickly become cumbersome. Switching between keyboards and mice across different systems eats up valuable time and breaks workflow. This is where Lan Mouse open source software steps in as an elegant solution, allowing you to share your mouse and keyboard across devices seamlessly. Lan Mouse is a lightweight, open-source application designed to let you control multiple computers using a single mouse and keyboard setup. Built with simplicity in mind, it works over your local network (LAN), making it perfect for home offices, small businesses, or anyone juggling multiple machines. The software operates on a client-server model where one computer acts as the server (with the physical keyboard and mouse), and other devices connect as clients. Once connected, moving your mouse cursor to the edge of one screen automatically transfers control to the next device—just like having dual monitors but across separate computers.\n\nStep 4: Connect Client Devices On each client computer, open Lan Mouse, enter the server’s IP address and port, and click connect. You may need to enter a password if you’ve set one up. Step 5: Arrange Screen Layout Configure the relative positions of your screens in the software settings to ensure the cursor moves to the correct adjacent device when reaching screen edges. While Lan Mouse open source software is generally reliable, you might encounter occasional hiccups: Connection problems often stem from firewall settings. Ensure Lan Mouse has permission to communicate through your firewall on all devices. Cursor jumping can occur if screen positions aren’t configured correctly. Double-check your screen layout settings. Performance lag might indicate network congestion. Try connecting devices via Ethernet instead of Wi-Fi for more stable performance.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.techedubyte.com/share-mouse-keyboard-lan-mouse-open-source/', 'search_provider': 'anthropic', 'age': '1 month ago'}} {'type': 'knowledge', 'title': 'Download lan-mouse (Lan Mouse)', 'url': 'https://sourceforge.net/projects/lan-mouse.mirror/files/v0.10.0/lan-mouse/download', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'sourceforge.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=sourceforge.net', 'site_name': 'SourceForge'}, 'is_missing': False, 'text': "Lan Mouse is a mouse and keyboard-sharing software similar to universal control on Apple devices. It allows for using multiple PCs with a single set of mouse and keyboard. This is also known as a Software KVM switch. The primary target is Wayland on Linux but Windows MacOS and Linux on Xorg have partial support as well (see below for more details). Focus lies on performance and a clean, manageable implementation that can easily be expanded to support additional backends like e.g. Android, iOS. ... Synergy Core This is the open source core component of Synergy, a keyboard and mouse sharing tool. Control your computers with one mouse and keyboard. Control multiple computers using only one keyboard and mouse. Focus on developing software, designing, gaming and remove time switching between operating systems. Throw away the extra keyboards and spend time where it really matters.\n\nInput Remapper An easy-to-use tool to change the behavior of your input devices. Supports X11, Wayland, combinations, programmable macros, joysticks, wheels, triggers, keys, mouse movements and more. Maps any input to any other input. Downloads: 90 This Week Last Update: 2025-11-01 · See Project · KeymouseGo KeymouseGo is a lightweight, open-source Windows/Mac/Linux automation tool built with Python. It records and replays mouse and keyboard actions—for example, click sequences and typing—allowing repetition of repetitive tasks via scripts or GUI buttons. Downloads: 22 This Week Last Update: 2025-07-14 · See Project · Input Overlay Input‑Overlay is an open-source OBS Studio plugin for Windows and Linux that visualizes keyboard, mouse, and gamepad inputs on screen during livestreams or recordings. It presents inputs as overlay source with configurable presets.\n\nInput Remapper An easy-to-use tool to change the behavior of your input devices. Supports X11, Wayland, combinations, programmable macros, joysticks, wheels, triggers, keys, mouse movements and more. Maps any input to any other input. ... KeymouseGo KeymouseGo is a lightweight, open-source Windows/Mac/Linux automation tool built with Python. It records and replays mouse and keyboard actions—for example, click sequences and typing—allowing repetition of repetitive tasks via scripts or GUI buttons. ... Input Overlay Input‑Overlay is an open-source OBS Studio plugin for Windows and Linux that visualizes keyboard, mouse, and gamepad inputs on screen during livestreams or recordings. It presents inputs as overlay source with configurable presets. ... OnScreen Keyboard Eazykeyboard provides a simple onscreen keyboard that can be used to type with keyboard or mouse into application windows.\n\nGet notified by email when Lan Mouse releases a new version. ... The primary target is Wayland on Linux but Windows and MacOS and Linux on Xorg have partial support as well ... Thanks for helping keep SourceForge clean.\n\nDownloads: 199 This Week Last Update: 2025-07-14 · See Project · OnScreen Keyboard Eazykeyboard provides a simple onscreen keyboard that can be used to type with keyboard or mouse into application windows. Downloads: 6 This Week Last Update: 2016-07-25 · See Project · Top 3 Projects in Hardware · Linux Diagnostic Tools Project's goal is to create better tools for diagnosing Linux systems. Diagnostics include first failure data capture, error log analysis, preventative testing, and system inventory gathering. You can now find Power System specific packages on github. libservicelog : https://github.com/power-ras/libservicelog servicelog : https://github.com/power-ras/servicelog lsvpd : https://github.com/power-ras/lsvpd libvpd : https://github.com/power-ras/libvpd ppc64-diag : https://github.com/power-ras/ppc64-diag sysfsutils is moved to github.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://sourceforge.net/projects/lan-mouse.mirror/files/v0.10.0/lan-mouse/download', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Lan Mouse download | SourceForge.net', 'url': 'https://sourceforge.net/projects/lan-mouse.mirror/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'sourceforge.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=sourceforge.net', 'site_name': 'SourceForge'}, 'is_missing': False, 'text': 'Lan Mouse is a mouse and keyboard-sharing software similar to universal control on Apple devices. It allows for using multiple PCs with a single set of mouse and keyboard. This is also known as a Software KVM switch. The primary target is Wayland on Linux but Windows MacOS and Linux on Xorg have partial support as well (see below for more details). Focus lies on performance and a clean, manageable implementation that can easily be expanded to support additional backends like e.g. Android, iOS. All network traffic is currently unencrypted and sent in plaintext · The primary target is Wayland on Linux but Windows and MacOS and Linux on Xorg have partial support as well ... Enterprise Plus edition delivers sub-second maintenance downtime and 2x read/write performance. Built for critical apps. Cloud SQL Enterprise Plus gives you a 99.99% availability SLA with near-zero downtime maintenance—typically under 10 seconds.\n\nLan Mouse is a mouse and keyboard-sharing software similar to universal control on Apple devices. It allows for using multiple PCs with a single set of mouse and keyboard. This is also known as a Software KVM switch. The primary target is Wayland on Linux but Windows MacOS and Linux on Xorg have partial support as well (see below for more details). Focus lies on performance and a clean, manageable implementation that can easily be expanded to support additional backends like e.g. Android, iOS. All network traffic is currently unencrypted and sent in plaintext · The primary target is Wayland on Linux but Windows and MacOS and Linux on Xorg have partial support as well ... Enterprise Plus edition delivers sub-second maintenance downtime and 2x read/write performance. Built for critical apps. Cloud SQL Enterprise Plus gives you a 99.99% availability SLA with near-zero downtime maintenance—typically under 10 seconds.\n\nEazykeyboard provides a simple onscreen keyboard that can be used to type with keyboard or mouse into application windows. ... Thanks for helping keep SourceForge clean.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://sourceforge.net/projects/lan-mouse.mirror/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'feschber/lan-mouse: mouse & keyboard sharing via LAN | daily.dev', 'url': 'https://app.daily.dev/posts/feschber-lan-mouse-mouse-keyboard-sharing-via-lan-onk53yqwg', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'daily.dev', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=daily.dev', 'site_name': 'Daily.dev'}, 'is_missing': False, 'text': 'Lan Mouse is an open-source mouse and keyboard sharing software with support for multiple operating systems. It aims to be a replacement for proprietary tools like Synergy and Share Mouse, offering performance and expandability. Lan Mouse supports Wayland on Linux, as well as Windows and MacOS. It can be installed on different platforms using the provided instructions. ... Table of contentsOS SupportBuild and RunUsageConfigurationRoadmapProtocolBandwidth considerationsPackets per SecondSecurityWayland support ... Hacker News is a community-driven platform for sharing and discussing technology news, startups, and...\n\nLan Mouse is an open-source mouse and keyboard sharing software with support for multiple operating systems. It aims to be a replacement for proprietary tools like Synergy and Share Mouse, offering performance and expandability. Lan Mouse supports Wayland on Linux, as well as Windows and MacOS. It can be installed on different platforms using the provided instructions. ... Table of contentsOS SupportBuild and RunUsageConfigurationRoadmapProtocolBandwidth considerationsPackets per SecondSecurityWayland support ... Hacker News is a community-driven platform for sharing and discussing technology news, startups, and...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://app.daily.dev/posts/feschber-lan-mouse-mouse-keyboard-sharing-via-lan-onk53yqwg', 'search_provider': 'anthropic', 'age': 'January 2, 2024'}} {'type': 'knowledge', 'title': 'Arch Linux - lan-mouse 0.10.0-1 (x86_64)', 'url': 'https://archlinux.org/packages/extra/x86_64/lan-mouse/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'archlinux.org', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=archlinux.org', 'site_name': 'Arch Linux'}, 'is_missing': False, 'text': 'View the file list for lan-mouse · View the soname list for lan-mouse', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://archlinux.org/packages/extra/x86_64/lan-mouse/', 'search_provider': 'anthropic'}}
Here's a complete setup guide for LAN Mouse between your Windows and Feren OS (Linux) machines:

---

## LAN Mouse Setup — Windows ↔ Linux

### Step 1: Download on both machines

Go to **https://github.com/feschber/lan-mouse/releases** and grab:
- **Windows**: the `.zip` file (dependencies included)
- **Linux (Feren OS)**: the `.AppImage` or binary for your architecture

---

### Step 2: Install on Feren OS

```bash
# Make the AppImage executable
chmod +x lan-mouse-*.AppImage
./lan-mouse-*.AppImage
```

Or if you want a proper install, build from source via Cargo (Rust):
```bash
cargo install lan-mouse
```

---

### Step 3: Open firewall port (UDP 4242)

**On Feren OS:**
```bash
sudo ufw allow 4242/udp
```

**On Windows:** Allow LAN Mouse through Windows Defender Firewall when prompted, or manually add a UDP inbound rule for port 4242.

---

### Step 4: Connect the two machines

By default the GTK frontend opens when you run LAN Mouse. Click **Add**, enter the hostname or IP of the other device, then on the remote device click **Authorize** under "Incoming Connections" to approve it.

To find the IP of your Windows machine: run `ipconfig` in Command Prompt and look for your WiFi IPv4 address.

---

### Step 5: Using it

When you move your mouse to the edge of the screen toward the configured client, control automatically transfers. To return, move the mouse back to that edge, or press the release key combo (default: **Ctrl+Shift+Super+Alt**).

You can also configure the relative position (left, right, top, bottom) of the second machine so the cursor flows naturally between screens.

---

### Things to know for Feren OS specifically

- Feren OS uses **Cinnamon (X11)** by default. X11 currently only supports input **emulation** (receiving end), not capture (sending end). This means if your mouse/keyboard is physically on the **Windows** machine, Feren OS works perfectly as the receiver. If it's on Linux, you may have limitations.
- If a real mouse isn't connected to the Windows machine, the cursor will be invisible there — so keep a mouse plugged into Windows.

---

**Recommended setup:** Plug your mouse & keyboard into Windows → Windows is the **server/sender** → Feren OS is the **client/receiver**. That avoids the X11 capture limitation entirely.

---

### 🧑 You

direct cms to download

---

### 🤖 Claude

Here are the direct download links:

### Windows
👉 **https://github.com/feschber/lan-mouse/releases/latest**

On that page, download:
- `lan-mouse-win32-x64.zip` (most common)
- Extract the ZIP and run `lan-mouse.exe`

---

### Linux (Feren OS)
Open terminal and run this to auto-grab the latest AppImage:

```bash
wget https://github.com/feschber/lan-mouse/releases/latest/download/lan-mouse-x86_64.AppImage
chmod +x lan-mouse-x86_64.AppImage
./lan-mouse-x86_64.AppImage
```

Or just visit the same releases page on your Linux browser and download the `.AppImage` manually.

---

> **Tip:** Both machines must be on the **same WiFi network** before connecting them in the app.

---

### 🧑 You

bash: /home/sunny77/.bashrc: line 134: unexpected EOF while looking for matching `'' bash: /home/sunny77/.bashrc: line 155: syntax error: unexpected end of file ~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12  ❯ wget https://github.com/feschber/lan-mouse/releases/latest/download/lan-mouse-x86_64.AppImage chmod +x lan-mouse-x86_64.AppImage ./lan-mouse-x86_64.AppImage --2026-03-11 22:58:37--  https://github.com/feschber/lan-mouse/releases/latest/download/lan-mouse-x86_64.AppImage Resolving github.com (github.com)... 20.207.73.82 Connecting to github.com (github.com)|20.207.73.82|:443... connected. HTTP request sent, awaiting response... 302 Found Location: https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-x86_64.AppImage [following] --2026-03-11 22:58:37--  https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-x86_64.AppImage Reusing existing connection to github.com:443. HTTP request sent, awaiting response... 404 Not Found 2026-03-11 22:58:38 ERROR 404: Not Found. chmod: cannot access 'lan-mouse-x86_64.AppImage': No such file or directory bash: ./lan-mouse-x86_64.AppImage: No such file or directory ~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12  ❯

---

### 🤖 Claude

The AppImage doesn't exist for v0.10.0. Let me check the actual available files:

{'type': 'knowledge', 'title': 'Releases · feschber/lan-mouse', 'url': 'https://github.com/feschber/lan-mouse/releases', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Assets 6 · Loading · There was an error while loading. Please reload this page. 07 Nov 20:11 · github-actions · v0.10.0 · 4703a4c · Compare · Filter · Loading · There was an error while loading. Please reload this page. View all tags · v0.10.0 Latest · Latest · I had to re-release, sorry about that. For some reason the release job did not want to release :( fix crash due to dropped fd by @feschber in #167 · move refcounting of key presses to input-emulation by @feschber in #169 · track pressed keys in input-capture by @feschber in #170 · cleanup capture task by @feschber in #177 · move lan-mouse protocol to separate crate by @feschber in #178 · use local-channel instead of tokio sync channel by @feschber in #179 · [WIP] MacOS inputcapture by @meck in #131 · produce events in dummy capture-backend by @feschber in #184 · include commit-hash in version by @feschber in #185 ·\n\nAssets 6 · Loading · There was an error while loading. Please reload this page. 07 Nov 20:11 · github-actions · v0.10.0 · 4703a4c · Compare · Filter · Loading · There was an error while loading. Please reload this page. View all tags · v0.10.0 Latest · Latest · I had to re-release, sorry about that. For some reason the release job did not want to release :( fix crash due to dropped fd by @feschber in #167 · move refcounting of key presses to input-emulation by @feschber in #169 · track pressed keys in input-capture by @feschber in #170 · cleanup capture task by @feschber in #177 · move lan-mouse protocol to separate crate by @feschber in #178 · use local-channel instead of tokio sync channel by @feschber in #179 · [WIP] MacOS inputcapture by @meck in #131 · produce events in dummy capture-backend by @feschber in #184 · include commit-hash in version by @feschber in #185 ·\n\nFull Changelog: v0.9.1...v0.10.0 · nbolton, meck, and 5 other contributors · Assets 6 · Loading · There was an error while loading. Please reload this page. 10 people reacted · 30 Jul 10:07 · github-actions · v0.9.1 · 22dc333 · Compare · Filter · Loading · There was an error while loading. Please reload this page. View all tags · v0.9.1 · Input Capture and Emulation will prompt to be reenabled · Fixed issues on Windows · Fixes for Plasma 6.1 · Internal restructuring · Release (Ferdinand Schober) Release (Ferdinand Schober) e1096ae: fix macos build error (Ferdinand Schober) Assets 6 · Loading · There was an error while loading. Please reload this page. 5 people reacted · 17 May 16:13 · github-actions · v0.8.0 · e6d4585 · Compare · Filter · Loading · There was an error while loading. Please reload this page. View all tags ·\n\nRelease lan-mouse version 0.7.0 (Ferdinand Schober) 9a75a76: fix duplicate creating of wl_pointer / wl_keyboard (#92) (Ferdinand Schober) #92 · 9e56c54: make release bind configurable (#95) (Ferdinand Schober) #95 · 9afe7da: Libei Input Capture (#94) (Ferdinand Schober) #94 ... There was an error while loading. Please reload this page. ... There was an error while loading. Please reload this page. ... Incoming request now only check for IP address, which makes it possible to use lan-mouse behind a NAT router · initial dns resolve was not working (Ferdinand Schober) Release lan-mouse version 0.6.0 (Ferdinand Schober) b598087: Modified .desktop file to conform with standard (#72) (CupricReki) #72 · 13597b3: fix app_id + app icon (Ferdinand Schober) 8c276f8: temporary fix for AUR pkg (Ferdinand Schober) 2e52660: fix name of desktop entry (Ferdinand Schober) d90eb0c: Activate on startup (#70) (Ferdinand Schober) #70 ...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/feschber/lan-mouse/releases', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Release v0.10.0 · feschber/lan-mouse', 'url': 'https://github.com/feschber/lan-mouse/releases/tag/v0.10.0', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': "mouse &amp; keyboard sharing via LAN. Contribute to feschber/lan-mouse development by creating an account on GitHub.\n\nI had to re-release, sorry about that. For some reason the release job did not want to release :( What's Changed fix crash due to dropped fd by @feschber in #167 move refcounting of key presses to...\n\nmouse & keyboard sharing via LAN. Contribute to feschber/lan-mouse development by creating an account on GitHub.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/feschber/lan-mouse/releases/tag/v0.10.0', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Download lan-mouse (Lan Mouse)', 'url': 'https://sourceforge.net/projects/lan-mouse.mirror/files/v0.10.0/lan-mouse/download', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'sourceforge.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=sourceforge.net', 'site_name': 'SourceForge'}, 'is_missing': False, 'text': 'Your download will start shortly · Give your IT, operations, and business teams the ability to deliver exceptional services—without the complexity\n\nmouse & keyboard sharing via LAN\n\nFreshservice is an intuitive, AI-powered platform that helps IT, operations, and business teams deliver exceptional service without the usual complexity. Automate repetitive tasks, resolve issues faster, and provide seamless support across the organization. From managing incidents and assets to driving smarter decisions, Freshservice makes it easy to stay efficient and scale with confidence. ... Free diagnostic script reveals configuration issues, error patterns, and security risks. Instant HTML report. Windows Task Scheduler might be hiding critical failures. Download the free JAMS diagnostic tool to uncover problems before they impact production—get a color-coded risk report with clear remediation steps in minutes. ... Stop waiting on engineering. Build production-ready internal tools with AI—on your company data, in your cloud. Retool lets you generate dashboards, admin panels, and workflows directly on your data.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://sourceforge.net/projects/lan-mouse.mirror/files/v0.10.0/lan-mouse/download', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Arch Linux - lan-mouse 0.10.0-1 (x86_64)', 'url': 'https://archlinux.org/packages/extra/x86_64/lan-mouse/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'archlinux.org', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=archlinux.org', 'site_name': 'Arch Linux'}, 'is_missing': False, 'text': 'View the file list for lan-mouse · View the soname list for lan-mouse', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://archlinux.org/packages/extra/x86_64/lan-mouse/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'LAN-MOUSE | PORTABLE LINUX APPS', 'url': 'https://portable-linux-apps.github.io/apps/lan-mouse.html', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.io', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.io', 'site_name': 'PORTABLE LINUX APPS'}, 'is_missing': False, 'text': 'The first AUR-inspired Software Center of all AppImage packages and portable applications for GNU/Linux.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://portable-linux-apps.github.io/apps/lan-mouse.html', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'GitHub - feschber/lan-mouse: mouse & keyboard sharing via LAN · GitHub', 'url': 'https://github.com/feschber/lan-mouse', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'mouse &amp; keyboard sharing via LAN. Contribute to feschber/lan-mouse development by creating an account on GitHub.\n\n# example configuration # configure release bind release_bind = [ "KeyA", "KeyS", "KeyD", "KeyF" ] # optional port (defaults to 4242) port = 4242 # list of authorized tls certificate fingerprints that # are accepted for incoming traffic [authorized_fingerprints] "bc:05:ab:7a:a4:de:88:8c:2f:92:ac:bc:b8:49:b8:24:0d:44:b3:e6:a4:ef:d7:0b:6c:69:6d:77:53:0b:14:80" = "iridium" # define a client on the right side with host name "iridium" [[clients]] # position (left | right | top | bottom) position = "right" # hostname hostname = "iridium" # activate this client immediately when lan-mouse is started activate_on_startup = true # optional list of (known) ip addresses ips = ["192.168.178.156"] # define a client on the left side with IP address 192.168.178.189 [[clients]] position = "left" # The hostname is optional: When no hostname is specified, # at least one ip address needs to be specified.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/feschber/lan-mouse', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'AM/programs/x86_64/lan-mouse at main · ivan-hc/AM', 'url': 'https://github.com/ivan-hc/AM/blob/main/programs/x86_64/lan-mouse', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'AppImage Package Manager: AppImage sandboxing, local and system installation, update all AppImages, an extensible database of AppImages and portable apps, lists for AppImages and other GNU/Linux binaries, integrate AppImages by drag/drop or install unlisted AppImages, conversion of old AppImage types... and more! Manage AppImages like never before! - AM/programs/x86_64/lan-mouse at main · ivan-hc/AM\n\nAppImage Package Manager: AppImage sandboxing, local and system installation, update all AppImages, an extensible database of AppImages and portable apps, lists for AppImages and other GNU/Linux binaries, integrate AppImages by drag/drop or install unlisted AppImages, conversion of old AppImage types... and more! Manage AppImages like never before! - AM/programs/x86_64/lan-mouse at main · ivan-hc/AM', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/ivan-hc/AM/blob/main/programs/x86_64/lan-mouse', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Releases · TheAssassin/AppImageLauncher', 'url': 'https://github.com/TheAssassin/AppImageLauncher/releases', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Helper application for Linux distributions serving as a kind of &quot;entry point&quot; for running and integrating AppImages - Releases · TheAssassin/AppImageLauncher\n\nHelper application for Linux distributions serving as a kind of "entry point" for running and integrating AppImages - TheAssassin/AppImageLauncher', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/TheAssassin/AppImageLauncher/releases', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Releases · 0ad-matters/0ad-appimage', 'url': 'https://github.com/0ad-matters/0ad-appimage/releases', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'If it&#x27;s not available from your distro, you can download the tool as an AppImage from the repo (linked above) or by using AM, a command line AppImage package manager. ... There was an error while loading.\n\nThe AppImage is updateable with appimageupdatetool. If it\'s not available from your distro, you can download the tool as an AppImage from the repo (linked above) or by using AM, a command line AppImage package manager. ... There was an error while loading. Please reload this page. ... This commit was created on GitHub.com and signed with GitHub’s verified signature. ... Learn about vigilant mode. ... There was an error while loading. Please reload this page. ... Update for 0.27.0; Use linuxdeploy container (#26) * Use linuxdeploy action * update, remove files no longer needed * Rename script * make-appimage.sh: replace tabs with spaces * Update for 0.27.0, add docker-compose.yml * update docs ... There was an error while loading. Please reload this page. ... This commit was signed with the committer’s verified signature. ... Learn about vigilant mode.\n\nYou can download either the "focal" or "jammy" AppImage (the codename is part of the AppImage filename). If you have a GPU that has a chipset other than Nvidia, the Vulkan backend may be automatically disabled in some cases. If that happens to you, and you downloaded the "focal" image, try the "jammy" image (note the "jammy" image is less likely to work on older distros, but the vulkan backend is more likely to work). More info about this release at https://wildfiregames.com/forum/topic/107313-alpha-27-pre-releaserelease-candidate-build-testing ... There was an error while loading. Please reload this page. ... This commit was created on GitHub.com and signed with GitHub’s verified signature. The key has expired. ... Learn about vigilant mode. ... There was an error while loading. Please reload this page. ... https://www.reddit.com/r/0ad/comments/10aocep/the_next_alpha_of_0_ad_will_feature_an/?utm_source=share&utm_medium=web2x&context=3 ...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/0ad-matters/0ad-appimage/releases', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Lan Mouse download | SourceForge.net', 'url': 'https://sourceforge.net/projects/lan-mouse.mirror/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'sourceforge.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=sourceforge.net', 'site_name': 'SourceForge'}, 'is_missing': False, 'text': 'Download Lan Mouse for free. mouse &amp; keyboard sharing via LAN. Lan Mouse is a mouse and keyboard-sharing software similar to universal control on Apple devices. It allows for using multiple PCs with a single set of mouse and keyboard.\n\nJDisc Discovery is a comprehensive network inventory and IT asset management solution designed to help organizations gain clear, up-to-date visibility into their IT environment. It automatically scans and maps devices across the network, including servers, workstations, virtual machines, and... ... Eazykeyboard provides a simple onscreen keyboard that can be used to type with keyboard or mouse into application windows. ... Thanks for helping keep SourceForge clean.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://sourceforge.net/projects/lan-mouse.mirror/', 'search_provider': 'anthropic'}}
The v0.10.0 release doesn't include an AppImage — only a binary. Here's the correct command:

```bash
wget https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-x86_64-unknown-linux-gnu.tar.gz
tar -xzf lan-mouse-x86_64-unknown-linux-gnu.tar.gz
chmod +x lan-mouse
./lan-mouse
```

If that filename also 404s, check the exact available files first:

```bash
curl -s https://api.github.com/repos/feschber/lan-mouse/releases/latest | grep "browser_download_url" | awk -F'"' '{print $4}'
```

That will list **all actual download links** for the latest release so you can pick the right one.

Also, your `.bashrc` has a syntax error (unclosed quote on line 134) — that's unrelated to LAN Mouse but worth fixing. Run this to see the problematic line:

```bash
sed -n '130,140p' ~/.bashrc
```

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12  ❯ wget https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-x86_64-unknown-linux-gnu.tar.gz tar -xzf lan-mouse-x86_64-unknown-linux-gnu.tar.gz chmod +x lan-mouse ./lan-mouse --2026-03-11 22:59:28--  https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-x86_64-unknown-linux-gnu.tar.gz Resolving github.com (github.com)... 20.207.73.82 Connecting to github.com (github.com)|20.207.73.82|:443... connected. HTTP request sent, awaiting response... 404 Not Found 2026-03-11 22:59:29 ERROR 404: Not Found. tar (child): lan-mouse-x86_64-unknown-linux-gnu.tar.gz: Cannot open: No such file or directory tar (child): Error is not recoverable: exiting now tar: Child returned status 2 tar: Error is not recoverable: exiting now chmod: cannot access 'lan-mouse': No such file or directory bash: ./lan-mouse: No such file or directory ~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12  ❯ curl -s https://api.github.com/repos/feschber/lan-mouse/releases/latest | grep "browser_download_url" | awk -F'"' '{print $4}' https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-macos-aarch64 https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-macos-intel https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-windows.zip ~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12  ❯ sed -n '130,140p' ~/.bashrc # OSINT Tool Aliases alias osint-env='source ~/osint/tools/osint_venv/bin/activate' alias tor-check='curl -s https://check.torproject.org/ | grep -o "Congratulations" alias pchain='proxychains4' # Tool Runners function run-harvester { source ~/osint/tools/osint_venv/bin/activate && theHarvester "$@"; deactivate; } function run-sherlock { source ~/osint/tools/osint_venv/bin/activate && sherlock "$@"; deactivate; } function run-maigret { source ~/osint/tools/osint_venv/bin/activate && maigret "$@"; deactivate; } function run-holehe { source ~/osint/tools/osint_venv/bin/activate && holehe "$@"; deactivate; } ~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12  ❯ wget https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-x86_64-unknown-linux-gnu.tar.gz tar -xzf lan-mouse-x86_64-unknown-linux-gnu.tar.gz chmod +x lan-mouse ./lan-mouse --2026-03-11 22:59:52--  https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-x86_64-unknown-linux-gnu.tar.gz Resolving github.com (github.com)... 20.207.73.82 Connecting to github.com (github.com)|20.207.73.82|:443... connected. HTTP request sent, awaiting response... 404 Not Found 2026-03-11 22:59:52 ERROR 404: Not Found. tar (child): lan-mouse-x86_64-unknown-linux-gnu.tar.gz: Cannot open: No such file or directory tar (child): Error is not recoverable: exiting now tar: Child returned status 2 tar: Error is not recoverable: exiting now chmod: cannot access 'lan-mouse': No such file or directory bash: ./lan-mouse: No such file or directory ~ on  main [⇡] is  v1.0.0 via 寧 via  v3.10.12  ❯

---

### 🤖 Claude

The curl output already showed the answer. The Linux binary is just called `lan-mouse` (no extension). Run:

```bash
wget https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse
chmod +x lan-mouse
./lan-mouse
```

---

Also, your `.bashrc` error is on the `tor-check` alias — missing a closing single quote. Fix it:

```bash
nano ~/.bashrc
```

Find this line (~134):
```bash
alias tor-check='curl -s https://check.torproject.org/ | grep -o "Congratulations"
```

Change it to:
```bash
alias tor-check='curl -s https://check.torproject.org/ | grep -o "Congratulations"'
```

Then:
```bash
source ~/.bashrc
```

---

### 🤖 Claude

Two issues to fix:

---

### 1. Fix the missing `libadwaita` library

```bash
sudo apt install libadwaita-1-0
```

Then run it again:
```bash
./lan-mouse
```

---

### 2. Fix the `.bashrc` syntax error

The `tor-check` alias is still broken. Run:

```bash
sed -n '133,135p' ~/.bashrc
```

You'll see the unclosed quote. Fix it directly with sed (no nano needed):

```bash
sed -i "s/alias tor-check='curl -s https:\/\/check.torproject.org\/ | grep -o \"Congratulations\"/alias tor-check='curl -s https:\/\/check.torproject.org\/ | grep -o \"Congratulations\"'/" ~/.bashrc
```

Or the safer manual way — open nano, go to line 134:
```bash
nano +134 ~/.bashrc
```

Find this:
```
alias tor-check='curl -s https://check.torproject.org/ | grep -o "Congratulations"
```

Add the missing `'` at the end:
```
alias tor-check='curl -s https://check.torproject.org/ | grep -o "Congratulations"'
```

Save with **Ctrl+O → Enter → Ctrl+X**, then:
```bash
source ~/.bashrc
```

---

### 🤖 Claude

LAN Mouse is running! The GUI should have opened. The warnings are harmless — it's using X11 emulation which is fine for receiving input from Windows.

Now fix the `.bashrc` — use nano directly:

```bash
nano +134 ~/.bashrc
```

Find this line (should be around line 134):
```
alias tor-check='curl -s https://check.torproject.org/ | grep -o "Congratulations"
```

Add `'` at the very end so it becomes:
```
alias tor-check='curl -s https://check.torproject.org/ | grep -o "Congratulations"'
```

Save: **Ctrl+O → Enter → Ctrl+X**

```bash
source ~/.bashrc
```

---

### Back to LAN Mouse — next steps

Did the GUI window open on your screen? If yes:

1. On **Windows**, download and run `lan-mouse-windows.zip` from the releases page
2. In the LAN Mouse GUI on Linux, note your machine's IP (`hostname -I`)
3. On Windows side, add your Linux IP as a client
4. Set Linux to the **right or left** of Windows depending on your monitor layout

---

### 🧑 You

GNU nano 6.2                                             /home/sunny77/.bashrc *                                                     # some more ls aliases alias ll='ls -alF' alias la='ls -A' alias l='ls -CF' # Add an "alert" alias for long running commands.  Use like so: #   sleep 10; alert alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+> # Alias definitions. # You may want to put all your additions into a separate file like # ~/.bash_aliases, instead of adding them here directly. # See /usr/share/doc/bash-doc/examples in the bash-doc package. if [ -f ~/.bash_aliases ]; then    . ~/.bash_aliases fi # enable programmable completion features (you don't need to enable # this, if it's already enabled in /etc/bash.bashrc and /etc/profile # sources /etc/bash.bashrc). if ! shopt -oq posix; then  if [ -f /usr/share/bash-completion/bash_completion ]; then    . /usr/share/bash-completion/bash_completion  elif [ -f /etc/bash_completion ]; then    . /etc/bash_completion  fi fi eval "$(starship init bash)" neofetch export PATH="$HOME/.local/bin:$PATH" # opencode export PATH=/home/sunny77/.opencode/bin:$PATH export NVM_DIR="$HOME/.nvm" [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion alias harvester="~/osint/tools/recon/run_harvester.sh" export PATH="$HOME/.local/bin:$PATH" # OSINT Tool Aliases alias osint-env='source ~/osint/tools/osint_venv/bin/activate' alias tor-check='curl -s https://check.torproject.org/ | grep  -o "Congratulations"'' ```alias pchain='proxychains4' # Tool Runners Find this:function run-harvester { source ~/osint/tools/osint_venv/bin/activate && theHarvester "$@"; deactivate; } function  run-sherlock { source ~/osint/tools/osint_venv/bin/activate && sherlock "$@"; deactivate; } function run-maigret { source  ~/osint/tools/osint_venv/bin/activate && maigret "$@"; deactivate; } function run-holehe { source  ~/osint/tools/osint_venv/bin/activate && holehe "$@"; deactivate; } ``` alias tor-check='curl -s https://check.torproject.org/  | grep -o "Congratulations" ``` osint() { bash ~/osint/osint_menu.sh Add the missing `'` at the end:} ``` osint() { alias tor-check='curl -s  https://check.torproject.org/ | grep -o "Congratulations"' bash ~/osint/osint_menu.sh source ~/.bashrc} # bun export BUN_INSTALL="$HOME/.bun" export PATH="$BUN_INSTALL/bin:$PATH"

---

### 🤖 Claude

Your `.bashrc` is very messy — it looks like previous fix attempts got pasted directly into the file as text! There's a lot of garbage in there. Let me help you clean it up properly.

In nano, you need to delete everything from the `# OSINT Tool Aliases` section downward and replace it cleanly. 

First, let's see the full damage — press **Ctrl+X** to exit nano without saving, then run:

```bash
grep -n "" ~/.bashrc | tail -40
```

Paste the output here and I'll give you the exact lines to delete and the clean replacement block to paste in. That way we fix it once properly instead of making it worse.

---

### 🤖 Claude

Lines 132–142 are completely mangled. Let me fix this with a clean Python script — safer than sed for multi-line edits:

```bash
python3 << 'EOF'
with open('/home/sunny77/.bashrc', 'r') as f:
    lines = f.readlines()

# Replace lines 132-142 (0-indexed: 131-141) with clean content
clean = [
    '\n',
    '# OSINT Tool Aliases\n',
    'alias osint-env=\'source ~/osint/tools/osint_venv/bin/activate\'\n',
    'alias tor-check=\'curl -s https://check.torproject.org/ | grep -o "Congratulations"\'\n',
    'alias pchain=\'proxychains4\'\n',
    '\n',
    '# Tool Runners\n',
    'function run-harvester { source ~/osint/tools/osint_venv/bin/activate && theHarvester "$@"; deactivate; }\n',
    'function run-sherlock { source ~/osint/tools/osint_venv/bin/activate && sherlock "$@"; deactivate; }\n',
    'function run-maigret { source ~/osint/tools/osint_venv/bin/activate && maigret "$@"; deactivate; }\n',
    'function run-holehe { source ~/osint/tools/osint_venv/bin/activate && holehe "$@"; deactivate; }\n',
    '\n',
    'osint() { bash ~/osint/osint_menu.sh; }\n',
    '\n',
]

new_lines = lines[:131] + clean + lines[143:]

with open('/home/sunny77/.bashrc', 'w') as f:
    f.writelines(new_lines)

print("Done! Lines 132-142 replaced cleanly.")
EOF
```

Then verify and reload:

```bash
sed -n '129,148p' ~/.bashrc
source ~/.bashrc
```

---

### 🧑 You

open app

---

### 🤖 Claude

Looking at the logs, LAN Mouse **did open and close** — it ran for ~5 minutes then exited. The issue is **X11 input capture is not implemented**, meaning Linux can only **receive** input, not send it.

To open it again:

```bash
./lan-mouse
```

The GUI window should appear. If it's not showing, it may be opening in the background — check your taskbar.

---

### Important: Your setup must be

**Mouse & Keyboard plugged into Windows** → Windows sends → Linux receives

This is because:
- ✅ Linux X11 = can **receive** input (emulation works)
- ❌ Linux X11 = cannot **capture/send** input (not implemented yet)

So on the **Windows side**, download and run the app:
👉 `https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-windows.zip`

Extract and run `lan-mouse.exe` on Windows — that's where you add Linux as a client and configure the screen layout.

---

### 🧑 You

it is showing like this

---

### 🤖 Claude

LAN Mouse is open and working! Now just connect it to Windows.

### Next steps:

**On your Linux machine — get your IP:**
```bash
hostname -I
```
Note the IP (something like `192.168.1.x`)

---

**On Windows:**
1. Download and extract `lan-mouse-windows.zip` from:
   `https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-windows.zip`
2. Run `lan-mouse.exe`

---

**Back in the Linux LAN Mouse app:**
1. Click **+ Add**
2. Enter your **Windows machine's IP**
3. Set position to **Right** (or wherever Windows screen is relative to Linux)
4. Click **Reenable** to re-enable capture

---

**On Windows LAN Mouse:**
- It will show an incoming connection request from Linux — click **Authorize**

Once both sides are connected, move your mouse to the edge of the Windows screen toward Linux and it will slide over automatically. 🖱️

---

### 🧑 You

in linux it is showing input capture is disable

---

### 🤖 Claude

That's expected and fine! Since you're on **X11** (not Wayland), Linux **cannot capture** input — it can only **receive** it.

This means:
- ✅ Your **mouse & keyboard must be plugged into Windows** (Windows captures and sends)
- ✅ Linux just receives — the "input capture disabled" warning is normal for X11

**You don't need to click Reenable on Linux.** Just leave it as is.

---

### All you need to do now is set up the Windows side:

1. On Windows, download and run:
   `https://github.com/feschber/lan-mouse/releases/download/v0.10.0/lan-mouse-windows.zip`

2. In the **Windows** LAN Mouse app, click **+ Add** and enter your **Linux IP**

3. Run this on Linux to get your IP:
   ```bash
   hostname -I
   ```

4. Set the position (e.g. Linux is to the **Left** of Windows screen)

5. On Windows, click **Reenable** — Windows will capture your mouse and send it to Linux when you move to that edge

That's it. Everything is configured from the **Windows side**.

---

### 🧑 You

in linux it is not working

---

### 🤖 Claude

The issue is clear — **X11 input capture is not implemented** in LAN Mouse. Linux cannot send OR properly receive on your setup.

You have two options:

---

{'type': 'text', 'text': '{\n  "questions": [\n    {\n      "question": "Have you set up the Windows side yet?",\n      "options": [\n        "Yes, Windows app is running",\n        "No, not yet"\n      ],\n      "type": "single_select"\n    },\n    {\n      "question": "What is your physical setup?",\n      "options": [\n        "Mouse & keyboard plugged into Windows",\n        "Mouse & keyboard plugged into Linux",\n        "Separate mouse/keyboard for each"\n      ],\n      "type": "single_select"\n    }\n  ]\n}', 'uuid': '59a90e51-3e68-496c-92a8-4dd898fa9210'}

---

### 🧑 You

Q: Have you set up the Windows side yet?
A: Yes, Windows app is running

Q: What is your physical setup?
A: Mouse & keyboard plugged into Windows

---

### 🤖 Claude

Perfect setup! Now let's connect them.

**On Linux, get your IP:**
```bash
hostname -I
```

Then on **Windows LAN Mouse**:
1. Click **+ Add**
2. Enter the Linux IP (e.g. `192.168.1.x`)
3. Set position to **Left** (if Linux monitor is to the left of Windows)
4. Click **Reenable**

Then move your mouse to the **left edge** of your Windows screen — it should slide over to Linux.

---

**If it still doesn't work**, check firewall on Linux:
```bash
sudo ufw allow 4242/udp
sudo ufw status
```

And make sure both machines are on the **same WiFi network**. What happens when you try — does the cursor just stop at the edge, or anything on the Linux screen?

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ hostname -I 192.168.29.215 2405:201:c400:592d:34a6:8d61:3675:6a14 2405:201:c400:592d:369c:5496:7529:4c5d  ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12

---

### 🤖 Claude

Your Linux IP is **`192.168.29.215`**

---

**On Windows LAN Mouse:**
1. Click **+ Add**
2. Enter: `192.168.29.215`
3. Set position: **Left** or **Right** (wherever your Linux screen is physically)
4. Click **Reenable**

Then slide your mouse to that edge on Windows — it should jump to Linux.

---

Also allow the port on Linux just in case:
```bash
sudo ufw allow 4242/udp
```

Try it and let me know what happens — does the cursor stop at the edge or does anything appear in the Linux LAN Mouse app?

---

### 🧑 You

on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ hostname -I 192.168.29.215 2405:201:c400:592d:34a6:8d61:3675:6a14 2405:201:c400:592d:369c:5496:7529:4c5d  ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ sudo ufw allow 4242/udp [sudo] password for sunny77:  sudo: ufw: command not found ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12 took 2s  ❯ ./lan-mouse [2026-03-11T17:53:00Z WARN  lan_mouse::config] /home/sunny77/.config/lan-mouse/config.toml: No such file or directory (os error 2) [2026-03-11T17:53:00Z WARN  lan_mouse::config] Continuing without config file ... [2026-03-11T17:53:00Z INFO  lan_mouse] release bind: [KeyLeftCtrl, KeyLeftShift, KeyLeftMeta, KeyLeftAlt] [2026-03-11T17:53:00Z WARN  lan_mouse::config] /home/sunny77/.config/lan-mouse/config.toml: No such file or directory (os error 2) [2026-03-11T17:53:00Z WARN  lan_mouse::config] Continuing without config file ... [2026-03-11T17:53:00Z INFO  lan_mouse] release bind: [KeyLeftCtrl, KeyLeftShift, KeyLeftMeta, KeyLeftAlt] [2026-03-11T17:53:00Z INFO  lan_mouse] Press [KeyLeftCtrl, KeyLeftShift, KeyLeftMeta, KeyLeftAlt] to release the mouse [2026-03-11T17:53:00Z INFO  lan_mouse::server::emulation_task] creating input emulation... [2026-03-11T17:53:00Z WARN  input_emulation] wlroots backend: `Could not find wayland compositor` [2026-03-11T17:53:00Z WARN  input_capture] input-capture-portal input capture backend unavailable: error creating input-capture-portalbackend: `xdg-desktop-portal: `A portal frontend implementing `org.freedesktop.portal.InputCapture` was not found`` [2026-03-11T17:53:00Z WARN  input_capture] layer-shell input capture backend unavailable: error creating layer-shell capture backend: `Could not find wayland compositor` [2026-03-11T17:53:00Z WARN  input_capture] X11 input capture backend unavailable: error creating x11 capture backend: `X11 input capture is not yet implemented :(` [2026-03-11T17:53:00Z WARN  lan_mouse::server::capture_task] input capture exited: error creating input-capture: `no backend available` [2026-03-11T17:53:00Z WARN  input_emulation] libei backend: `Portal request didn't succeed: Other` [2026-03-11T17:53:00Z WARN  input_emulation] xdg-desktop-portal: `Portal request didn't succeed: Other` [2026-03-11T17:53:00Z INFO  input_emulation] using emulation backend: X11 (lan-mouse:245030): Gtk-WARNING **: 23:23:00.324: Unknown key gtk-modules in /home/sunny77/.config/gtk-4.0/settings.ini (lan-mouse:245030): Adwaita-WARNING **: 23:23:00.395: Using GtkSettings:gtk-application-prefer-dark-theme with libadwaita is unsupported. Please use AdwStyleManager:color-scheme instead. [2026-03-11T17:53:08Z WARN  lan_mouse::server::emulation_task] ignoring events from client 192.168.29.38:4242 sudo ufw allow 4242/udp

---

### 🤖 Claude

Great news! I can see this line:

```
ignoring events from client 192.168.29.38:4242
```

**Windows is connecting and sending data!** Linux is receiving it but ignoring it because there's no authorized connection set up on the Linux side.

**In the Linux LAN Mouse GUI:**
1. Click **+ Add**
2. Enter Windows IP: **`192.168.29.38`**
3. Set position (Left/Right depending on your screen layout)
4. Click **Save/Add**

That tells Linux to trust and accept input from that Windows machine. Then it should work!

---

### 🤖 Claude

The connection is established (`added client 0` with `192.168.29.38`). The only remaining issue is **X11 input capture not implemented** — this means LAN Mouse v0.10.0 simply **cannot work on X11 Linux as a receiver from Windows** in the current version.

---

### The real fix: Switch to Input Leap instead

Input Leap works perfectly on X11 Linux. Install it:

```bash
sudo apt install input-leap
```

Then:
1. Open **Input Leap** on Linux → set it as **Server**
2. Install Input Leap on Windows → set as **Client**
3. Enter Linux IP (`192.168.29.215`) in the Windows client
4. Done — mouse slides between screens

---

### Why LAN Mouse fails here

LAN Mouse requires **Wayland** on Linux to capture AND emulate input properly. Your Feren OS runs **X11/KDE Plasma**, and the developer hasn't implemented X11 capture yet. Input Leap was built specifically for X11 and works reliably.

Want me to walk you through the Input Leap setup?

---

### 🧑 You

input leap did not work on my system

---

### 🤖 Claude

Let me check what alternatives work on X11:

{'type': 'knowledge', 'title': 'Install Input Leap to share Mouse / Keyboard between Linux, Windows & macOS | UbuntuHandbook', 'url': 'https://ubuntuhandbook.org/index.php/2025/03/input-leap-share-mouse-keyboard/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'ubuntuhandbook.org', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=ubuntuhandbook.org', 'site_name': 'UbuntuHandbook'}, 'is_missing': False, 'text': 'It’s Input Leap a free open-source application forked from Barrier, allowing to use single mouse and keyboard to control multiple computers in same local network. Input Leap is a fork of barrier, by barrier’s active maintainers. One of the core Barrier developer has not been active for ...\n\nIt’s Input Leap a free open-source application forked from Barrier, allowing to use single mouse and keyboard to control multiple computers in same local network. Input Leap is a fork of barrier, by barrier’s active maintainers. One of the core Barrier developer has not been active for a few years, and other maintainers do not have enough administrative access to maintain the project. So, the active maintainers of Barrier created the new Input Leap fork. Barrier is considered unmaintained currently, though Input Leap intends to maintain compatibility with older versions of Barrier. Input Leap has been made into many Linux Distributions’ system repositories, including Arch Linux, Fedora, Manjaro, and Solus. For Debian 12, Ubuntu 22.04, Ubuntu 24.04, and Ubuntu 24.10, as well as Windows 10/11, and macOS 10.12 and newer, it provides official packages through the Github releases page: ...', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://ubuntuhandbook.org/index.php/2025/03/input-leap-share-mouse-keyboard/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Barrier download | SourceForge.net', 'url': 'https://sourceforge.net/projects/barrier.mirror/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'sourceforge.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=sourceforge.net', 'site_name': 'SourceForge'}, 'is_missing': False, 'text': 'Deploy in 115+ regions with the modern database for every enterprise. MongoDB Atlas gives you the freedom to build and run modern applications anywhere—across AWS, Azure, and Google Cloud.\n\nSimple and easy control of multiple computers with just one mouse and keyboard ... Deploy in 115+ regions with the modern database for every enterprise. MongoDB Atlas gives you the freedom to build and run modern applications anywhere—across AWS, Azure, and Google Cloud. With global availability in over 115 regions, Atlas lets you deploy close to your users, meet compliance needs, and scale with confidence across any geography. ... Rant: (to SourceForge: Excessive punctuation is prohibited? Do you have any idea of how unreadable user comments become without it??? So getting done with you... ) 2025, 6th August Hi "all", TL;DR-1 (input-leap): head to Barrier\'s github link above and find the link to input-leap): TL;DR-2 (this, unmantained, Barrier): - It works! - configuration screen misguides you into thinking it\'s all about machine ip addresses. IT IS NOT!\n\nSome successfully installed, some went through different levels of \'pain\' to get it working. - WHY DO WE NEED THE CLIENT HOSTNAME WHEN THEY CAN BE CONFIGURED BY IP? <name-your-god>-only-know\'s... :P *After reading instructions* - Well, let\'s put the damn name into the server screen... reload... "running"... - Let\'s stop and restart debian\'s client... "running"! - It WORKS! :D - kind of... No file dragging... no file copy/paste from windows explorer, no text copy/paste... barrier logs do show clipboard being updated... Ok, let\'s call it a day... - Today, 6th August, while accidentally (having forgot clipboard wasn\'t working) copying something from a browser on windows to paste in debian... - wait! what? It pasted ! - does file...? - nope, that\'s still a - no file dragging, copy/paste... *Conclusion* - hmmm, might fork it - i thought, ... Only then I learned about the new «Input-Leap» project.\n\nCreate macros, control and simulate keyboard and mouse events with LUA scripts; also supports remapping of keyboard, game controller, and mouse events. ... Mouse Control is a remote administration application made in Visual Basic 6.\n\nIt allows you to control the mouse, keyboard, shutdown computer, watch the remote screen, and more.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://sourceforge.net/projects/barrier.mirror/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Great Barrier Alternatives: Top Mouse Sharing Utilities in 2025 | AlternativeTo', 'url': 'https://alternativeto.net/software/barrier/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'alternativeto.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=alternativeto.net', 'site_name': 'AlternativeTo'}, 'is_missing': False, 'text': "The best Barrier alternatives are Input Leap, Synergy and Mouse without Borders. Our crowd-sourced lists contains more than 10 apps similar to Barrier for Windows, Mac, Linux, BSD and more.\n\nBarrier is described as 'Cross-platform software utility for sharing your mouse and keyboard between multiple computers on your desk. It was forked from Synergy version 1.9's codebase' and is a very popular Mouse Sharing utility in the os & utilities category. There are more than 10 alternatives to Barrier for a variety of platforms, including Windows, Mac, Linux, BSD and Flathub apps. The best Barrier alternative is Input Leap, which is both free and Open Source. Other great apps like Barrier are Synergy, Mouse without Borders, InputShare and Input Director. Barrier alternatives are mainly Mouse Sharing Utilities, but if you're looking for Keyboard Sharing Utilities or Remote Desktop Tools you can filter on that. Other popular filters include Linux. You can also filter by region, for example EU-based alternatives if you prefer software developed in the European Union.\n\nBarrier is a cross-platform software utility for sharing your mouse and keyboard between multiple computers on your desk. It was forked from Synergy version 1.9's codebase. ... Input Leap is software that mimics the functionality of a KVM switch, which historically would allow you to use a single keyboard and mouse to control multiple computers by physically turning a dial on the box to switch the machine you're controlling at any given moment.19 Input Leap alternatives ... Barrier has been stagnant since 2021. Developers moved to Input Leap. ... Neither really have a grip on security. #1204 ... Synergy combines your desktop devices together in to one cohesive experience. It's software for sharing your mouse and keyboard between multiple computers on your desk. It works on Windows, macOS and Linux.19 Synergy alternatives ... As Barrier is forked from earlier versions of Synergy, there is naturally a lot of feature set overlap.\n\nMultiplicity offers a virtual KVM solution, managing several computers with one keyboard and mouse. Its remote modes enable cursor transition across monitors and centralized control. Users can transfer files, stream audio, and lo... ... InputShare enables you to share the keyboard and mouse of your computer with an Android device via ADB in wired / wireless way.12 InputShare alternatives ... Input Director is a Windows application that lets you control multiple Windows systems using the keyboard/mouse attached to one computer. It is designed for folks who have two (or more) computers set up at home and find themselves regularly sliding from one system to the other.15 Input Director alternatives ... Very easy painless setup. It's free. No lagging, works. ... I've used Input Director for years on Windows computers, and its smoothness, clipboard sharing, and built-in encryption are second to none.\n\nDeskflow is a free and open-source keyboard and mouse sharing app. Use the keyboard, mouse, or trackpad of one computer to control nearby computers, and work seamlessly between them. It's like a software KVM (but without the video). TLS encryption is enabled by default.11 Deskflow alternatives ... Barrier's predecessor is Synergy. Deskflow is an open source app that also includes Synergy developers. The previous repository name was Synergy-core. it's Synergy system. Deskflow is Free and Open SourceBarrier is also Free and Open Source · Deskflow is Privacy focused and LightweightBarrier is not according to our users ... Multiplicity offers a virtual KVM solution, managing several computers with one keyboard and mouse. Its remote modes enable cursor transition across monitors and centralized control. Users can transfer files, stream audio, and lock computers without extra hardware, suitable for command rooms, IT desks, and home users.22 Multiplicity alternatives ...", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://alternativeto.net/software/barrier/', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'GitHub - deskflow/deskflow: Share a single keyboard and mouse between multiple computers. · GitHub', 'url': 'https://github.com/deskflow/deskflow', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': "Input Leap - Inactive Deskflow/Synergy-derivative with the goal continuing Barrier development (now a dead fork). Yes, Deskflow has network compatibility with all forks: ... Deskflow will just work with Input Leap and Barrier (server or client). Connecting a Deskflow client to a Synergy 1 server will also just work. To connect a Synergy 1 client, you need to select the Synergy protocol in the Deskflow server settings. Note: Only Synergy 1 is compatible with Deskflow (Synergy 3 is not yet compatible). We would love to see compatibility with Lan Mouse. This may be quite an effort as currently the way they handle the generated input is very different. We welcome PRs (pull requests) from the community. If you&#x27;d like to make a change, please feel free to start a discussion or open a PR. Absolutely. The clipboard-sharing feature is a cornerstone feature of the product and we are committed to maintaining and improving that feature.\n\nInput Leap - Inactive Deskflow/Synergy-derivative with the goal continuing Barrier development (now a dead fork). Yes, Deskflow has network compatibility with all forks: ... Deskflow will just work with Input Leap and Barrier (server or client). Connecting a Deskflow client to a Synergy 1 server will also just work. To connect a Synergy 1 client, you need to select the Synergy protocol in the Deskflow server settings. Note: Only Synergy 1 is compatible with Deskflow (Synergy 3 is not yet compatible). We would love to see compatibility with Lan Mouse. This may be quite an effort as currently the way they handle the generated input is very different. We welcome PRs (pull requests) from the community. If you'd like to make a change, please feel free to start a discussion or open a PR. Absolutely. The clipboard-sharing feature is a cornerstone feature of the product and we are committed to maintaining and improving that feature.", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/deskflow/deskflow', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'GitHub - input-leap/input-leap: Open-source KVM software · GitHub', 'url': 'https://github.com/input-leap/input-leap', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': "Input Leap is software that mimics the functionality of a KVM switch, which historically would allow you to use a single keyboard and mouse to control multiple computers by physically turning a dial on the box to switch the machine you&#x27;re ...\n\nNote that if the keyboard's Scroll Lock is active then this will prevent the mouse from switching screens. To find information about configuring Input Leap look at the wiki · Please be aware that the only way to draw our attention to a bug is to create a new issue in the issue tracker. Always follow the template, it's there for a reason. Failure to do so will inevitably result in a delay in the issue being fixed! Please also see the IRC channels at the top of the README for other methods of support. At this time we are looking for developers to help fix the issues found in the issue tracker. Submit pull requests once you've polished up your patch and we'll review and possibly merge it. Most pull requests will need to include a release note. See doc/newsfragments/README.md for documentation of how to do that. While not a comprehensive list, repology provides a decent list of distro specific packages. Q: Input Leap vs. barrier?\n\nA: Input Leap is a fork of barrier, by barrier's active maintainers. See issue #1414 for more details. Currently, barrier is considered unmaintained. ... Q: After loading my configuration on the client the field 'Server IP' is still empty! A: Edit your configuration to include the server's ip address manually with · (...) section: options serverhostname=<AAA.BBB.CCC.DDD> Q: Are there any other significant limitations with the current version of Input Leap? ... Input Leap currently has limited UTF-8 support; issues have been reported with processing various languages. ... Clipboard sharing is not currently supported on Linux/Wayland. AltGr key combinations when Server is linux and client is Windows don't usually work out of the box. See #100 for a workaround · The complete list of open issues can be found in the 'Issues' tab on GitHub.\n\nInput Leap is software that mimics the functionality of a KVM switch, which historically would allow you to use a single keyboard and mouse to control multiple computers by physically turning a dial on the box to switch the machine you're controlling at any given moment. Input Leap does this in software, allowing you to tell it which machine to control by moving your mouse to the edge of the screen, or by using a keypress to switch focus to a different system. At the moment, Input Leap is not compatible with Synergy. Input Leap needs to be installed on all machines that will share keyboard and mouse. Whereas Synergy has moved beyond its goals from the 1.x era, Input Leap aims to maintain that simplicity. Input Leap will let you use your keyboard and mouse from one computer to control one or more other computers. Clipboard sharing is supported (Note: Not currently supported on Linux/Wayland).", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/input-leap/input-leap', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Share Your Keyboard and Mouse Between Linux and Raspberry Pi', 'url': 'https://itsfoss.com/keyboard-mouse-sharing-between-computers/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'itsfoss.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=itsfoss.com', 'site_name': "It's FOSS"}, 'is_missing': False, 'text': "I learned this the hard way after extensive testing. On the second computer, start input-leap and choose to use it as client. You need to provide the IP address of input-leap server.\n\nInput Leap does not support Wayland. If your system uses Wayland, you’ll need to switch to X11 or consider alternatives like Barrier. I learned this the hard way after extensive testing. On the second computer, start input-leap and choose to use it as client. You need to provide the IP address of input-leap server. You can find this IP address on the input-leap application running on the main system, in my case on my Raspberry Pi (see the screenshots in previous section). If you see an option to accept secure connection from another computer, accept it. You should be now able to move your mouse pointer between the screens connected to two different computers running two different operating systems. How cool is that! During my initial attempts, I couldn’t get input-leap to build successfully on my Raspberry Pi. As a workaround, I used Barrier on the Pi and Input Leap on my Windows PC.\n\nSoftware: You use a tool like Barrier or its fork Input Leap (both explained in detail in this article). ... If you could, go for a keyboard mouse pair that allows connecting/switching between multiple devices. That will be a convenient option. The software method takes some effort but it could be a solution when you want to learn something new and don't want to spend on new hardware. If you cannot go for the hardware solution, try the software based approach to share the keyboard and mouse between computers. Barrier used to be the go-to software for this kind of approach but it has not seen new development in years. An earlier version of this tutorial used Barrier, and the instructions can still be followed in the PDF here. I used Input Leap, a fork of another open-source project called Barrier. The architecture of this setup is simple. You setup Input Leap in server mode on the system where keyboard-mouse is attached.\n\nAnd then you setup Input Leap or Barrier in client mode. Why Barrier? I'll discuss it later in the tutorial. ... Did I mention that you can even share clipboard and thus copy paste text between the computers using Input Leap? That's awesome, isn't it? Let’s see how to share the mouse and keyboard with multiple computers using this method. The developers of Input Leap have kindly provided pre-built releases on their GitHub page. This is the easiest way to get started. Visit the GitHub releases page and download the .deb file that matches your system’s architecture (e.g., amd64). ... That’s it! Your Debian system is ready to share its keyboard and mouse. Configure the client on your secondary device(s). If you can’t find a suitable pre-built release, or you’re using a platform like Raspberry Pi, you’ll need to build Input Leap manually from source.\n\nBuilding from source could be intimidating and often not worth the effort. If it scares you, you can try installing barrier on Raspberry Pi as it is available in Debian repositories. Input Leap as server and Barrier as client works fine, too. If you still decided to go for source code installation, here are the steps. Ensure your system has all the necessary tools and libraries installed: sudo apt-get install -y \\ cmake \\ g++ \\ git \\ libavahi-compat-libdnssd-dev \\ libcurl4-openssl-dev \\ libice-dev \\ libsm-dev \\ libssl-dev \\ libxinerama-dev \\ libxrandr-dev \\ libxtst-dev \\ libxkbcommon-dev \\ libglib2.0-dev \\ ninja-build \\ qtdeclarative5-dev \\ qttools5-dev \\ meson ... You do it on the computer that has keyboard and mouse attached to it. Once you build and install Input Leap, you won’t find its icon in the main menu bar. To access it, simply type: ...", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://itsfoss.com/keyboard-mouse-sharing-between-computers/', 'search_provider': 'anthropic', 'age': 'December 2, 2024'}} {'type': 'knowledge', 'title': 'Top 10 Synergy Alternatives and Competitors in 2025', 'url': 'https://buddyxtheme.com/synergy-alternatives-and-competitors/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'buddyxtheme.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=buddyxtheme.com', 'site_name': 'BuddyX'}, 'is_missing': False, 'text': 'Input Leap is another open-source tool derived from Barrier and Synergy. While still in active development, it supports multi-platform mouse and keyboard control over a network. It works well on Windows and Linux, and macOS support is improving.\n\nWhile not designed for peripheral sharing, VNC solutions like RealVNC, TigerVNC, or TightVNC can provide full remote control of another system, including keyboard and mouse, via a graphical interface. This is more of a remote desktop setup, but it can work for those who need occasional interaction without physically switching devices. Best for: Users already using VNC for remote access and looking to expand control across devices. Input Leap is another open-source tool derived from Barrier and Synergy. While still in active development, it supports multi-platform mouse and keyboard control over a network. It works well on Windows and Linux, and macOS support is improving. Users who want to tinker and possibly contribute to the project may find this a good fit. Best for: Developers and Linux enthusiasts looking for a community-driven open-source solution.\n\nBarrier is a free and open-source fork of Synergy that retains the core functionality—keyboard and mouse sharing across networked computers—without the paywall. It’s one of the closest alternatives, offering cross-platform support for Windows, macOS, and Linux, along with features such as a shared clipboard and drag-and-drop file transfer. Setup is a bit technical, but the community is active, and performance is generally stable for LAN use. Best for: Users who want Synergy’s functionality without paying, and don’t mind a basic UI. Also Read: Top 25 Fiverr Alternatives for Freelancers and Businesses · If you’re using Logitech mice and keyboards, Logitech Flow (now part of Logi Options+) allows device switching across Windows and macOS by simply moving your cursor across screens. It also supports clipboard sync and file drag-and-drop. It requires compatible Logitech devices, but when it works, it’s seamless and stable.\n\nBest for: Windows-only users who want fast and free keyboard/mouse sharing on a local network. ShareMouse offers seamless control of multiple Windows and Mac systems with automatic device discovery, drag-and-drop file transfers, and clipboard sync. It provides a polished, intuitive user interface and supports features like screen dimming when switching devices. The free version supports basic sharing between two devices, while the Pro version unlocks additional functionality like multi-monitor support and password protection. Best for: Professionals seeking a polished Synergy alternative with easy setup and strong performance. If you’re looking for a direct free alternative, Barrier and Mouse Without Borders are the most accessible, offering solid keyboard and mouse sharing without a paywall. For a feature-rich, polished experience, ShareMouse and Multiplicity offer more stable performance and support for advanced setups, including multi-monitor workflows, clipboard synchronization, an\n\n1. How can I use a single keyboard and mouse between multiple computers? You can use software solutions like Synergy, Barrier, ShareMouse, or Input Director to share a keyboard and mouse across multiple computers over a local network. These tools allow seamless control, clipboard sharing, and sometimes even drag-and-drop file transfers between devices. 2. Are there free alternatives to Synergy for sharing a keyboard and mouse? Yes, Barrier and Mouse Without Borders are popular free alternatives. Barrier works on Windows, macOS, and Linux, while Mouse Without Borders is Windows-only. Both offer basic keyboard and mouse sharing functionality without cost. 3. Can I use one keyboard and mouse across Windows and macOS? Absolutely. Paid solutions like ShareMouse and Logi Options+ / Logitech Flow, as well as open-source tools like Barrier, support cross-platform setups.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://buddyxtheme.com/synergy-alternatives-and-competitors/', 'search_provider': 'anthropic', 'age': 'August 18, 2025'}} {'type': 'knowledge', 'title': 'GitHub - feschber/lan-mouse: mouse & keyboard sharing via LAN · GitHub', 'url': 'https://github.com/feschber/lan-mouse', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'github.com', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=github.com', 'site_name': 'GitHub'}, 'is_missing': False, 'text': 'Goal of this project is to be an open-source alternative to proprietary tools like Synergy 2/3, Share Mouse and other open source tools like Deskflow or Input Leap (Synergy fork).\n\nGoal of this project is to be an open-source alternative to proprietary tools like Synergy 2/3, Share Mouse and other open source tools like Deskflow or Input Leap (Synergy fork). Focus lies on performance, ease of use and a maintainable implementation that can be expanded to support additional backends for e.g. Android, iOS, ... in the future. ... Lan Mouse encrypts all network traffic using the DTLS implementation provided by WebRTC.rs. There are currently no mitigations in place for timing side-channel attacks. Most current desktop environments and operating systems are fully supported, this includes ... X11 currently only has support for input emulation, i.e. can only be used on the receiving end. Sway / wlroots: Wlroots based compositors without libei support on the receiving end currently do not handle modifier events on the client side. This results in CTRL / SHIFT / ALT / SUPER keys not working with a sending device that is NOT using the layer-shell backend ·', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://github.com/feschber/lan-mouse', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Just tried Barrier - MX Linux Forum', 'url': 'https://forum.mxlinux.org/viewtopic.php?t=79933', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'mxlinux.org', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=mxlinux.org', 'site_name': 'MX Linux Forum'}, 'is_missing': False, 'text': 'The main effort is getting it working on Wayland. There are two active devs from Barrier working on it. So leap-input is the spiritual and literal successor to Barrier. That said I&#x27;m lucky to have gotten Barrier working on my 3 machines. I read lots of posts from people who haven&#x27;t been so lucky.\n\nOld thread, but I\'m also using barrier for years, it was not updated for almost 3 years. I tried deskflow but it\'s not mature enough. I just discovered that input-leap had issued binaries/packages, ready to install (I used debian 12 deb and windows exe), fully compatible with barrier, but to do it properly I changed my .config folder etc but config is the same. It works pretty well. It looks like between latest barrier v2.4.0 and this 3.0.2 input-leap, there\'s is ~800 changes/fix in the code. Try it :) https://github.com/input-leap/input-leap/releases ·\n\n@CharlesV As usual I often post too soon. In this case Barrier hasn\'t been updated on GitHub since late 2021 (I think). They\'ve forked it over to a new project "input-leap" which hasn\'t had a first build yet. The source code is there to compile. The main effort is getting it working on Wayland. There are two active devs from Barrier working on it. So leap-input is the spiritual and literal successor to Barrier. That said I\'m lucky to have gotten Barrier working on my 3 machines. I read lots of posts from people who haven\'t been so lucky. But I did have my struggles. Also disabled SSL per a YouTube video suggestion. There\'s an option to use SSL without a certificate. Had to open up the firewall on the Linux server host. It was added automatically on Windows. The MX RPi respin doesn\'t have a firewall by default. In some ways NoMachine has advantages for me.\n\nI came across "Barrier" which acts as a partial software KVM switch or a KM without the V. I used a KVM for a couple years at home to switch keyboard, mouse, and monitor between two Windows 10 PCs. I worked on contract where they sent me a mini PC monitor, keyboard, and mouse. I only got the mini PC out of the box as I didn\'t want their keyboard and mouse. I had an old DVI KVM setting in the box unused. Had to buy an adapter for DisplayPort to DVI and was set. Used this for two years and it worked like a champ. But it was limited to two machines. The other option is various remote desktop options. I\'ve been using this option at home recently. Mostly used Nomachine recommended by @CharlesV and I agree it\'s about the best for desktop to deskop. Then I saw an article about Syngery which is the commercial version of Barrier. Barrier doesn\'t have the most helpful docs imho.\n\nI even started compiling it, but soon realized MXPI has it on both x64 and arm64. And they have a Windows x64 version. So now I have my MX 23 XFCE, Windows PC, and MX Raspberry Pi 4B and working together. The MX desktop is the server and has the keyboard & mouse directly connected. The other two machines are clients. It took a few tries for the Windows install to persist the server IP address, but noticed finally persisted it after a shutdown and startup. And it works as a client on my RPI 4B. The biggest downside is having to toggle between video inputs on my monitor. It was meant to be used with a monitor on each machine. Selecting which machine has focus is a matter of moving the mouse off screen. With multiple monitors, it would a breeze. But with a single monitor, I have to careful about moving the mouse off screen. I\'ll probably switch the server machine over the the RPi 4B as it\'s powered up 24/7.', 'is_citable': True, 'prompt_context_metadata': {'url': 'https://forum.mxlinux.org/viewtopic.php?t=79933', 'search_provider': 'anthropic'}} {'type': 'knowledge', 'title': 'Lan Mouse: open source cross-platform mouse and keyboard sharing software - gHacks Tech News', 'url': 'https://www.ghacks.net/2024/01/03/lan-mouse-open-source-cross-platform-mouse-and-keyboard-sharing-software/', 'metadata': {'type': 'webpage_metadata', 'site_domain': 'ghacks.net', 'favicon_url': 'https://www.google.com/s2/favicons?sz=64&domain=ghacks.net', 'site_name': 'gHacks Tech News'}, 'is_missing': False, 'text': "Programs like Mouse Without Borders, Stardock&#x27;s Multiplicity KVM, Input Leap, or ShareMouse offer similar functionality. The programs are either commercial or only available for specific platforms.\n\nThe roadmap lists several major improvements. Next to introducing input capture on the systems that don't support it yet, Windows, macOS and x11 for the most part, there will also be IP address switching functionality, Clipboard support and support for encryption for security. ... Lan Mouse is an interesting open source project to control multiple computers with a single mouse and keyboard. The project is in active development and new versions have been released regularly up to this point. Now You: do you use software like Lan Mouse or have use for it? Previous Post: « 20 years of Notepad++. Version 8.6 launches with Multi-Edit feature Next Post: « Canonical: up to 12 years of support for Ubuntu 24.04 LTS · Chukwudum Okeke said on October 14, 2024 at 4:09 pm Reply · Ah, if only it could work on android too. ... No and No but, I can imagine setups where it could be useful.\n\nPrograms like Mouse Without Borders, Stardock's Multiplicity KVM, Input Leap, or ShareMouse offer similar functionality. The programs are either commercial or only available for specific platforms. The core idea of all of these programs is to control multiple devices, e.g. a Windows PC, a macBook and a Linux system, with the mouse and keyboard of one of these devices. Lan Mouse's latest version can be downloaded from GitHub. Installation packages for Linux, macOS and Windows as well as the source code are provided there. The application has an interface but it can also be used from the command line. There is a configuration file that supports loading clients automatically on startup. Note that Windows may throw a SmartScreen security error when Lan Mouse is launched. This is a false positive, which happens often when software is new. The interface displays all connected clients and the option to add clients to control them with a single mouse and keyboard set.\n\nI’ve used Barrier for this for years. https://github.com/debauchee/barrier · Anonymous said on January 3, 2024 at 10:50 pm Reply · Interesting idea. I will try it out. VioletMoon said on January 3, 2024 at 9:10 pm Reply · “Do you use software like Lan Mouse or have use for it?” · Software like TeamViewer or RustDesk has the option of controlling a computer, mouse and all. I think I can envision the program being used in the classroom–either for helping students or for putting an obstacle in their fun and games during study. FireWire said on January 6, 2024 at 10:07 pm Reply · TeamViewer is now bloated Electron garbage. Uninstalled that trash on my pcs. AnyDesk turned into nagware. RustDesk is the only good option nowadays. Apple to Launch AI Smart Glasses With Cameras and Silent Voice Control · Windows 11 Has 4 Powerful Features Most Users Never Turn On (But Should) Anthropic Launches Claude Inside PowerPoint for AI-Powered Slide Creation and Editing ·", 'is_citable': True, 'prompt_context_metadata': {'url': 'https://www.ghacks.net/2024/01/03/lan-mouse-open-source-cross-platform-mouse-and-keyboard-sharing-software/', 'search_provider': 'anthropic', 'age': 'January 3, 2024'}}
Let's try **Deskflow** — it's the most actively maintained, works on X11, and is compatible with Input Leap/Barrier protocols.

```bash
sudo apt install deskflow
```

If not in repos, install via flatpak:
```bash
flatpak install flathub io.github.deskflow.deskflow
```

---

### Setup (mouse & keyboard on Windows):

**On Linux — set as Client:**
1. Open Deskflow
2. Choose **Client** mode
3. Enter your **Windows IP** (`192.168.29.38`)

**On Windows — set as Server:**
1. Download Deskflow from: `https://github.com/deskflow/deskflow/releases/latest`
2. Open it, choose **Server** mode
3. Click **Configure Server**, add Linux screen to the right/left of Windows
4. Click **Start**

Since your mouse/keyboard is on Windows, Windows is the **server** and Linux is the **client**.

What error did Input Leap give you? That might help us fix it too as a backup option.

---

### 🧑 You

not connecting deskflow

---

### 🤖 Claude

Let me check the exact issue:

{'type': 'text', 'text': '{\n  "questions": [\n    {\n      "question": "What error does Deskflow show?",\n      "options": [\n        "Timeout / no connection",\n        "SSL/TLS certificate error",\n        "Connected but mouse doesn\'t move",\n        "Crashes immediately"\n      ],\n      "type": "single_select"\n    },\n    {\n      "question": "Are both PCs on the same WiFi router?",\n      "options": [\n        "Yes, same router",\n        "No, different networks"\n      ],\n      "type": "single_select"\n    }\n  ]\n}', 'uuid': 'c81416d2-d22a-4940-a71f-6dec494307c7'}

---

### 🧑 You

Q: What error does Deskflow show?
A: SSL/TLS certificate error

Q: Are both PCs on the same WiFi router?
A: Yes, same router

---

### 🤖 Claude

SSL/TLS is a common Deskflow issue — easy fix!

**On Windows Deskflow (Server):**
1. Go to **Edit → Preferences**
2. Uncheck **Enable SSL/TLS**
3. Click **OK**
4. Click **Stop** then **Start**

**On Linux Deskflow (Client):**
1. Go to **Edit → Preferences**
2. Uncheck **Enable SSL/TLS**
3. Click **OK**
4. Disconnect and reconnect

Both sides must have SSL **disabled** to match each other. Try connecting again after that.

---

### 🧑 You

in linux it is showing edit

---

### 🤖 Claude

On Linux Deskflow, look for SSL settings in a different place:

1. Click the **☰ menu** or **Settings** (gear icon)
2. Look for **Preferences** or **Advanced settings**
3. Find **SSL/TLS** option and uncheck it

**Or try via command line** — run Deskflow without SSL:

```bash
deskflow --no-tls
```

**Or**, if you can't find it in the GUI, disable SSL from the config file:

```bash
nano ~/.config/deskflow/deskflow.conf
```

Look for a line with `tls` or `ssl` and set it to `false`.

Can you share a screenshot of what the Linux Deskflow window looks like? That'll help me point to the exact option.

---

### 🧑 You

it is like this no any button to edit

---

### 🤖 Claude

I can see the issue — the **Connect to** field shows `192.168.9.1` which is wrong. Your Windows IP is `192.168.29.38`.

Also, to disable SSL, click the **≈ (hamburger/wave) menu icon** in the top left corner.

**Steps:**

1. Click **≈** (top left) → look for **Preferences** or **Settings** → disable SSL/TLS

2. Change the IP in **Connect to** field from `192.168.9.1` to:
   **`192.168.29.38`**

3. Make sure **"Use another computer's mouse and keyboard (client)"** is selected ✅ (it already is)

4. Click **Connect**

Try that and let me know what happens!

---

### 🧑 You

in my windows it is showing  192.168.9.1

---

### 🤖 Claude

Then your Windows IP is `192.168.9.1` — that's correct for your network! Leave the IP as is.

The only issue is **SSL/TLS**. Click the **≈ icon** (top left corner of Deskflow) and check if there's a Preferences option there.

Also on **Windows Deskflow**:
1. Click **Edit → Preferences**
2. Uncheck **Enable SSL**
3. Restart Deskflow on Windows

Then click **Connect** on Linux.

What does the ≈ menu show when you click it on Linux?

---

### 🧑 You

in linux it is showing please check your tls and firewall settings

---

### 🤖 Claude

That confirms it's an SSL issue. Let's fix it via the config file directly:

```bash
# First stop deskflow if running, then edit config
mkdir -p ~/.config/deskflow
nano ~/.config/deskflow/deskflow.conf
```

Look for `tls` or `ssl` line and change it to `false`. If the file is empty or doesn't exist, paste this:

```ini
[deskflow]
tlsEnabled=false
```

Save with **Ctrl+O → Enter → Ctrl+X**

Then restart Deskflow and click **Connect**.

---

Also on **Windows**, make sure SSL is disabled:
1. Open Deskflow on Windows
2. **Edit → Preferences → uncheck "Enable TLS"**
3. Click **Stop → Start**

---

If config file approach doesn't work, try running Deskflow from terminal to see the exact error:

```bash
deskflow 2>&1 | head -30
```

or 

```bash
flatpak run io.github.deskflow.deskflow 2>&1
```

What does the Windows Deskflow **Edit → Preferences** show — is there a TLS/SSL checkbox there?

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ deskflow 2>&1 | head -30 deskflow: command not found ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ flatpak run io.github.deskflow.deskflow 2>&1 error: app/io.github.deskflow.deskflow/x86_64/master not installed ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯

---

### 🤖 Claude

How did you install Deskflow then? Let's find it:

```bash
which deskflow
find / -name "deskflow*" 2>/dev/null | grep -v proc
```

Also check if it's a downloaded binary or AppImage:

```bash
ls ~/Downloads/ | grep -i desk
ls ~/ | grep -i desk
```

Paste the output and I'll find where it is and how to run it with the right flags to disable TLS.

---

### 🧑 You

on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ which deskflow find / -name "deskflow*" 2>/dev/null | grep -v proc /home/sunny77/deskflow.key /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/tls/deskflow.pem /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/deskflow-server.conf /home/sunny77/.config/deskflow /home/sunny77/.config/deskflow/deskflow.conf /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/app-info/media/org/deskflow /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/app-info/media/org/deskflow/deskflow /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/man/man1/deskflow.1 /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/man/man1/deskflow-core.1 /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/deskflow /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/deskflow/translations/deskflow_ja.qm /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/deskflow/translations/deskflow_it.qm /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/deskflow/translations/deskflow_zh_CN.qm /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/deskflow/translations/deskflow_ru.qm /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/deskflow/translations/deskflow_en.qm /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/deskflow/translations/deskflow_es.qm /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/deskflow/translations/deskflow_ko.qm /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/licenses/deskflow /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/share/licenses/org.deskflow.deskflow/deskflow /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/bin/deskflow /var/lib/flatpak/app/org.deskflow.deskflow/x86_64/stable/69ba131ee89a84ef7d516fc0db91270d1d39ef7faadb52419c498ac48d6f2cb8/files/bin/deskflow-core ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12 took 14s  ❯ ls ~/Downloads/ | grep -i desk ls ~/ | grep -i desk opencode-desktop-linux-amd64 opencode-desktop-linux-amd64.deb deskflow.key Desktop ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯

---

### 🤖 Claude

It's installed as flatpak with ID `org.deskflow.deskflow`. Disable TLS via the config file directly:

```bash
cat ~/.var/app/org.deskflow.deskflow/config/Deskflow/deskflow-server.conf
```

Then edit the config to disable TLS:

```bash
nano ~/.var/app/org.deskflow.deskflow/config/Deskflow/deskflow-server.conf
```

Look for a `[deskflow]` section and add or change:
```ini
tlsEnabled=false
```

Also edit the main config:
```bash
nano ~/.config/deskflow/deskflow.conf
```

Add:
```ini
[deskflow]
tlsEnabled=false
```

Then run it correctly:
```bash
flatpak run org.deskflow.deskflow
```

And make sure **Windows Deskflow also has TLS disabled** in Edit → Preferences before clicking Connect.

---

### 🧑 You

ection: screens        maz77:                halfDuplexCapsLock = false                halfDuplexNumLock = false                halfDuplexScrollLock = false                xtestIsXineramaUnaware = false                switchCorners = none                switchCornerSize = 0 end section: aliases end section: links        maz77: end section: options        protocol = synergy        relativeMouseMoves = false        win32KeepForeground = false        defaultLockToScreenState = false        disableLockToScreen = false        clipboardSharing = true        clipboardSharingSize = 3072        switchCorners = none        switchCornerSize = 0 end

---

### 🤖 Claude

The config doesn't have TLS settings there. Let's disable it directly in the Deskflow settings file:

```bash
nano ~/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf
```

Add this at the bottom:
```ini
[deskflow]
tlsEnabled=false
```

Save with **Ctrl+O → Enter → Ctrl+X**

Then run:
```bash
flatpak run org.deskflow.deskflow
```

---

Also, **on Windows Deskflow** — go to:
**Edit → Preferences → Security tab** → uncheck **Enable TLS** → click OK → Stop → Start

Both sides must have TLS off. Did you find the TLS option on Windows side?

---

### 🧑 You

still same not working

---

### 🤖 Claude

Let's try **Barrier** — the older, simpler version that works reliably on X11 without TLS issues:

```bash
sudo apt install barrier
```

Then:

**On Linux (Client — no keyboard/mouse here):**
1. Open Barrier
2. Select **Client**
3. Enter Windows IP: `192.168.9.1`
4. Go to **Barrier → Change Settings** → uncheck **Enable SSL**
5. Click **Start**

**On Windows (Server — keyboard/mouse here):**
1. Download Barrier from: `https://github.com/debauchee/barrier/releases/latest`
2. Open it, select **Server**
3. Click **Configure Server** → drag a new screen next to yours → name it **maz77** (your Linux hostname)
4. Go to **Barrier → Change Settings** → uncheck **Enable SSL**
5. Click **Start**

---

The key difference from Deskflow — Barrier has a clear **"Enable SSL" checkbox** in Settings that's easy to find and disable on both sides.

Try installing it first:
```bash
sudo apt install barrier
```

Does it install successfully?

---

### 🧑 You

i tried barrier it also did not work

---

### 🤖 Claude

Let me think differently. The root issue is **X11**. Let me try a completely different approach — **x2x**, which was made specifically for X11:

```bash
sudo apt install x2x
```

But actually, let me ask what exactly happened with Barrier — because Barrier **definitely works on X11**. The fix is almost always the same SSL issue.

{'type': 'text', 'text': '{\n  "questions": [\n    {\n      "type": "single_select",\n      "options": [\n        "SSL/TLS error",\n        "Timeout/no connection",\n        "Connected but mouse didn\'t move",\n        "Different error"\n      ],\n      "question": "What error did Barrier show?"\n    },\n    {\n      "type": "single_select",\n      "options": [\n        "Yes disabled on both",\n        "Only disabled on Linux",\n        "Only disabled on Windows",\n        "Couldn\'t find the option"\n      ],\n      "question": "Did you disable SSL on BOTH Windows and Linux Barrier?"\n    }\n  ]\n}', 'uuid': 'a4bef6ba-d1ac-4525-aeab-687262050f0c'}

---

### 🧑 You

Q: What error did Barrier show?
A: not connecting. but deskflow was working but suddently it is not working

Q: Did you disable SSL on BOTH Windows and Linux Barrier?
A: Only disabled on Linux

---

### 🤖 Claude

That's the problem! **SSL must be disabled on Windows too.**

Go to Windows Barrier:
1. Click **Barrier menu → Change Settings**
2. Uncheck **Enable SSL**
3. Click **OK**
4. Click **Stop** then **Start**

Then on Linux Barrier:
1. Make sure SSL is also unchecked
2. Click **Start**

---

Also, since **Deskflow was working before**, let's go back to Deskflow and fix it:

**On Windows Deskflow:**
1. Click **Edit → Preferences**
2. Find **Security** or **TLS** tab
3. **Uncheck Enable TLS**
4. Click **Stop → Start**

**On Linux:**
```bash
flatpak run org.deskflow.deskflow
```

The fact that Deskflow worked before means your network connection is fine — it's purely the TLS mismatch. Disable it on **Windows side** and it will connect again.

Can you check the Windows Deskflow **Edit → Preferences** and tell me exactly what tabs/options you see there?

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ nano ~/.var/app/org.deskflow.deskflow/config/Deskflow/deskflow-server.conf ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12 took 59s  ❯ nano ~/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12 took 28s  ❯ flatpak run org.deskflow.deskflow Qt: Session management error: Could not open network socket no qt translations found initial settings file: /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf initial language: en [2026-03-11T23:37:17.831] INFO: Deskflow v1.26.0 [2026-03-11T23:37:34.016] INFO: starting client process (desktop mode) [2026-03-11T23:37:34.016] INFO: running command: /app/bin/deskflow-core client [2026-03-11T23:37:52.579] INFO: stopping core process (desktop mode) [2026-03-11T23:37:52.579] INFO: stopping core desktop process [2026-03-11T23:37:52.580] WARNING: desktop process exited with code: 9 [2026-03-11T23:39:46.530] INFO: starting client process (desktop mode) [2026-03-11T23:39:46.530] INFO: running command: /app/bin/deskflow-core client [2026-03-11T23:39:55.260] INFO: stopping core process (desktop mode) [2026-03-11T23:39:55.260] INFO: stopping core desktop process [2026-03-11T23:39:55.262] WARNING: desktop process exited with code: 9 [2026-03-11T23:40:04.437] INFO: starting client process (desktop mode) [2026-03-11T23:40:04.438] INFO: running command: /app/bin/deskflow-core client [2026-03-11T23:40:11.814] INFO: stopping core process (desktop mode) [2026-03-11T23:40:11.815] INFO: stopping core desktop process [2026-03-11T23:40:11.816] WARNING: desktop process exited with code: 9

---

### 🤖 Claude

`exit code 9` means the process is being killed — likely a TLS handshake failure crashing it. Let's force disable TLS properly:

```bash
# Check current config
cat ~/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf
```

Then completely replace the config with TLS disabled:

```bash
cat > ~/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf << 'EOF'
[deskflow]
tlsEnabled=false
serverHostname=192.168.9.1
EOF
```

Then restart:
```bash
flatpak run org.deskflow.deskflow
```

---

**Most importantly — on Windows Deskflow right now:**
1. Click **Edit** in menu bar
2. Click **Preferences**
3. Screenshot and show me what you see — I need to confirm TLS is actually off on Windows side, because that's almost certainly why it's crashing with code 9.

---

### 🧑 You

tlsEnabled=false [server] externalConfig=false externalConfigFile=/home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/deskflow-server.conf ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ cat > ~/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf << 'EOF' [deskflow] tlsEnabled=false serverHostname=192.168.9.1 EOF ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ flatpak run org.deskflow.deskflow Qt: Session management error: Could not open network socket no qt translations found initial settings file: /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf initial language: en [2026-03-11T23:41:14.033] INFO: Deskflow v1.26.0 [2026-03-11T23:43:12.542] INFO: starting client process (desktop mode) [2026-03-11T23:43:12.543] INFO: running command: /app/bin/deskflow-core client [2026-03-11T23:43:28.759] INFO: stopping core process (desktop mode) [2026-03-11T23:43:28.760] INFO: stopping core desktop process [2026-03-11T23:43:28.761] WARNING: desktop process exited with code: 9

---

### 🤖 Claude

Linux TLS is off but it's still crashing. The problem is **Windows Deskflow still has TLS enabled** and is rejecting the connection, causing the crash.

**On Windows right now — please do this:**

1. Open Deskflow on Windows
2. Click **Edit** in the top menu bar
3. Click **Preferences**
4. Look for a **Security** tab or **TLS** checkbox
5. **Uncheck** it
6. Click **OK**
7. Click **Stop** then **Start**

---

If you can't find TLS option on Windows, try this — **uninstall Deskflow on Windows** and install **Barrier for Windows** instead (Barrier is simpler, no TLS by default):

👉 `https://github.com/debauchee/barrier/releases/download/v2.4.0/BarrierSetup-2.4.0-release.exe`

Then:
- Windows Barrier = **Server** (SSL unchecked)
- Linux Barrier = **Client** (SSL unchecked)
- Enter Windows IP `192.168.9.1` on Linux side

Can you take a screenshot of Windows Deskflow **Edit → Preferences** window and show me?

---

### 🧑 You

barrier did not work .but yesterday deskflow was working properly but i did connect it is not working now

---

### 🤖 Claude

Since Deskflow worked yesterday, something changed. Let's restore it to working state.

**On Windows Deskflow — check these exactly:**

1. What version of Deskflow is on Windows? (Help → About)
2. Is Windows Deskflow set as **Server**?
3. Is it currently **running/started**? (green status?)
4. Does it show your Linux machine (`maz77`) in the server layout?

---

Also on Linux, let's see the actual error by running the core directly:

```bash
flatpak run --command=deskflow-core org.deskflow.deskflow client --no-tls -f 192.168.9.1 2>&1
```

This will show the **exact error message** instead of just "exit code 9". Paste the output here.

---

### 🧑 You

yes it is showing maz77also

---

### 🤖 Claude

Good! So Windows is set up correctly. Run this on Linux to see the exact error:

```bash
flatpak run --command=deskflow-core org.deskflow.deskflow client --no-tls -f 192.168.9.1 2>&1
```

Paste the full output here — that will tell us exactly why it's failing.

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ flatpak run --command=deskflow-core org.deskflow.deskflow client --no-tls -f 192.168.9.1 2>&1 Unknown options: no-tls, f. [2026-03-11T23:48:05.342] WARNING: an instance of deskflow core is already running ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12

---

### 🤖 Claude

There's already a deskflow core running in background. Kill it and try again:

```bash
pkill -f deskflow
sleep 2
flatpak run --command=deskflow-core org.deskflow.deskflow client -f --no-daemon 192.168.9.1 2>&1
```

If that also fails with unknown options, try:

```bash
pkill -f deskflow
sleep 2
flatpak run --command=deskflow-core org.deskflow.deskflow --help 2>&1 | head -30
```

That will show us the exact correct syntax for the flags, then we can run it properly to see the real error.

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ flatpak run --command=deskflow-core org.deskflow.deskflow client --no-tls -f 192.168.9.1 2>&1 Unknown options: no-tls, f. [2026-03-11T23:48:05.342] WARNING: an instance of deskflow core is already running ~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ pkill -f deskflow sleep 2 flatpak run --command=deskflow-core org.deskflow.deskflow client -f --no-daemon 192.168.9.1 2>&1 Unknown options: f, no-daemon. initial settings file: /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf [2026-03-11T23:48:33.078] NOTE: configured 1 server address(es) [2026-03-11T23:48:33.078] INFO: using legacy x windows screen [2026-03-11T23:48:33.118] NOTE: started client [2026-03-11T23:48:33.118] IPC: connecting to '192.168.9.1': 192.168.9.1:24800 [2026-03-11T23:48:35.142] WARNING: failed to connect to server: Timed out [2026-03-11T23:48:36.153] IPC: connecting to '192.168.9.1': 192.168.9.1:24800 [2026-03-11T23:48:38.174] WARNING: failed to connect to server: Timed out [2026-03-11T23:48:39.181] IPC: connecting to '192.168.9.1': 192.168.9.1:24800 [2026-03-11T23:48:41.288] WARNING: failed to connect to server: Timed out [2026-03-11T23:48:42.074] IPC: connecting to '192.168.9.1': 192.168.9.1:24800 [2026-03-11T23:48:44.093] WARNING: failed to connect to server: Timed out [2026-03-11T23:48:45.103] IPC: connecting to '192.168.9.1': 192.168.9.1:24800 [2026-03-11T23:48:47.124] WARNING: failed to connect to server: Timed out [2026-03-11T23:48:48.133] IPC: connecting to '192.168.9.1': 192.168.9.1:24800 [2026-03-11T23:48:50.145] WARNING: failed to connect to server: Timed out [2026-03-11T23:48:51.153] IPC: connecting to '192.168.9.1': 192.168.9.1:24800 [2026-03-11T23:48:53.169] WARNING: failed to connect to server: Timed out [2026-03-11T23:48:54.175] IPC: connecting to '192.168.9.1': 192.168.9.1:24800

---

### 🤖 Claude

The error is **"Timed out"** — Linux can reach Windows IP but Windows Deskflow is not accepting connections. This is a **Windows firewall** blocking port 24800.

**On Windows — fix the firewall:**

1. Open **Windows Defender Firewall** (search in Start menu)
2. Click **Allow an app through firewall**
3. Find **Deskflow** and make sure both **Private** and **Public** are checked ✅
4. If not listed, click **Allow another app** → browse to `deskflow.exe`

**Or the quick way — open port 24800 on Windows:**
1. Press **Win+R** → type `wf.msc` → Enter
2. Click **Inbound Rules → New Rule**
3. Choose **Port → TCP → 24800**
4. Allow the connection → finish

Then on Linux press **Ctrl+C** to stop and run again:
```bash
flatpak run org.deskflow.deskflow
```

Click Connect — it should work now. The connection timing out means Windows is blocking it, not a TLS issue anymore.

---

### 🧑 You

[2026-03-11T23:49:32.052] INFO: starting client process (desktop mode)
[2026-03-11T23:49:32.053] INFO: running command: /app/bin/deskflow-core client
[2026-03-11T23:49:32.064] WARNING: an instance of deskflow core is already running
[2026-03-11T23:49:32.080] WARNING: desktop process is already running
[2026-03-11T23:53:31.328] INFO: starting client process (desktop mode)
[2026-03-11T23:53:31.328] INFO: running command: /app/bin/deskflow-core client
[2026-03-11T23:53:31.337] WARNING: an instance of deskflow core is already running
[2026-03-11T23:53:31.346] WARNING: desktop process is already running

---

### 🤖 Claude

Kill all deskflow processes first:

```bash
pkill -9 -f deskflow
sleep 2
flatpak run org.deskflow.deskflow
```

But more importantly — **have you opened port 24800 on Windows firewall yet?** That's the real fix needed right now. The timeout error confirmed Windows is blocking the connection.

Do the Windows firewall step first, then try connecting again.

---

### 🧑 You

[2026-03-11T23:54:40.707] INFO: starting client process (desktop mode)
[2026-03-11T23:54:40.708] INFO: running command: /app/bin/deskflow-core client
[2026-03-11T23:54:40.719] NOTE: configured 1 server address(es)
[2026-03-11T23:54:40.719] INFO: using legacy x windows screen
initial settings file: /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf
[2026-03-11T23:54:40.780] NOTE: started client
[2026-03-11T23:54:40.780] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:54:42.800] WARNING: failed to connect to server: Timed out
[2026-03-11T23:54:43.819] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:54:46.447] WARNING: failed to connect to server: Timed out
[2026-03-11T23:54:47.464] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:54:48.676] WARNING: failed to connect to server: Timed out
[2026-03-11T23:54:50.565] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:54:52.582] WARNING: failed to connect to server: Timed out
[2026-03-11T23:54:53.598] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:54:54.975] WARNING: failed to connect to server: Timed out
[2026-03-11T23:54:56.034] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:54:56.721] INFO: stopping core process (desktop mode)
[2026-03-11T23:54:56.721] INFO: stopping core desktop process
[2026-03-11T23:54:56.722] WARNING: desktop process exited with code: 9

---

### 🤖 Claude

Still timing out — Windows firewall is definitely blocking it. Please do this on Windows right now:

**Press Win+R → type this → Enter:**
```
netsh advfirewall firewall add rule name="Deskflow" dir=in action=allow protocol=TCP localport=24800
```

This opens port 24800 instantly without navigating menus.

Then also check if **Deskflow is actually running and started on Windows** — the status bar at the bottom should say **"Deskflow is running"** in green, not "not running".

Is Deskflow showing as **running** on Windows or **stopped**?

---

### 🧑 You

still not working in linux

---

### 🤖 Claude

Let's verify Windows is actually listening on port 24800. **On Windows**, open Command Prompt and run:

```
netstat -an | findstr 24800
```

Does it show anything? If it shows `LISTENING` then Windows is ready. If it shows nothing, Deskflow is not started on Windows.

Also check — **on Windows Deskflow, what does the status bar say at the bottom?** "Deskflow is running" or something else?

---

### 🧑 You

Failed to connect to the server '192.168.9.1'.
Please check your TLS and firewall settings.   in my linux

---

### 🤖 Claude

So TLS is still the issue. Let's completely remove the TLS certificate files that are causing the mismatch:

```bash
pkill -9 -f deskflow
rm -f ~/.var/app/org.deskflow.deskflow/config/Deskflow/tls/deskflow.pem
rm -f ~/deskflow.key
flatpak run org.deskflow.deskflow
```

And **on Windows Deskflow** — this is critical:
1. Click **Edit → Preferences**
2. Take a **screenshot** and show me

I need to see exactly what the Windows preferences look like because that's where TLS needs to be disabled. Without seeing it I'm guessing, and clearly the TLS option on Windows is still enabled.

---

### 🧑 You

Failed to connect to the server '192.168.9.1'.
Please check your TLS and firewall setting[2026-03-11T23:58:45.678] INFO: starting client process (desktop mode)
[2026-03-11T23:58:45.680] INFO: running command: /app/bin/deskflow-core client
[2026-03-11T23:58:45.692] NOTE: configured 1 server address(es)
[2026-03-11T23:58:45.692] INFO: using legacy x windows screen
initial settings file: /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf
[2026-03-11T23:58:45.753] NOTE: started client
[2026-03-11T23:58:45.753] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:58:47.772] WARNING: failed to connect to server: Timed out
[2026-03-11T23:58:48.793] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:58:50.812] WARNING: failed to connect to server: Timed out
[2026-03-11T23:58:51.821] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:58:54.388] WARNING: failed to connect to server: Timed out
[2026-03-11T23:58:55.407] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:58:57.427] WARNING: failed to connect to server: Timed out
[2026-03-11T23:58:58.437] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:00.457] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:01.468] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:03.486] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:04.496] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:06.515] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:07.526] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:09.546] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:10.519] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:12.566] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:13.586] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:15.386] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:16.406] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:18.428] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:19.440] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:21.459] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:22.468] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:24.490] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:25.498] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:27.513] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:28.522] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:30.545] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:31.556] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:33.573] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:34.581] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:36.580] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:37.159] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:39.177] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:39.890] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:42.323] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:43.331] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-11T23:59:45.051] WARNING: failed to connect to server: Timed out
[2026-03-11T23:59:46.136] INFO: stopping core process (desktop mode)
[2026-03-11T23:59:46.137] INFO: stopping core desktop process
[2026-03-11T23:59:46.138] WARNING: desktop process exited with code: 9

---

### 🤖 Claude

The log shows **only "Timed out"** — this is purely a **Windows firewall** issue, not TLS. The connection never even reaches Windows to do a TLS handshake.

**On Windows, run this in Command Prompt as Administrator:**

```
netstat -an | findstr 24800
```

If it shows **nothing** → Deskflow is not started on Windows. Click **Start** in Windows Deskflow.

If it shows **LISTENING** → firewall is blocking. Run this as Administrator:

```
netsh advfirewall firewall add rule name="Deskflow" dir=in action=allow protocol=TCP localport=24800
```

---

Also on Windows, **temporarily turn off Windows Firewall completely** to test:
1. Search **"Windows Defender Firewall"**
2. Click **"Turn Windows Defender Firewall on or off"**
3. Turn it **OFF** for Private network
4. Try connecting from Linux

If it connects with firewall off → firewall rule is the fix. If still timeout → Deskflow isn't started on Windows.

---

### 🧑 You

in windows it is ok only in linux it is not working

---

### 🤖 Claude

The timeout is coming from Linux side — let's verify Linux can even reach Windows on that port:

```bash
nc -zv 192.168.9.1 24800
```

What does it say? Either `Connection refused`, `Connected`, or `Timed out`?

Also check if anything is blocking on Linux side:

```bash
sudo iptables -L -n | grep 24800
```

And confirm Windows IP is reachable at all:

```bash
ping -c 3 192.168.9.1
```

Paste the output — this will tell us exactly where the connection is dying.

---

### 🧑 You

[2026-03-12T00:01:10.259] INFO: starting client process (desktop mode)
[2026-03-12T00:01:10.260] INFO: running command: /app/bin/deskflow-core client
[2026-03-12T00:01:10.274] NOTE: configured 1 server address(es)
[2026-03-12T00:01:10.275] INFO: using legacy x windows screen
initial settings file: /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf
[2026-03-12T00:01:10.342] NOTE: started client
[2026-03-12T00:01:10.342] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-12T00:01:11.882] INFO: stopping core process (desktop mode)
[2026-03-12T00:01:11.882] INFO: stopping core desktop process
[2026-03-12T00:01:11.884] WARNING: desktop process exited with code: 9
[2026-03-12T00:01:55.897] INFO: starting client process (desktop mode)
[2026-03-12T00:01:55.897] INFO: running command: /app/bin/deskflow-core client
[2026-03-12T00:01:55.906] NOTE: configured 1 server address(es)
[2026-03-12T00:01:55.906] INFO: using legacy x windows screen
initial settings file: /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf
[2026-03-12T00:01:55.950] NOTE: started client
[2026-03-12T00:01:55.950] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-12T00:01:57.973] WARNING: failed to connect to server: Timed out
[2026-03-12T00:01:58.993] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-12T00:02:01.014] WARNING: failed to connect to server: Timed out
[2026-03-12T00:02:01.676] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-12T00:02:03.983] WARNING: failed to connect to server: Timed out
[2026-03-12T00:02:05.002] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-12T00:02:06.989] WARNING: failed to connect to server: Timed out
[2026-03-12T00:02:08.007] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-12T00:02:08.828] INFO: stopping core process (desktop mode)
[2026-03-12T00:02:08.828] INFO: stopping core desktop process
[2026-03-12T00:02:08.830] WARNING: desktop process exited with code: 9

---

### 🤖 Claude

Run these diagnostic commands first:

```bash
ping -c 3 192.168.9.1
nc -zv 192.168.9.1 24800
```

Paste the output. This tells us if Linux can reach Windows at all, and if port 24800 is open. Without this I can't tell if it's a network issue or a Deskflow issue.

---

### 🧑 You

~ on  main [⇡] is  v1.0.0 via 寧 v1.3.10 via  v3.10.12  ❯ ping -c 3 192.168.9.1 nc -zv 192.168.9.1 24800 PING 192.168.9.1 (192.168.9.1) 56(84) bytes of data. --- 192.168.9.1 ping statistics --- 3 packets transmitted, 0 received, 100% packet loss, time 2030ms

---

### 🤖 Claude

**100% packet loss** — Linux cannot reach Windows at all! The two machines are on **different subnets**:

- Linux IP: `192.168.29.215` (subnet `192.168.29.x`)
- Windows IP: `192.168.9.1` (subnet `192.168.9.x`)

They're on different networks so they can't talk to each other. That's why nothing has worked.

**Check on Windows — run in Command Prompt:**
```
ipconfig
```

Look for the **WiFi adapter** IPv4 address. It should start with `192.168.29.x` to match Linux. What does it show?

The `192.168.9.1` might actually be your **router/hotspot IP**, not your Windows machine's IP.

---

### 🧑 You

1 server address(es)
[2026-03-12T00:08:18.377] INFO: using legacy x windows screen
initial settings file: /home/sunny77/.var/app/org.deskflow.deskflow/config/Deskflow/Deskflow.conf
[2026-03-12T00:08:18.415] NOTE: started client
[2026-03-12T00:08:18.415] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-12T00:08:20.439] WARNING: failed to connect to server: Timed out
[2026-03-12T00:08:21.459] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-12T00:08:22.671] WARNING: failed to connect to server: Timed out
[2026-03-12T00:08:23.693] IPC: connecting to '192.168.9.1': 192.168.9.1:24800
[2026-03-12T00:08:24.420] INFO: stopping core process (desktop mode)
[2026-03-12T00:08:24.420] INFO: stopping core desktop process
[2026-03-12T00:08:24.421] WARNING: desktop process exited with code: 9

---

### 🤖 Claude

Run `ipconfig` on Windows and find the correct IP. What does it show for WiFi adapter?

Also run this on Linux to find Windows IP automatically:

```bash
ip neigh show | grep -v FAILED
```

This shows all devices Linux can see on the network — your Windows machine's real IP will be in this list.

---
