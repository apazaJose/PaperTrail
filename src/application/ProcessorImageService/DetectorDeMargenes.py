import cv2

class DetectorDeMargenes:
    def __init__(self, procesador_escala_grises):
        """
        Inicializa el detector con el procesador de escala de grises necesario.

        Args:
            procesador_escala_grises: Objeto que implementa la conversión a escala de grises.
        """
        self.procesador_escala_grises = procesador_escala_grises

    def detectar(self, imagen):
        """
        Detecta los márgenes de la imagen usando el algoritmo de Canny y devuelve un valor representativo (promedio).

        Args:
            imagen: Imagen de entrada.

        Returns:
            float: Valor representativo de los márgenes (promedio).
        """
        # Procesar la imagen a escala de grises
        imagen_gris = self.procesador_escala_grises.process(imagen)

        # Detectar bordes utilizando Canny
        bordes = cv2.Canny(imagen_gris, 50, 150)

        # Análisis de los márgenes
        margen_superior = bordes[0].mean()
        margen_inferior = bordes[-1].mean()
        margen_izquierdo = bordes[:, 0].mean()
        margen_derecho = bordes[:, -1].mean()

        # Calcular el valor promedio de los márgenes
        valor_representativo = (margen_superior + margen_inferior + margen_izquierdo + margen_derecho) / 4

        return valor_representativo
