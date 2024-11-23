import cv2

class ImageSaver:
    def save(self, image: cv2.Mat, output_path: str):
        cv2.imwrite(output_path, image)