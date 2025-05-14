from docx2pdf import convert
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
    """Convert DOCX to PDF using docx2pdf"""
    try:
        convert(docx_path, pdf_path)
        return True
    except Exception as e:
        print(f"Error converting {docx_path} to PDF: {str(e)}")
        return False

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
    
def convert_latex_to_md(tex_path, md_path):
    """Convert LaTeX content to Markdown with proper formatting"""
    try:
        with open(tex_path, 'r', encoding='utf-8') as tex_file:
            content = tex_file.readlines()

        md_content = []
        in_itemize = False
        
        for line in content:
            # Skip comments and LaTeX commands we don't need
            if line.strip().startswith('%') or any(cmd in line for cmd in [
                '\\documentclass', '\\usepackage', '\\input', '\\renewcommand',
                '\\setlist', '\\raggedright', '\\pagestyle'
            ]):
                continue
                
            # Handle section headers
            if '\\section*{' in line:
                section = line.split('{')[1].split('}')[0]
                md_content.append(f"\n## {section}\n")
                continue
                
            # Handle name (centerline with Huge)
            if '\\centerline{\\Huge' in line:
                name = line.split('\\Huge')[1].strip()[:-1]
                md_content.append(f"# {name}\n\n")
                continue
                
            # Handle contact information
            if '\\centerline{\\href' in line:
                line = line.replace('\\centerline{', '').replace('}', '')
                links = line.split('|')
                formatted_links = []
                for link in links:
                    if '\\href{' in link:
                        url = link.split('\\href{')[1].split('}')[0]
                        text = link.split('}{')[1].split('}')[0]
                        formatted_links.append(f"[{text}]({url})")
                    else:
                        formatted_links.append(link.strip())
                md_content.append(' | '.join(formatted_links) + '\n')
                continue
                
            # Handle bold text
            if '\\textbf{' in line:
                line = line.replace('\\textbf{', '**').replace('}', '**')
                if '\\hfill' in line:
                    parts = line.split('\\hfill')
                    line = f"{parts[0].strip()} | {parts[1].strip()}\n"
                md_content.append(line)
                continue
                
            # Handle itemize environment
            if '\\begin{itemize}' in line:
                in_itemize = True
                continue
            elif '\\end{itemize}' in line:
                in_itemize = False
                md_content.append('\n')
                continue
                
            # Handle items in lists
            if '\\item' in line and in_itemize:
                item_text = line.replace('\\item', '').strip()
                md_content.append(f"- {item_text}\n")
                continue
                
            # Skip spacing commands
            if '\\vspace' in line or line.strip() == '':
                continue
                
            # Add any remaining text
            if line.strip():
                md_content.append(line.strip() + '\n')

        # Write to README.md
        with open(md_path, 'w', encoding='utf-8') as md_file:
            md_file.write(''.join(md_content))
            
        return True
    except Exception as e:
        print(f"Error converting {tex_path} to Markdown: {str(e)}")
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