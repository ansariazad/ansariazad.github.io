# LinkedIn Profile — Copy-Paste Guide (AI Automation Engineer Edition)

## Headline (220 chars max)
```
AI Automation Engineer | Building Autonomous LLM Agents & Production AI Pipelines | Python · FastAPI · LangChain · RAG | Open to AI/Backend/Founding Engineer Roles
```

## About Section
```
I build AI systems that think, decide, and act — without human babysitting.

My AutoShorts engine generates YouTube content autonomously: an LLM writes the script, a 5-dimension quality gate validates it, Edge-TTS synthesizes the voiceover, FFmpeg assembles the video, and the YouTube API publishes it. It processes 4 videos a day. I haven't touched it in weeks.

My ClawBot agent controls my MacBook through Telegram messages. It has 32+ tools — from sending WhatsApp messages to tracking crypto prices to managing files. I give it a sentence; it chains multiple tools together and executes. It replaced 10 separate apps.

The stack behind both: Python, Groq/Ollama LLMs, tool-calling architectures with JSON reasoning, SQLite for state, cron for scheduling, and Docker for deployment.

Beyond AI, I build full-stack products. EAHP is an emergency ambulance platform with real-time GPS tracking, admin dashboards, and RBAC — built with Next.js 16 and Supabase. TaskFlow is a production REST API with JWT auth, refresh tokens, filtering, and auto-generated OpenAPI docs.

I care about shipping things that work. Every project in my portfolio is deployed, functional, and production-grade — not a tutorial clone.

🔧 Stack: Python, FastAPI, LangChain, Groq, React, Next.js, PostgreSQL, Docker, Git
📍 Mumbai, India | BSc Computer Science, University of Mumbai (2026)

Open to full-time AI / Python / Backend / Founding Engineer roles — immediate joiner.
Let's connect: ansariazadcs232421@gmail.com
```

## Experience Entries

### Entry 1: AI Automation Engineer (Self-Directed)
**Company:** AutoShorts Project
**Duration:** 2025 — Present
**Description:**
```
Engineered a fully autonomous AI content pipeline that generates, validates, and publishes YouTube Shorts with zero human intervention — currently processing 4 videos/day in production.

• Designed end-to-end pipeline: Groq LLM script generation → 5-dimension quality validation → Edge-TTS voice synthesis → FFmpeg video assembly → YouTube Data API v3 upload
• Built SQLite deduplication engine with 60-day topic cooldown and 30-day clip rotation, preventing content repetition across 500+ generated assets
• Deployed cron-scheduled automation with jittered upload times to mimic organic posting behavior

Tech: Python, Groq API, Ollama, Edge-TTS, FFmpeg, YouTube Data API v3, Pexels API, SQLite
```

### Entry 2: AI Agent Developer (Self-Directed)
**Company:** ClawBot Project
**Duration:** 2026
**Description:**
```
Built an autonomous AI agent with 32+ integrated tools that controls macOS through natural language commands via Telegram — replacing 10+ separate applications.

• Designed LLM-powered tool-calling architecture with JSON-structured reasoning and multi-tool chaining
• Integrated real-time crypto/stock monitoring (CoinGecko, Yahoo Finance), WhatsApp messaging, and macOS AppleScript automation
• Implemented security layer with dangerous-command detection, owner-only confirmation flows, persistent SQLite memory

Tech: Python, Groq LLM, Telegram Bot API, AppleScript, CoinGecko API, Yahoo Finance API
```

### Entry 3: Full-Stack Developer (Self-Directed)
**Company:** EAHP — Emergency Ambulance Hiring Portal
**Duration:** 2025
**Description:**
```
Developed full-stack emergency ambulance booking platform with real-time GPS tracking and admin dashboard.

• Built interactive Leaflet.js maps for live ambulance tracking with RBAC admin panel
• Developed booking analytics with Recharts and automated PDF receipt generation via jsPDF
• Migrated from PHP monolith to Next.js 16 + Supabase with auth middleware

Tech: Next.js 16, React 19, Supabase, Leaflet.js, Recharts, jsPDF, Framer Motion
```

### Entry 4: Operations Associate
**Company:** DMart (Avenue Supermarts Ltd)
**Duration:** Feb 2024 — Nov 2025
**Description:**
```
• Processed 500+ daily transactions with 0% error rate across high-frequency billing and inventory systems
• Maintained 100% database integrity across all transaction records following strict SOPs
• Resolved 50+ daily customer escalations under high-pressure retail scenarios
```

## Featured Section

**Item 1: AutoShorts — Autonomous AI Content Engine**
→ Link to GitHub repo
→ Description: AI pipeline that generates YouTube Shorts autonomously. LLM writes scripts, quality gate validates, TTS narrates, FFmpeg edits, YouTube API uploads. 4 videos/day, zero human input.

