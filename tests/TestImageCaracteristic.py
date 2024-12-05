import pytest
from unittest.mock import MagicMock
import cv2
from src.application.services import ProcesadorDeImagenes

class TestProcesadorDeImagenes:
    def setUp(self):
        # Crear un mock para la imagen
        self.image_mock = cv2.imread('/Users/jose/Documents/Pycharm/PaperTrail/PaperTrail/tests/imagenes/receta.jpeg')

        # Crear la instancia del ProcesadorDeImagenes
        self.procesador = ProcesadorDeImagenes()

        # Asegúrate de que esta clase se esté instanciando correctamente

        # Configurar el mock para que devuelva la imagen mockeada cuando se invoque su proceso
        # Por ejemplo, si hay un atributo que debe ser mockeado:
        # self.procesador.procesadorReducirRuido = MagicMock()
        # self.procesador.procesadorReducirRuido.process.return_value = self.image_mock

    def test_vectorizar_imagen(self):
        # Llamar al método 'vectorizarImagen' con la imagen mockeada
        if self.image_mock is None:
            return "no procesador de imagen no"
        vector = self.procesador.vectorizarImagen(self.image_mock)
        print(vector)

        # Realiza las aserciones necesarias
        assert vector is not None  # O cualquier otra condición que desees verificar
