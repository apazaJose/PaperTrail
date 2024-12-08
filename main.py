from src.application.services.ImageOCRService import ImageOCRService
from src.application.services.TfidfExtractionService import TfidfExtractionService
from src.domain.entities.imagenProcessor.OcrProcessor import OCRProcessor
from src.application.services.WordFeature import tamaño_promedio_palabras, contar_lineas, contar_palabras, \
    contar_numeros, contar_fechas

def main():
    # Configurar OCR con la ruta de Tesseract (si es necesario)
    tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ocr_processor = OCRProcessor(tesseract_cmd=tesseract_cmd)

    # Inicializar el servicio de OCR
    ocr_service = ImageOCRService(ocr_processor)

    # Ruta de la imagen a procesar
    image_path = r'C:\Users\Gustavo\Pictures\Screenshots\Captura de pantalla 2024-12-07 202541.png'

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
        #Mostrar solo las palabras que retornadas en forma de diccionario
        print("Palabras con la frecuencia más alta:")
        for word, score in most_frequent_words.items():
            print(f"{word}: {score}")
        print("Caracteristicas nuevas")
        print(f"Lineas de texto presentes: {contar_lineas(text)}")
        print(f"Tamaño promedio de palabras: {tamaño_promedio_palabras(text)}")
        print(f"Cantidad de palabras: {contar_palabras(text)}")
        print(f"Cantidad de numeros: {contar_numeros(text)}")
        print(f"Cantidad de fechas: {contar_fechas(text)}")

    except Exception as e:
        print(f"Error durante la extracción de TF-IDF: {e}")


if __name__ == "__main__":
    main()
