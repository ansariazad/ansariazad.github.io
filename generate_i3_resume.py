#!/usr/bin/env python3
"""Generate 1-PAGE ATS resume for i3systems Data Annotator."""
from fpdf import FPDF

class ResumePDF(FPDF):
    def section_title(self, title):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(0, 0, 0)
        self.cell(0, 5, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.4)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(2)

    def entry_header(self, title, date):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(0, 0, 0)
        w = self.get_string_width(date)
        self.cell(self.w - self.l_margin - self.r_margin - w, 4.5, title)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(80, 80, 80)
        self.cell(w, 4.5, date, new_x="LMARGIN", new_y="NEXT")

    def entry_sub(self, text):
        self.set_font("Helvetica", "I", 8.5)
        self.set_text_color(80, 80, 80)
        self.cell(0, 4, text, new_x="LMARGIN", new_y="NEXT")

    def bullet(self, text):
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(30, 30, 30)
        self.cell(4, 4, "-")
        self.multi_cell(self.w - self.l_margin - self.r_margin - 4, 4, text, new_x="LMARGIN", new_y="NEXT")

    def skill_row(self, cat, val):
        self.set_font("Helvetica", "B", 8.5)
        self.set_text_color(0, 0, 0)
        self.cell(28, 4, cat)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(30, 30, 30)
        self.cell(0, 4, val, new_x="LMARGIN", new_y="NEXT")


pdf = ResumePDF()
pdf.set_auto_page_break(auto=False)
pdf.add_page()
pdf.set_margins(16, 12, 16)
pdf.set_y(12)

# ── HEADER ──
pdf.set_font("Helvetica", "B", 18)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 7, "AZAD MUMTAZ ANSARI", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(60, 60, 60)
pdf.cell(0, 4.5, "+91 7208434724  |  ansariazadcs232421@gmail.com  |  Mumbai, India", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 4.5, "github.com/ansariazad  |  linkedin.com/in/azad-ansari-902035297  |  ansariazad.github.io", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.6)
pdf.line(16, pdf.get_y()+2, pdf.w-16, pdf.get_y()+2)
pdf.ln(4)

# ── OBJECTIVE ──
pdf.section_title("Objective")
pdf.set_font("Helvetica", "", 8.5)
pdf.set_text_color(30, 30, 30)
pdf.multi_cell(0, 4,
    "Detail-oriented CS graduate with hands-on AI experience and 0% error rate in data processing. "
    "Seeking Data Annotator role at i3systems to deliver high-quality training data for insurance AI models.",
    new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

# ── EXPERIENCE ──
pdf.section_title("Experience")

pdf.entry_header("Operations Associate - DMart (Avenue Supermarts Ltd)", "Feb 2024 - Nov 2025")
pdf.entry_sub("Mumbai, India")
pdf.bullet("Processed 500+ daily transactions with 0% error rate - exceptional attention to detail")
pdf.bullet("Classified products across 50+ categories with consistent labeling; 100% database integrity")
pdf.bullet("Resolved data discrepancies through systematic verification and quality auditing")
pdf.ln(1)

pdf.entry_header("Research & Data Intelligence Specialist", "Dec 2025 - Present")
pdf.bullet("Structured large datasets with consistent tagging, classification, and dashboard reporting")
pdf.ln(2)

# ── PROJECTS ──
pdf.section_title("AI & Data Projects")

pdf.entry_header("AutoShorts - AI Pipeline with Data Validation", "Python, Groq AI, SQLite")
pdf.bullet("Built validation engine scoring content against 10+ quality criteria; deduplication via classification/tagging")
pdf.ln(1)

pdf.entry_header("ClawBot - AI Agent (32+ Tools)", "Python, LLM, Telegram API")
pdf.bullet("Classifies user intents into 32+ tool categories; JSON-structured labeling of tool responses")
pdf.ln(1)

pdf.entry_header("TaskFlow - Production REST API", "FastAPI, JWT, Docker")
pdf.bullet("Strict data validation, type checking, structured error handling - data quality focus")
pdf.ln(2)

# ── SKILLS ──
pdf.section_title("Skills")
pdf.skill_row("Data:", "Data Labeling, Classification, Tagging, Annotation, QA, Pattern Recognition, OCR Verification")
pdf.skill_row("Code:", "Python, JavaScript, SQL, Bash, HTML/CSS")
pdf.skill_row("AI/ML:", "LLM Prompt Engineering, AI Data Pipelines, NLP, Document Processing, IDP")
pdf.skill_row("Tools:", "Git, GitHub, Docker, VS Code, Excel (Pivot Tables, VLOOKUP), Google Sheets")
pdf.skill_row("DB:", "SQLite, MySQL, PostgreSQL - Querying, Filtering, Structured Data")
pdf.skill_row("Soft:", "Attention to Detail, Analytical Thinking, Fast Learning, Independent Work")
pdf.ln(2)

# ── EDUCATION ──
pdf.section_title("Education")
pdf.entry_header("BSc Computer Science - Mumbai University", "2023 - 2026")
pdf.entry_sub("Sheth L.U.J College of Arts & Sir M.V. College of Science & Commerce")
pdf.ln(1)
pdf.entry_header("HSC (12th) Science", "2022")
pdf.entry_sub("V.P.M.'s Valia College, Mumbai")
pdf.ln(2)

# ── ADDITIONAL ──
pdf.section_title("Additional")
pdf.skill_row("Lang:", "English (Professional), Hindi (Fluent), Marathi (Native)")
pdf.skill_row("GitHub:", "11 public repos, 200+ commits - github.com/ansariazad")
pdf.skill_row("Ready:", "Immediate joiner | Rotating shifts OK | Marol, Mumbai")

pdf.output("/Users/azad/Desktop/Modify/Azad_Ansari_Resume_i3systems.pdf")
print("1-PAGE ATS Resume saved!")
