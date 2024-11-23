import cv2
import numpy as np

def process_document_image(image_path, output_path):


    # Leer la imagen
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("La imagen no pudo ser cargada. Verifica la ruta.")

    # Escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{output_path}/grayscale.png", gray)

    # Umbralización binaria
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(f"{output_path}/binary.png", binary)

    # Ajuste de contraste
    contrast = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)
    cv2.imwrite(f"{output_path}/contrast.png", contrast)

    # Corrección de perspectiva y recorte (detectando contornos)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    epsilon = 0.02 * cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, epsilon, True)

    if len(approx) == 4:
        # Perspectiva corregida
        pts = np.array([point[0] for point in approx], dtype="float32")
        rect = cv2.boundingRect(pts)
        x, y, w, h = rect
        warped = gray[y:y+h, x:x+w]
        cv2.imwrite(f"{output_path}/warped.png", warped)

    # Reducción de ruido
    denoised = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imwrite(f"{output_path}/denoised.png", denoised)

    print("Imágenes procesadas y guardadas en el directorio de salida.")