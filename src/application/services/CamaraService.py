

import cv2

from src.domain.entities.imagenProcessor.ImagePreprocessor import ImagePreprocessor
from src.shared.OpenCv.ImageSaver import ImageSaver


class CameraService:
    def __init__(self, image_path: str, preprocessor: ImagePreprocessor, saver: ImageSaver):
        self.image_path = image_path
        self.preprocessor = preprocessor
        self.saver = saver

    def capture_and_process_image(self):
        image = cv2.imread(self.image_path)

        # Procesar la imagen con el preprocesador
        processed_image = self.preprocessor.preprocess(image)

        # Guardar la imagen procesada
        self.saver.save(processed_image, 'processed_image.jpg')

        return processed_image
