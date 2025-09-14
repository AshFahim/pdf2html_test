import pdfplumber
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
        html_content.append("<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<title>PDF to HTML</title>\n<style>\nbody { font-family: sans-serif; margin: 20px; }\n.page { margin-bottom: 20px; border: 1px solid #eee; padding: 15px; }\n.text-block { margin-bottom: 10px; }\n.image-container { text-align: center; margin: 10px 0; }\nimg { max-width: 100%; height: auto; border: 1px solid #ddd; }\n</style>\n</head>\n<body>")

        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                html_content.append(f'<div class="page" id="page-{i+1}">')
                html_content.append(f'<h2>Page {i+1}</h2>')

                # Extract text
                text = page.extract_text()
                if text:
                    html_content.append('<div class="text-block">')
                    html_content.append(f'<pre>{text}</pre>') # Use pre to preserve whitespace
                    html_content.append('</div>')

                html_content.append('</div>')  # Close page div
            
            # Add closing tags for HTML
            html_content.append('</body>\n</html>')
            
            # Write to file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(html_content))
            
            return output_path
            
    except Exception as e:
        print(f"Error converting PDF: {str(e)}")
        return None 
    
    
result = convert_pdf_to_html('pdf/a.pdf')
if result:
    print(f"HTML file created at: {result}")
else:
    print("Conversion failed.")