from matplotlib import pyplot as plt


class ClusterImageOrganizer:
    """
    Clase encargada de organizar imágenes según sus etiquetas de clúster.
    Implementa el Patrón Singleton para asegurar una única instancia en toda la aplicación.
    """
    _instance = None  # Atributo privado para almacenar la instancia única

    def __new__(cls, *args, **kwargs):
        """
        Sobrescribe el método __new__ para implementar el patrón Singleton.
        """
        if cls._instance is None:
            # Si no existe la instancia, crearla
            cls._instance = super(ClusterImageOrganizer, cls).__new__(cls)
        return cls._instance

    def __init__(self, imagenes=None, etiquetas=None):
        """
        Constructor que organiza las imágenes por clúster.
        :param imagenes: Lista de imágenes originales.
        :param etiquetas: Etiquetas de los clústeres generados por el modelo KMeans.
        """
        if not hasattr(self, 'clusters'):  # Asegurar que la inicialización solo ocurra una vez
            self.imagenes = imagenes if imagenes else []
            self.etiquetas = etiquetas if etiquetas else []
            self.clusters = self._organizar_imagenes()

    def _organizar_imagenes(self):
        """
        Agrupa las imágenes por clústeres.
        Devuelve un diccionario con claves como el número de clústeres y valores como la lista de imágenes.
        """
        clusters = {}
        for i, etiqueta in enumerate(self.etiquetas):
            if etiqueta not in clusters:
                clusters[etiqueta] = []
            clusters[etiqueta].append(self.imagenes[i])
        return clusters

    def obtener_imagenes_por_clust(self, cluster_num):
        """
        Devuelve las imágenes pertenecientes a un clúster específico.
        :param cluster_num: El número de clúster que se desea obtener.
        :return: Lista de imágenes en ese clúster.
        """
        return self.clusters.get(cluster_num, [])

    def visualizar_imagenes_por_clust(self):
        """
        Visualiza las imágenes de cada clúster (asumiendo que son imágenes 2D).
        Úsalo solo si estás trabajando con imágenes visualizables.
        """
        for cluster_num, imagenes in self.clusters.items():
            print(f"Imágenes en el clúster {cluster_num}:")
            for img in imagenes:
                plt.imshow(img.reshape(64, 64), cmap="gray")  # Ajusta la dimensión de la imagen aquí
                plt.axis('off')
                plt.show()
            print(f"--- Fin del Clúster {cluster_num} ---")

    def agregar_imagen_a_clust(self, imagen, cluster_num):
        """
        Agrega una nueva imagen a un clúster específico.
        :param imagen: Imagen para agregar.
        :param cluster_num: Número de clúster al que la imagen pertenece.
        """
        if cluster_num not in self.clusters:
            self.clusters[cluster_num] = []
        self.clusters[cluster_num].append(imagen)

    @classmethod
    def get_instance(cls, imagenes=None, etiquetas=None):
        """
        Método de clase para obtener la instancia única de la clase.
        Si la instancia aún no existe, se inicializa con los parámetros dados.
        """
        if cls._instance is None:
            cls._instance = cls(imagenes, etiquetas)
        return cls._instance
