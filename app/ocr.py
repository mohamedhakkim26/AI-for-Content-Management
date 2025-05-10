
from PIL import Image
import pytesseract
import fitz 

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

def extract_text(file, file_type):
    if file_type == "application/pdf":
        return extract_text_from_pdf(file), "PDF"
    elif file_type.startswith("image"):
        return extract_text_from_image(file), "Image"
    else:
        return file.read().decode("utf-8"), "Text File"
