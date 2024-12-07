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
    image_path = r'C:\Users\Gustavo\Downloads\verificador-de-facturas-del-SIN-9.png'

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
        most_frequent_words = tfidf_service.extract(text)
        #Mostrar solo las palabras con la fecuencia mas alta
        print("Palabras con la frecuencia más alta:")
        for word, score in most_frequent_words.items():
            print(f"{word}: {score}")
    except Exception as e:
        print(f"Error durante la extracción de TF-IDF: {e}")


if __name__ == "__main__":
    main()
