from pdfminer.high_level import extract_text
import sys

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        return extract_text(pdf_path)
    except Exception as e:
        return f"Failed to extract text: {e}"

if __name__ == "__main__":
    pdf_file = "test.pdf"
    
    if len(sys.argv) > 1:
        pdf_file = sys.argv[1]

    extracted_text = extract_text_from_pdf(pdf_file)
    print("Extracted Text:\n", extracted_text)

