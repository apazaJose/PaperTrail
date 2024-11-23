
import cv2

from src.shared.OpenCv.ImageProcessorInterface import ImageProcessorInterface


class ImagePreprocessor:
    def __init__(self, processors: list[ImageProcessorInterface]) -> None:
        self.processors = processors

    def preprocess(self, image: cv2.Mat) -> cv2.Mat:
        for processor in self.processors:
            image = processor.process(image)
        return image