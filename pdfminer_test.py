from pdfminer.high_level import extract_text_to_fp
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
        
        # Create StringIO object without encoding specification
        output_string = StringIO()
        
        # Convert PDF to HTML
        with open(pdf_path, 'rb') as fin:
            extract_text_to_fp(fin, output_string, output_type='html', codec=None)
        
        # Write the HTML content to file
        with open(output_path, "w", encoding="utf-8") as fout:
            output_string.seek(0)  # Reset the StringIO cursor to beginning
            fout.write(output_string.getvalue())
            
        print(f"Successfully converted '{pdf_path}' to '{output_path}'")
        
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        raise  # Re-raise the exception for debugging

# Example usage with absolute path
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_folder = os.path.join(current_dir, "pdf")
pdf_path = os.path.join(pdf_folder, "b.pdf")
convert_pdf_to_html(pdf_path)