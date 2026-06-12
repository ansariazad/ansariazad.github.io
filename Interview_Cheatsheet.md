# 🧠 Interview Cheat Sheet — Quick Reference Before Any Call

> **Print this. Read it 15 minutes before every interview.**

---

## Your Elevator Pitch (30 sec — memorize this)

> "I'm Azad, an AI Automation Engineer from Mumbai. I build autonomous systems that run without human input. My AI content engine generates and publishes 4 YouTube videos a day — fully autonomously. My AI agent has 32 tools and controls an entire Mac through Telegram messages. I work with Python, LLMs, FastAPI, and full-stack tech. I'm looking for a role at a startup or AI company where I can build production agent systems. I can start immediately."

---

## Your 5 Key Stories (memorize the headlines)

| # | Story | Use For |
|:-:|-------|---------|
| 1 | **AutoShorts** — "Built an AI pipeline that generates 4 YouTube videos/day autonomously. LLM script → quality gate → TTS → FFmpeg → YouTube upload. Zero human input." | Technical depth, AI, automation, system design |
| 2 | **ClawBot** — "Built an AI agent with 32+ tools. Send it a Telegram message, it chains tools together and executes. Multi-tool chaining, security layer, persistent memory." | AI agents, tool calling, architecture |
| 3 | **TaskFlow** — "Production REST API with JWT auth including refresh token rotation, RBAC, filtering, pagination, auto-generated Swagger docs." | Backend, API design, auth systems |
| 4 | **EAHP** — "Emergency ambulance portal with real-time GPS tracking, admin dashboard, RBAC. Migrated from PHP to Next.js + Supabase." | Full-stack, migration, real-world impact |
| 5 | **DMart** — "Processed 500+ daily transactions with 0% error rate. A billing discrepancy happened during peak hours — I suggested logging every discrepancy with timestamps, which helped IT fix the root cause in 2 hours instead of a full day." | Teamwork, problem-solving, data thinking |

---

## Common Questions — Quick Answers

### "Tell me about yourself"
→ Use the elevator pitch above.

### "Why AI?"
→ "I saw the gap between what LLMs can do and how companies use them. Most teams use ChatGPT as a chatbot. I build systems where the LLM decides which tools to use and executes autonomously."

### "Where do you see yourself in 3 years?"
→ "Senior AI engineer or tech lead owning the architecture of an agent platform. Eventually want to build my own AI SaaS product."

### "Biggest weakness?"
→ "I sometimes over-engineer. Built refresh token rotation in TaskFlow before having a single user. AutoShorts taught me to ship MVP first, iterate later."

### "Why should we hire you?"
→ "Most candidates at my level have tutorial projects. I have production systems running right now. AutoShorts generates videos autonomously. ClawBot has 32 real tools I use daily. I ship."

### "Salary expectations?"
→ "Based on the market for AI engineers, I'm looking at ₹[X]-[Y] LPA. But I'm more focused on the opportunity. Open to discussion."
→ Startup: ₹6-12 LPA | Remote US: $2-4K/month | Freelance: $15-25/hr

---

## Technical Quick Reference

### Python
- **Decorators:** Function that wraps another function. `@decorator` = `func = decorator(func)`. Use for logging, auth, retry.
- **Generators:** Lazy iteration with `yield`. Use for large datasets.
- **Async/Await:** Cooperative concurrency for I/O-bound. GIL prevents true CPU parallelism.
- **GIL:** Only one thread executes Python bytecode. Use multiprocessing for CPU-bound.

### FastAPI
- **Depends():** Dependency injection. Resolves before endpoint runs.
- **Middleware:** Processes every request/response. CORS, logging, timing.
- **BackgroundTasks:** Run after response sent. For emails, webhooks.
- **Pydantic:** Auto-validation from type hints. 422 on failure.

### AI/LLM
- **RAG:** Chunk docs → embed → vector DB → similarity search → context to LLM.
- **Tool Calling:** LLM outputs JSON specifying function + params. Code executes. Result fed back.
- **Agent Loop:** Observe → Think → Act → Evaluate → Loop until done.
- **Hallucination Prevention:** RAG grounding, quality gates, structured output, low temperature.

---

## Questions to Ask THEM

1. "What's the biggest technical challenge your team is facing right now?"
2. "How does the team ship features? What does a typical sprint look like?"
3. "What does success look like in this role in the first 90 days?"
4. "What AI/ML infrastructure does the team use?"
5. "How large is the engineering team and what's the growth plan?"

---

## Pre-Interview Checklist

- [ ] Research the company — what they build, recent news, tech stack
- [ ] Find the interviewer on LinkedIn — their background, interests
- [ ] Open your portfolio (ansariazad.github.io/hire.html) in a tab
- [ ] Open your GitHub (github.com/ansariazad) in a tab
- [ ] Have AutoShorts + ClawBot repos ready to show
- [ ] Test your camera, mic, and internet
- [ ] Have water nearby
- [ ] Read this cheat sheet one more time
