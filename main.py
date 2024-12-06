from src.application.services.ImageOCRService import ImageOCRService
from src.application.services.TfidfExtractionService import TfidfExtractionService
from src.domain.entities.imagenProcessor.OcrProcessor import OCRProcessor

def main():
    # Configurar OCR con la ruta de Tesseract (si es necesario)
    tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ocr_processor = OCRProcessor(tesseract_cmd=tesseract_cmd)

    # Inicializar el servicio de OCR
    ocr_service = ImageOCRService(ocr_processor)

    # Ruta de la imagen a procesar
    image_path = r'C:\Users\Gustavo\Downloads\WhatsApp Image 2024-11-26 at 18.38.06.jpeg'

    # Extraer texto de la imagen usando OCR
    try:
        text = ocr_service.extract_text_from_processed_image(image_path)
        print("Texto extraído de la imagen:")
        print(text)
    except Exception as e:
        print(f"Error durante la extracción de texto: {e}")
        return

    # Inicializar el servicio de extracción de TF-IDF
    tfidf_service = TfidfExtractionService()

    # Extraer las características TF-IDF del texto procesado
    try:
        features = tfidf_service.extract(text)
        print("Características extraídas con TF-IDF:")
        for word, score in features.items():
            print(f"{word}: {score}")
    except Exception as e:
        print(f"Error durante la extracción de TF-IDF: {e}")

if __name__ == "__main__":
    main()
