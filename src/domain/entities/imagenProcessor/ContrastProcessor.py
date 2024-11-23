from src.shared.OpenCv.ImageProcessorInterface import ImageProcessorInterface


class ContrastProcessor(ImageProcessorInterface):
    def __init__(self, open_cv_handler):
        super().__init__(open_cv_handler)

    def process(self, image):
        return self.open_cv_handler.increase_contrast(image)