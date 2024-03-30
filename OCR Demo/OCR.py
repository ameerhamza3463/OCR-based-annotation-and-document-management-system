import pdfplumber
import pytesseract
from PIL import Image
import pathlib

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = "../Tesseract/tesseract.exe"


# Function to perform OCR on an image and return the extracted text
def ocr_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)


# Function to extract text from a PDF file using OCR
def extract_text_from_pdf(pdf_file_path):
    with pdfplumber.open(pdf_file_path) as pdf:
        text = ""
        for page in pdf.pages:
            # Extract image from each page
            image_path = f"page_{page.page_number}.png"
            page.to_image().save(image_path, format="PNG")

            # Perform OCR on the image and append the extracted text to the result
            text += ocr_image(image_path)

            # Delete the temporary image file
            pathlib.Path(image_path).unlink()
    return text


# Path to the PDF file
pdf_file_path = "./sample.pdf"

# Extract text from the PDF file using OCR
pdf_text = extract_text_from_pdf(pdf_file_path)

# Print the extracted text
print(pdf_text)
