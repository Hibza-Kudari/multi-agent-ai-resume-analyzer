import fitz
import easyocr
import numpy as np
from PIL import Image
import io

reader = easyocr.Reader(['en'])


def extract_text_from_pdf(pdf_file):

    pdf_bytes = pdf_file.read()

    pdf = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    text = ""

    # Try normal extraction first
    for page in pdf:
        text += page.get_text()

    # If normal extraction works, return it
    if len(text.strip()) > 50:
        return text

    print("Using OCR...")

    text = ""

    # Reopen PDF for OCR
    pdf = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    for page in pdf:

        pix = page.get_pixmap(
            matrix=fitz.Matrix(2, 2)
        )

        img_bytes = pix.tobytes("png")

        image = Image.open(
            io.BytesIO(img_bytes)
        )

        image_np = np.array(image)

        results = reader.readtext(
            image_np,
            detail=0
        )

        text += "\n".join(results)
        text += "\n"

    return text