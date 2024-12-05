import cv2


class ContadorDeElementosVisuales:
    def __init__(self, procesador_escala_grises, procesador_umbral):
        """
        Inicializa el contador de elementos visuales con los procesadores necesarios.

        Args:
            procesador_escala_grises: Objeto que implementa la conversión a escala de grises.
            procesador_umbral: Objeto que implementa la binarización de la imagen.
        """
        self.procesador_escala_grises = procesador_escala_grises
        self.procesador_umbral = procesador_umbral

    def contar(self, imagen):
        """
        Cuenta el número de elementos visuales (contornos) en una imagen.

        Args:
            imagen: Imagen de entrada.

        Returns:
            int: Número de elementos visuales (contornos) encontrados en la imagen.
        """
        # Procesar la imagen
        imagen_gris = self.procesador_escala_grises.process(imagen)
        imagen_binaria = self.procesador_umbral.process(imagen_gris)

        # Detectar contornos
        contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Retornar el número de contornos encontrados
        return len(contornos)
