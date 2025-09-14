import fitz  # PyMuPDF

def convert_pdf_to_html(pdf_path, output_path):
    try:
        doc = fitz.open(pdf_path)
        html_content = ""
        for page in doc:
            html_content += page.get_text("html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"<html><body>{html_content}</body></html>")
        doc.close()
        return output_path
    except Exception as e:
        raise ValueError(f"Conversion failed: {e}")

# Usage
import os
pdf_folder = "pdf"
output_folder = "output"
convert_pdf_to_html(os.path.join(pdf_folder, "a.pdf"), os.path.join(output_folder, "a.html"))