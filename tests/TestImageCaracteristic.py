import cv2

from src.application.services.ProcesadorDeImagenes import ProcesadorDeImagenes


class TuProcesadorDeImagenes:
    def __init__(self):
        # Crear un mock para la imagen
        self.image_mock = cv2.imread('./../../PaperTrail/tests/imagenes/caratula.jpeg')

        if self.image_mock is None:
            raise ValueError("No se pudo cargar la imagen, verifica la ruta.")

        # Crear la instancia del ProcesadorDeImagenes
        self.procesador = ProcesadorDeImagenes()

    def test_vectorizar_imagen(self):
        # Llamar al método 'vectorizarImagen' con la imagen mockeada
        vector = self.procesador.vectorizarImagen(self.image_mock)
        print(vector)
        # Realiza las aserciones necesarias
        assert vector is not None  # O cualquier otra condición que desees verificar

if __name__ == '__main__':
    tu = TuProcesadorDeImagenes()  # Inicializamos correctamente la clase
    tu.test_vectorizar_imagen()

