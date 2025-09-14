from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO
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
        
        # Create output buffer
        output_string = StringIO()
        
        # Set layout parameters for better formatting preservation
        laparams = LAParams(
            line_margin=0.3,
            word_margin=0.1,
            boxes_flow=0.5,
            detect_vertical=True,
            all_texts=True
        )
        
        # Convert PDF to HTML with formatting
        with open(pdf_path, 'rb') as fin:
            extract_text_to_fp(
                fin,
                output_string,
                output_type='html',
                laparams=laparams
            )
        
        # Add custom CSS for better formatting
        html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        div { margin-bottom: 1em; }
        table { border-collapse: collapse; width: 100%; }
        td, th { border: 1px solid #ddd; padding: 8px; }
        pre { white-space: pre-wrap; }
    </style>
</head>
<body>
{}
</body>
</html>
"""
        
        # Write formatted HTML to file
        with open(output_path, "w", encoding="utf-8") as fout:
            output_string.seek(0)
            content = output_string.getvalue()
            fout.write(html_template.format(content))
            
        print(f"Successfully converted '{pdf_path}' to '{output_path}'")
        
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        raise

# Example usage with absolute path
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_folder = os.path.join(current_dir, "pdf")
pdf_path = os.path.join(pdf_folder, "b.pdf")
convert_pdf_to_html(pdf_path)