**Item 2: ClawBot — Autonomous AI Mac Agent**
→ Link to GitHub repo
→ Description: AI agent with 32+ tools controlling macOS via Telegram. Multi-tool reasoning chains, security layer, persistent memory.

**Item 3: Portfolio Website**
→ Link to ansariazad.github.io/hire.html
→ Description: Everything I've built in one place. Services, projects, contact.

**Item 4: TaskFlow API**
→ Link to GitHub repo
→ Description: Production REST API with JWT auth, token rotation, RBAC, filtering, pagination, auto-generated Swagger docs.

## Skills to Add on LinkedIn (in order of priority)
1. Python
2. Artificial Intelligence (AI)
3. Large Language Models (LLM)
4. FastAPI
5. REST APIs
6. Machine Learning
7. React.js
8. Docker
9. PostgreSQL
10. Git
11. Next.js
12. Prompt Engineering
13. JavaScript
14. SQL
15. Full-Stack Development

## First 3 Posts to Make

### Post 1: Introduction
```
🎓 BSc Computer Science — done.

But here's the thing — my real education happened while building production systems.

While studying, I shipped:
🤖 An AI engine that generates and publishes YouTube videos autonomously (4/day, zero human input)
🦾 An AI agent with 32+ tools that controls my Mac through Telegram
🚑 A full-stack emergency healthcare platform with real-time GPS tracking
⚡ A production REST API with JWT auth and auto-generated docs

No certificates. No bootcamps. Just curiosity + code + shipping to production.

Now looking for AI Engineer / Backend Engineer / Founding Engineer roles.

If you're hiring someone who builds production AI systems, not tutorial clones — let's talk.

#OpenToWork #AIEngineer #Python #LLMAgents #Automation
```

### Post 2: AutoShorts Deep Dive
```
I built an AI engine that generates YouTube Shorts autonomously. Here's how it works:

1️⃣ Groq LLM generates a script using my custom prompt framework
2️⃣ A 5-dimension quality gate validates it (factual accuracy, hook strength, length, relevance, originality)
3️⃣ If it fails validation → auto-reject + retry (max 3 attempts)
4️⃣ Edge-TTS synthesizes natural voiceover
5️⃣ Pexels API fetches relevant B-roll footage
6️⃣ FFmpeg assembles the final video — voiceover + visuals + captions
7️⃣ YouTube Data API uploads with optimized metadata
8️⃣ SQLite logs everything — 60-day topic cooldown prevents repetition

It runs 24/7 via cron. 4 videos per day. I haven't touched it in weeks.

The interesting part? The quality gate was the hardest engineering challenge. Not the AI — the validation.

What's the most complex pipeline you've built?

#AI #Python #Automation #LLM #YouTube
```

### Post 3: ClawBot Demo
```
I told my AI agent to "check Bitcoin price and if it's above $60K, WhatsApp my friend."

Here's what happened:

1. It called the crypto_price tool → got $67,432
2. It evaluated the condition → $67K > $60K ✓
3. It called whatsapp_send → sent the message
4. It returned: "Bitcoin is at $67,432. I've notified your friend via WhatsApp."

3 tools. 1 sentence. Fully autonomous.

ClawBot has 32+ tools:
🖥️ System control (volume, brightness, screenshots, apps)
💬 Messaging (WhatsApp, Telegram, email)
💰 Finance (crypto prices, stock monitoring, alerts)
📁 Files (create, read, move, search)
🌐 Web (search, scrape, download)
🔐 Security (dangerous command detection, owner confirmation)

The security layer is my favorite part. Some commands require explicit confirmation before execution. No AI agent should have unguarded access to system-level operations.

What would you automate with an agent like this?

#AIAgent #LLM #Python #Automation #ToolCalling
```

## Connection Request Templates

**To AI recruiters:**
```
Hi [Name], I'm Azad — an AI Automation Engineer from Mumbai. I build autonomous LLM agents and production AI pipelines. Would love to connect and learn about opportunities at [Company]. Portfolio: ansariazad.github.io
```

**To startup founders:**
```
Hey [Name] 👋 Saw [Company] is building [product] — excited about the approach. I'm an AI engineer who's shipped production agent systems (32+ tools, autonomous pipelines). Would love to chat if you're growing the team.
```

**To other engineers:**
```
Hi [Name], I'm building AI agents and automation systems in Python. Saw your work on [their project/post] — really cool. Would love to connect and exchange notes.
```

## Weekly Content Strategy

- **Monday:** Technical post (how I built something)
- **Tuesday:** Engage — comment on 5-10 AI/startup posts
- **Wednesday:** Share a demo (screenshot or video of ClawBot/AutoShorts)
- **Thursday:** Engage + send 10 connection requests
- **Friday:** Career insight or "what I learned" post
- **Saturday:** Short technical tip or hot take
- **Sunday:** Review metrics — connections, impressions, messages

**Goal: 4-5 posts per week. 50+ new connections per week.**
