from docx import Document
from fpdf import FPDF
import os
import glob

def convert_docx_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(pdf_path)

def convert_docx_to_md(docx_path, md_path):
    doc = Document(docx_path)
    with open(md_path, "w") as md_file:
        for para in doc.paragraphs:
            md_file.write(para.text + "\n\n")

if __name__ == "__main__":
    for docx_file in glob.glob("*.docx"):
        pdf_file = docx_file.replace(".docx", ".pdf")
        md_file = "README.md"
        convert_docx_to_pdf(docx_file, pdf_file)
        convert_docx_to_md(docx_file, md_file)
