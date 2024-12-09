# application/services/ImageOCRService.py
from src.domain.entities.imagenProcessor.OcrProcessor  import OCRProcessor
from src.shared.OpenCv.ProcessImage import preprocess_image

class ImageOCRService:
    def __init__(self, ocr_processor: OCRProcessor):
        self.ocr_processor = ocr_processor

    def extract_text_from_processed_image(self, image_path: str) -> str:
        """
        Procesa y extrae texto de una imagen.
        """
        try:
            # Preprocesa la imagen (si es necesario) cambiar esto para integrar lo que hizo josé
            processed_image_path = preprocess_image(image_path)

            # Extrae texto usando OCR
            text = self.ocr_processor.extract_text(processed_image_path)
            return text
        except Exception as e:
            raise ValueError(f"Error en el servicio de OCR: {e}")


    def extract_text_from_processed_image2(self, image) -> str:
        """
        Procesa y extrae texto de una imagen.
        """
        try:
            # Extrae texto usando OCR
            text = self.ocr_processor.extract_text_image(image)
            return text
        except Exception as e:
            raise ValueError(f"Error en el servicio de OCR: {e}")