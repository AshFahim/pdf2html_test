import fitz # PyMuPDF
import sys
import os

def convert_pdf_to_html(pdf_path, output_folder="output"):
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Get the PDF filename without extension
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # Create output path with HTML extension
        output_path = os.path.join(output_folder, f"{pdf_name}.html")
        
        html_content = []
        # Add HTML header with CSS for better formatting
        html_content.append("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial, sans-serif; }
        .page { margin: 1em; padding: 1em; border-bottom: 1px solid #ddd; }
        pre { white-space: pre-wrap; }
        table { border-collapse: collapse; }
        td, th { border: 1px solid #ddd; padding: 8px; }
    </style>
</head>
<body>
""")
        
        with fitz.open(pdf_path) as doc:
            for page_num, page in enumerate(doc, 1):
                # Add page div for better structure
                html_content.append(f'<div class="page" id="page-{page_num}">')
                # Get page content with HTML formatting
                page_html = page.get_text("html")
                html_content.append(page_html)
                html_content.append('</div>')
        
        # Add HTML footer
        html_content.append("</body></html>")
        
        # Write complete HTML to file
        with open(output_path, "w", encoding="utf-8") as html_file:
            html_file.write("\n".join(html_content))
        
        print(f"Successfully converted '{pdf_path}' to '{output_path}'")
    
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

# Example usage:
pdf_folder = "pdf"  # Define the PDF folder path
convert_pdf_to_html(os.path.join(pdf_folder, "a.pdf"))