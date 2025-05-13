from docx import Document
from fpdf import FPDF
import os
import glob
import subprocess
import shutil

# Define folder paths
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def ensure_folders_exist():
    """Create input and output folders if they don't exist"""
    for folder in [INPUT_FOLDER, OUTPUT_FOLDER]:
        if not os.path.exists(folder):
            os.makedirs(folder)

def convert_docx_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    
    # Replace unsupported characters with similar characters or remove them
    text = text.encode("latin-1", errors="replace").decode("latin-1")
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=11)  # Changed to Arial as it's more widely supported
    pdf.multi_cell(0, 10, text)
    pdf.output(pdf_path)

def convert_latex_to_pdf(tex_path, pdf_path):
    try:
        # Copy .tex file to current directory for processing
        temp_tex = os.path.basename(tex_path)
        shutil.copy2(tex_path, temp_tex)
        
        # Run pdflatex to convert .tex to .pdf
        subprocess.run(['pdflatex', temp_tex], check=True)
        
        # Move the generated PDF to output folder
        temp_pdf = os.path.splitext(temp_tex)[0] + '.pdf'
        if os.path.exists(temp_pdf):
            shutil.move(temp_pdf, pdf_path)
            
        # Clean up temporary files
        cleanup_latex_files(os.path.splitext(temp_tex)[0])
        os.remove(temp_tex)
        return True
    except subprocess.CalledProcessError:
        print(f"Error converting {tex_path} to PDF")
        return False

def cleanup_latex_files(basename):
    """Clean up auxiliary LaTeX files"""
    extensions = ['.aux', '.log', '.out']
    for ext in extensions:
        file_path = basename + ext
        if os.path.exists(file_path):
            os.remove(file_path)

def process_files():
    """Process all files in the input folder"""
    ensure_folders_exist()
    
    # Handle DOCX files
    for docx_file in glob.glob(os.path.join(INPUT_FOLDER, "*.docx")):
        filename = os.path.basename(docx_file)
        pdf_file = os.path.join(OUTPUT_FOLDER, filename.replace(".docx", ".pdf"))
        print(f"Converting {filename} to PDF...")
        convert_docx_to_pdf(docx_file, pdf_file)

    # Handle LaTeX files
    for tex_file in glob.glob(os.path.join(INPUT_FOLDER, "*.tex")):
        filename = os.path.basename(tex_file)
        pdf_file = os.path.join(OUTPUT_FOLDER, filename.replace(".tex", ".pdf"))
        print(f"Converting {filename} to PDF...")
        if convert_latex_to_pdf(tex_file, pdf_file):
            # Only update README.md for LaTeX files
            convert_latex_to_md(tex_file, "README.md")

if __name__ == "__main__":
    process_files()