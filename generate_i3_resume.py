#!/usr/bin/env python3
"""Generate BEST ATS-optimized resume for i3systems Data Annotator role."""
from fpdf import FPDF

class ResumePDF(FPDF):
    def section_title(self, title):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.5)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def entry_header(self, title, date):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(0, 0, 0)
        w = self.get_string_width(date)
        self.cell(self.w - self.l_margin - self.r_margin - w, 5, title)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(80, 80, 80)
        self.cell(w, 5, date, new_x="LMARGIN", new_y="NEXT")

    def entry_sub(self, text):
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")

    def bullet(self, text):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 30, 30)
        x = self.get_x()
        self.cell(5, 5, "-")
        self.multi_cell(self.w - self.l_margin - self.r_margin - 5, 5, text, new_x="LMARGIN", new_y="NEXT")

    def skill_row(self, cat, val):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(0, 0, 0)
        self.cell(32, 5, cat)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5, val, new_x="LMARGIN", new_y="NEXT")


pdf = ResumePDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_margins(20, 15, 20)

# ============ HEADER ============
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 8, "AZAD MUMTAZ ANSARI", align="C", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(60, 60, 60)
pdf.cell(0, 6, "+91 7208434724  |  ansariazadcs232421@gmail.com  |  Mumbai, India", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 5, "github.com/ansariazad  |  linkedin.com/in/azad-ansari-902035297  |  ansariazad.github.io", align="C", new_x="LMARGIN", new_y="NEXT")

pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.8)
pdf.line(20, pdf.get_y()+3, pdf.w-20, pdf.get_y()+3)
pdf.ln(6)

# ============ OBJECTIVE ============
pdf.section_title("Career Objective")
pdf.set_font("Helvetica", "", 9.5)
pdf.set_text_color(30, 30, 30)
pdf.multi_cell(0, 5,
    "Detail-oriented Computer Science graduate with strong analytical skills and hands-on experience in "
    "AI systems, data processing, and quality assurance. Seeking a Data Annotator role at i3systems to "
    "leverage my understanding of AI/ML data pipelines, document processing, and precision-driven work "
    "ethic to deliver high-quality training data for insurance automation models.",
    new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)

# ============ EXPERIENCE ============
pdf.section_title("Professional Experience")

pdf.entry_header("Operations Associate", "Feb 2024 - Nov 2025")
pdf.entry_sub("DMart (Avenue Supermarts Ltd) - Mumbai, India")
pdf.bullet("Processed 500+ daily transactions with 0% error rate, demonstrating exceptional attention to detail")
pdf.bullet("Managed data entry across billing systems ensuring 100% database integrity under strict SOPs")
pdf.bullet("Classified and categorized 50+ product categories with consistent labeling standards")
pdf.bullet("Resolved data discrepancies through systematic verification and quality auditing")
pdf.ln(2)

pdf.entry_header("Research & Data Intelligence Specialist", "Dec 2025 - Present")
pdf.entry_sub("Independent - Mumbai, India")
pdf.bullet("Structured large datasets applying consistent tagging and classification methodologies")
pdf.bullet("Designed tracking dashboards for competitor metrics and market intelligence")
pdf.ln(3)

# ============ PROJECTS ============
pdf.section_title("Technical Projects (AI & Data)")

pdf.entry_header("AutoShorts - AI Content Engine with Data Validation", "Python, Groq, SQLite")
pdf.bullet("Built quality validation engine scoring AI-generated content against 10+ criteria")
pdf.bullet("Designed deduplication system that classifies and tags content preventing repetition")
pdf.bullet("Demonstrates understanding of how training data quality impacts AI model performance")
pdf.ln(2)

pdf.entry_header("ClawBot - AI Agent with Intent Classification", "Python, LLM, Telegram API")
pdf.bullet("Classifies user intents and maps them to 32+ tool categories - annotation-like logic")
pdf.bullet("Designed JSON-structured data pipelines for organizing and labeling tool responses")
pdf.ln(2)

pdf.entry_header("TaskFlow - Production REST API", "FastAPI, JWT, SQLite, Docker")
pdf.bullet("Built API with strict data validation, type checking, and structured error handling")
pdf.ln(3)

# ============ SKILLS ============
pdf.section_title("Skills")
pdf.skill_row("Data:", "Data Labeling, Classification, Tagging, Annotation, Quality Assurance, Data Validation, Pattern Recognition")
pdf.skill_row("Languages:", "Python, JavaScript, SQL, Bash, HTML/CSS")
pdf.skill_row("AI/ML:", "LLM Prompt Engineering, AI Data Pipelines, Document Processing, NLP, Content Classification")
pdf.skill_row("Tools:", "Git, GitHub, Docker, VS Code, Google Sheets, Excel (Pivot Tables, VLOOKUP)")
pdf.skill_row("Database:", "SQLite, MySQL, PostgreSQL - Data Storage, Querying, Filtering, Structured Data")
pdf.skill_row("Soft Skills:", "Attention to Detail, Analytical Thinking, Independent Work, Fast Learning, Team Collaboration")
pdf.ln(3)

# ============ EDUCATION ============
pdf.section_title("Education")
pdf.entry_header("Bachelor of Science (BSc) - Computer Science", "2023 - 2026")
pdf.entry_sub("Sheth L.U.J College of Arts & Sir M.V. College of Science & Commerce, Mumbai University")
pdf.ln(1)
pdf.entry_header("HSC (12th) - Science", "2022")
pdf.entry_sub("V.P.M.'s Valia College of Arts, Commerce & Science, Mumbai")
pdf.ln(3)

# ============ ADDITIONAL ============
pdf.section_title("Additional Information")
pdf.skill_row("Languages:", "English (Professional), Hindi (Fluent), Marathi (Native)")
pdf.skill_row("Open Source:", "11 public GitHub repositories with 200+ commits - github.com/ansariazad")
pdf.skill_row("Portfolio:", "ansariazad.github.io - 8 live projects with source code and documentation")
pdf.skill_row("Available:", "Immediate joiner - Available for rotating shifts at Marol, Mumbai office")

pdf.output("/Users/azad/Desktop/Modify/Azad_Ansari_Resume_i3systems.pdf")
print("ATS Resume PDF saved!")
