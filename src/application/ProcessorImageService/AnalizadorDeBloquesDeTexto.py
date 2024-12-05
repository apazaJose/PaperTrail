import cv2


class AnalizadorDeBloquesDeTextoConMetricas:
    def __init__(self, procesador_escala_grises, procesador_umbral):
        """
        Inicializa el analizador con los procesadores necesarios.

        Args:
            procesador_escala_grises: Objeto que implementa la conversión a escala de grises.
            procesador_umbral: Objeto que implementa la binarización de la imagen.
        """
        self.procesador_escala_grises = procesador_escala_grises
        self.procesador_umbral = procesador_umbral

    def obtener_cantidad_bloques(self, imagen):
        """
        Calcula la cantidad de bloques de texto detectados en una imagen.

        Args:
            imagen: Imagen de entrada.

        Returns:
            int: Cantidad de bloques de texto detectados.
        """
        imagen_gris = self.procesador_escala_grises.process(imagen)
        imagen_binaria = self.procesador_umbral.process(imagen_gris)

        # Encontrar contornos de bloques de texto
        contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        return len(contornos)

    def obtener_area_total(self, imagen):
        """
        Calcula el área total ocupada por los bloques de texto.

        Args:
            imagen: Imagen de entrada.

        Returns:
            int: Área total de los bloques de texto detectados.
        """
        imagen_gris = self.procesador_escala_grises.process(imagen)
        imagen_binaria = self.procesador_umbral.process(imagen_gris)

        # Encontrar contornos de bloques de texto
        contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Calcular el área total de los bloques de texto
        area_total = sum([cv2.boundingRect(c)[2] * cv2.boundingRect(c)[3] for c in contornos])

        return area_total

    def obtener_promedio_area(self, imagen):
        """
        Calcula el promedio del área de los bloques de texto.

        Args:
            imagen: Imagen de entrada.

        Returns:
            float: Promedio del área de los bloques de texto detectados.
        """
        imagen_gris = self.procesador_escala_grises.process(imagen)
        imagen_binaria = self.procesador_umbral.process(imagen_gris)

        # Encontrar contornos de bloques de texto
        contornos, _ = cv2.findContours(imagen_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Calcular el promedio del área de los bloques de texto
        areas = [cv2.boundingRect(c)[2] * cv2.boundingRect(c)[3] for c in contornos]
        promedio_area = sum(areas) / len(areas) if areas else 0

        return promedio_area
