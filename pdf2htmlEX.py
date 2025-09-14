import pypdf2htmlEX

def convert_pdf_to_html(pdf_path, output_path=None):
    try:
        pdf = pypdf2htmlEX.PDF(pdf_path)
        html = pdf.to_html()
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
        return html
    except Exception as e:
        raise ValueError(f"Conversion failed: {e}")

# Usage
convert_pdf_to_html("input.pdf", "output.html")