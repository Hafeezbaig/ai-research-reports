from fpdf import FPDF
import os
import unicodedata

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "AI Research Report", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(33, 33, 33)
        self.multi_cell(0, 10, sanitize_text(title))
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 8, sanitize_text(body))
        self.ln(5)

def sanitize_text(text):
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

def generate_pdf(summary_text, filename="output/report.pdf"):
    pdf = PDF()
    pdf.add_page()

    sections = summary_text.split("### ")
    for section in sections:
        if not section.strip():
            continue
        lines = section.strip().split("\n", 1)
        title = lines[0]
        body = lines[1] if len(lines) > 1 else ""
        pdf.chapter_title(title.strip())
        pdf.chapter_body(body.strip())

    os.makedirs("output", exist_ok=True)
    pdf.output(filename)
    return filename
