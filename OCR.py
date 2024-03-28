import pdfplumber
import pytesseract

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file_path):
    with pdfplumber.open(pdf_file_path) as pdf:
        text = ''
        for page in pdf.pages:
            # Extract text from each page
            text += page.extract_text()
    return text

# Path to the PDF file
pdf_file_path = 'WebDevelopmentIBMCourseraCertificate.pdf'

# Extract text from the PDF file
pdf_text = extract_text_from_pdf(pdf_file_path)

# Perform OCR on the extracted text
ocr_text = pytesseract.image_to_string(pdf_text)

print(ocr_text)
