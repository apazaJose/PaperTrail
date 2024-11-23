
import cv2


class OpenCVHandler:
    def __init__(self):
        pass

    def to_grayscale(self, image):
        """Convierte la imagen a escala de grises."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def apply_threshold(self, image, threshold_value=128):
        """Aplica umbralización a la imagen."""
        _, thresh_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
        return thresh_image

    def increase_contrast(self, image):
        """Ajusta el contraste de la imagen."""
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        l = cv2.equalizeHist(l)
        lab = cv2.merge([l, a, b])
        return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    def reduce_noise(self, image):
        """Aplica un filtro para reducir el ruido en la imagen."""
        return cv2.GaussianBlur(image, (5, 5), 0)

    def correct_perspective(self, image, src_points, dst_points):
        """Corrige la perspectiva de la imagen."""
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        return cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))
