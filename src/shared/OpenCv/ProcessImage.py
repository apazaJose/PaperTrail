# shared/OpenCv.py
import cv2

def preprocess_image(image_path: str) -> str:
    """
    Preprocesa una imagen para mejorar la precisión del OCR.
    """
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, processed_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
        processed_image_path = "processed_image.png"
        cv2.imwrite(processed_image_path, processed_image)
        return processed_image_path
    except Exception as e:
        raise ValueError(f"Error en el preprocesamiento: {e}")
