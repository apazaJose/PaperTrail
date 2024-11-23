from abc import ABC, abstractmethod

from src.shared.OpenCv.OpenCVHandler import OpenCVHandler


class ImageProcessorInterface(ABC):
    def __init__(self, open_cv_handler: OpenCVHandler):
        self.open_cv_handler = open_cv_handler

    @abstractmethod
    def process(self, image):
        pass