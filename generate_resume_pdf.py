#!/usr/bin/env python3
"""Generate ATS-optimized resume PDF."""
from fpdf import FPDF

class ResumePDF(FPDF):
    def section_title(self, title):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(17, 17, 17)
        self.cell(0, 5, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(17, 17, 17)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(2)

    def entry_header(self, title, date):
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(17, 17, 17)
        w = self.get_string_width(date)
        self.cell(self.w - self.l_margin - self.r_margin - w, 4.5, title)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(100, 100, 100)
        self.cell(w, 4.5, date, new_x="LMARGIN", new_y="NEXT")

    def entry_sub(self, text):
        self.set_font("Helvetica", "I", 8.5)
        self.set_text_color(85, 85, 85)
        self.cell(0, 4, text, new_x="LMARGIN", new_y="NEXT")

    def bullet(self, text):
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(51, 51, 51)
        self.cell(4, 4, "-")
        self.multi_cell(0, 4, text, new_x="LMARGIN", new_y="NEXT")

    def skill_row(self, cat, val):
        self.set_font("Helvetica", "B", 8.5)
        self.set_text_color(17, 17, 17)
        self.cell(28, 4, cat)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(51, 51, 51)
        self.cell(0, 4, val, new_x="LMARGIN", new_y="NEXT")


pdf = ResumePDF()
pdf.set_auto_page_break(auto=True, margin=12)
pdf.add_page()
pdf.set_margins(18, 14, 18)

# ── HEADER ──
pdf.set_font("Helvetica", "B", 18)
pdf.set_text_color(17, 17, 17)
pdf.cell(0, 7, "AZAD MUMTAZ ANSARI", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 9.5)
pdf.set_text_color(68, 68, 68)
pdf.cell(0, 5, "Python Developer  |  AI Automation  |  Full-Stack Engineering", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 8)
pdf.set_text_color(85, 85, 85)
pdf.cell(0, 4, "+91 7208434724  |  ansariazadcs232421@gmail.com  |  Mumbai, India", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 4, "github.com/ansariazad  |  linkedin.com/in/azad-ansari-902035297  |  ansariazad.github.io", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_draw_color(17, 17, 17)
pdf.set_line_width(0.6)
pdf.line(18, pdf.get_y()+2, pdf.w-18, pdf.get_y()+2)
pdf.ln(5)

# ── SUMMARY ──
pdf.section_title("Summary")
pdf.set_font("Helvetica", "", 8.5)
pdf.set_text_color(51, 51, 51)
pdf.multi_cell(0, 4, "Results-driven Computer Science graduate with hands-on experience building and shipping production Python applications. Proficient in Git, Docker, and CI/CD pipelines. Maintain 11 public GitHub repositories with well-documented codebases. Built production-grade AI systems including an autonomous content pipeline and an LLM-powered agent with 32+ tools. Experienced in understanding, modifying, and testing complex codebases. Active open-source contributor.", new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

# ── EXPERIENCE ──
pdf.section_title("Professional Experience")

pdf.entry_header("Operations Associate - DMart (Avenue Supermarts Ltd)", "Feb 2024 - Nov 2025")
pdf.entry_sub("Mumbai, India")
pdf.bullet("Processed 500+ daily transactions with 0% error rate, maintaining complete database accuracy across billing systems")
pdf.bullet("Executed complex inventory and billing workflows following strict SOPs, ensuring 100% database integrity")
pdf.bullet("Resolved high-pressure customer and stakeholder queries, building strong analytical and communication skills")
pdf.ln(1)

pdf.entry_header("Research & Data Intelligence Specialist - Independent", "Dec 2025 - Present")
pdf.entry_sub("Mumbai, India")
pdf.bullet("Built structured research methodologies for identifying and qualifying digital assets and partnership opportunities")
pdf.bullet("Designed Google Sheets dashboards for tracking competitor metrics and delivering actionable market intelligence")
pdf.ln(2)

# ── PROJECTS ──
pdf.section_title("Technical Projects")

pdf.entry_header("AutoShorts - AI Content Automation Engine", "Python, Groq, FFmpeg, YouTube API")
pdf.bullet("Built fully autonomous pipeline: LLM script generation -> quality validation -> TTS synthesis -> video assembly -> YouTube upload")
pdf.bullet("Designed SQLite deduplication engine with topic/clip cooldowns; runs 4 videos/day with zero intervention")
pdf.bullet("Managed via Git version control with feature branches; deployed using Docker containers and cron-based CI/CD")
pdf.ln(1)

pdf.entry_header("ClawBot - Autonomous AI Mac Agent", "Python, LLM Agent, Telegram API")
pdf.bullet("Engineered AI agent with 32+ tools for system control, trading, messaging, and file management via Telegram")
pdf.bullet("Implemented LLM tool-calling architecture with JSON reasoning chain, multi-tool chaining, and security layer")
pdf.bullet("Wrote unit tests for tool handlers; managed complex multi-module codebase with Git branching workflow")
pdf.ln(1)

pdf.entry_header("EAHP - Emergency Ambulance Hiring Portal", "Next.js, React, Supabase, Leaflet.js")
pdf.bullet("Developed full-stack platform with real-time GPS tracking, admin RBAC dashboard, and PDF report generation")
pdf.bullet("Migrated legacy PHP/MySQL monolith to modern Next.js + Supabase stack with auth middleware")
pdf.ln(1)

pdf.entry_header("TaskFlow - Production REST API", "FastAPI, JWT, SQLite, Swagger")
pdf.bullet("Production REST API with JWT auth, token rotation, role-based access control, filtering, pagination, and OpenAPI docs")
pdf.ln(1)

pdf.entry_header("CryptoWatch - Crypto Dashboard", "Python, Flask, CoinGecko API")
pdf.bullet("Real-time dashboard tracking 50+ crypto assets with charts, portfolio calculator, and email price alerts")
pdf.ln(2)

# ── SKILLS ──
pdf.section_title("Technical Skills")
pdf.skill_row("Languages:", "Python, JavaScript, PHP, C#, SQL, Bash, HTML/CSS")
pdf.skill_row("AI:", "LLM Prompt Engineering, Groq API, Ollama, Edge-TTS, FFmpeg, AI Agents, n8n")
pdf.skill_row("Web:", "FastAPI, Flask, React.js, Next.js, REST API Design, Supabase, JWT Authentication")
pdf.skill_row("Databases:", "SQLite, MySQL, PostgreSQL (Supabase)")
pdf.skill_row("DevOps:", "Git, GitHub (11 public repos), Docker, CI/CD Pipelines, Cron Automation, VS Code, Vercel")
pdf.skill_row("Testing:", "pytest, Unit Testing, API Testing, Code Review, Complex Codebase Navigation")
pdf.skill_row("Office:", "Excel (Pivot Tables, VLOOKUP), Word, PowerPoint, Google Sheets")
pdf.skill_row("Soft:", "Problem Solving, Analytical Thinking, Technical Writing, Independent Remote Work")
pdf.ln(2)

# ── EDUCATION ──
pdf.section_title("Education")
pdf.entry_header("Bachelor of Science (BSc) in Computer Science", "2023 - 2026")
pdf.entry_sub("Sheth L.U.J College of Arts & Sir M.V. College of Science & Commerce, Mumbai")
pdf.ln(1)
pdf.entry_header("HSC (12th) - Science", "2022")
pdf.entry_sub("V.P.M.'s Valia College of Arts, Commerce & Science, Mumbai")
pdf.ln(2)

# ── ADDITIONAL ──
pdf.section_title("Additional")
pdf.skill_row("Languages:", "English (Professional), Hindi (Fluent), Marathi (Native)")
pdf.skill_row("Open Source:", "11 public GitHub repos - github.com/ansariazad | Active contributor with 200+ commits")
pdf.skill_row("Portfolio:", "ansariazad.github.io - 8 live projects with full source code and documentation")
pdf.skill_row("Available:", "Immediate joiner - Open to Full-time, Part-time, Remote, and Internship roles")

pdf.output("/Users/azad/Desktop/Modify/Azad_Ansari_Resume.pdf")
print("✅ Resume PDF saved!")
