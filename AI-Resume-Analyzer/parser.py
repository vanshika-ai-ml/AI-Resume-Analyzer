import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text_from_pdf(uploaded_file):
    text = ""

    # Open PDF
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    # First try normal text extraction
    for page in pdf:
        page_text = page.get_text()
        text += page_text

    # If little/no text was extracted, use OCR
    if len(text.strip()) < 50:
        text = ""

        for page in pdf:
            # Render PDF page as image
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

            # Convert image bytes to PIL image
            image = Image.open(io.BytesIO(pix.tobytes("png")))

            # OCR
            page_text = pytesseract.image_to_string(image)

            text += page_text

    return text