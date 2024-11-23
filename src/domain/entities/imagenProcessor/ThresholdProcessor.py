
import cv2

from src.shared.OpenCv.ImageProcessorInterface import ImageProcessorInterface


class ThresholdProcessor(ImageProcessorInterface):
    def __init__(self, open_cv_handler):
        super().__init__(open_cv_handler)

    def process(self, image):
        return self.open_cv_handler.apply_threshold(image)

