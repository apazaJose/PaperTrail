class CalculadorDeTamanoYProporcion:
    def __init__(self):
        """
        Inicializa el calculador de tamaño y proporción.
        """
        pass

    def calcular(self, imagen):
        """
        Calcula el tamaño (ancho, alto) y la proporción de una imagen.

        Args:
            imagen: Imagen de entrada.

        Returns:
            tuple: Una tupla con el ancho, la altura y la proporción (ancho / altura).
        """
        # Obtener el tamaño de la imagen
        altura, ancho = imagen.shape[:2]

        # Calcular la proporción
        proporcion = ancho / altura

        # Retornar los resultados
        return (ancho, altura)
