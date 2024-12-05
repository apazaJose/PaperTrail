import cv2


class CalculadorDeDensidadDeTexto:
    def __init__(self, procesador_escala_grises, procesador_umbral):
        """
        Inicializa el calculador de densidad de texto con los procesadores necesarios.

        Args:
            procesador_escala_grises: Objeto que implementa la conversión a escala de grises.
            procesador_umbral: Objeto que implementa la binarización de la imagen.
        """
        self.procesador_escala_grises = procesador_escala_grises
        self.procesador_umbral = procesador_umbral

    def calcular_densidad(self, imagen):
        """
        Calcula la densidad del texto en una imagen, es decir, la proporción de píxeles de texto respecto a la imagen total.

        Args:
            imagen: Imagen de entrada.

        Returns:
            float: Densidad del texto en la imagen.
        """
        # Procesar la imagen
        imagen_gris = self.procesador_escala_grises.process(imagen)
        imagen_binaria = self.procesador_umbral.process(imagen_gris)

        # Calcular píxeles negros (texto) y blancos (vacíos)
        pixeles_texto = cv2.countNonZero(imagen_binaria)
        pixeles_totales = imagen_binaria.size

        # Calcular densidad
        densidad = pixeles_texto / pixeles_totales

        return densidad
