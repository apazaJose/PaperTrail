# domain/entities/imagenProcessor/OCRProcessor.py
import pytesseract
from PIL import Image


class OCRProcessor:
    def __init__(self, tesseract_cmd=None):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_text(self, image_path: str) -> str:
        """
        Extrae texto de una imagen usando Tesseract OCR.
        """
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image, lang='spa')
            return text
        except Exception as e:
            raise ValueError(f"Error procesando la imagen: {e}")

    def extract_text_image(self, image) -> str:
        """
        Extrae texto de una imagen usando Tesseract OCR.
        """
        try:
            text = pytesseract.image_to_string(image, lang='spa')
            return text
        except Exception as e:
            raise ValueError(f"Error procesando la imagen: {e}")
