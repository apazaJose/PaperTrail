from src.shared.OpenCv.ImageProcessorInterface import ImageProcessorInterface


class PerspectiveCorrector(ImageProcessorInterface):
    def __init__(self, open_cv_handler, src_points, dst_points):
        super().__init__(open_cv_handler)
        self.src_points = src_points
        self.dst_points = dst_points

    def process(self, image):
        return self.open_cv_handler.correct_perspective(image, self.src_points, self.dst_points)