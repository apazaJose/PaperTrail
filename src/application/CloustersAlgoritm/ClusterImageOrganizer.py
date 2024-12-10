import numpy as np
from cv2.gapi.wip.draw import Image
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
        Se asegura de que solo exista una única instancia.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, imagenes=None, etiquetas=None):
        """
        Constructor que configura la instancia solo una vez.
        :param imagenes: Lista de imágenes originales.
        :param etiquetas: Etiquetas de los clústeres generados por el modelo KMeans.
        """
        if not self._initialized:  # Solo ejecuta la inicialización una vez
            self.imagenes = imagenes if imagenes else []
            self.etiquetas = etiquetas if etiquetas else []
            self.clusters = self.organizar_imagenes()
            self._initialized = True  # Marca la instancia como inicializada

    @classmethod
    def get_instance(cls):
        """
        Método de clase para obtener la instancia única de la clase.
        No acepta parámetros. Solo devuelve la instancia existente.
        """
        if cls._instance is None:
            raise ValueError("La instancia aún no ha sido inicializada. Inicialice usando el constructor.")
        return cls._instance
    def organizar_imagenes(self):
        """
        Agrupa las imágenes por clústeres.
        Devuelve un diccionario con claves como el número de clústeres y valores como la lista de imágenes.
        """
        clusters = {}
        for i, etiqueta in enumerate(self.etiquetas):
            if etiqueta not in clusters:
                clusters[etiqueta] = []
            # Redimensionar imágenes antes de agregarlas al clúster
            img_redimensionada = self.redimensionar_imagen(self.imagenes[i])
            if img_redimensionada is not None:
                clusters[etiqueta].append(img_redimensionada)
        return clusters

    def redimensionar_imagen(self, img, target_size=(64, 64)):
        """
        Redimensiona una imagen proporcionalmente al tamaño objetivo.
        :param img: Imagen a redimensionar.
        :param target_size: Tamaño objetivo para las imágenes.
        :return: Imagen redimensionada como un array numpy.
        """
        try:
            if isinstance(img, np.ndarray):
                img = Image.fromarray(img)  # Convertir a imagen con PIL si es un array numpy
            img = img.convert("L")  # Asegurar que esté en escala de grises
            img.thumbnail(target_size, Image.ANTIALIAS)  # Redimensionar proporcionalmente
            # Crear un lienzo nuevo con el tamaño objetivo
            nueva_img = Image.new("L", target_size)
            # Pegar la imagen redimensionada centrada en el lienzo
            nueva_img.paste(img, ((target_size[0] - img.size[0]) // 2, (target_size[1] - img.size[1]) // 2))
            return np.array(nueva_img)
        except Exception as e:
            print(f"Error al redimensionar la imagen: {e}")
            return None
    def obtener_imagenes_por_clust(self, cluster_num):
        """
        Devuelve las imágenes pertenecientes a un clúster específico.
        :param cluster_num: El número de clúster que se desea obtener.
        :return: Lista de imágenes en ese clúster.
        """
        return self.clusters.get(cluster_num, [])

    def visualizar_imagenes_por_clust(self):
        """
        Visualiza las imágenes de cada clúster en una sola ventana.
        Cada clúster tendrá su propia sección en la interfaz visual.
        """
        num_clusters = len(self.clusters)

        # Crear subgráficas para cada clúster
        fig, axes = plt.subplots(num_clusters, 1, figsize=(8, num_clusters * 4))
        fig.suptitle("Imágenes agrupadas por Clúster", fontsize=16)

        # En caso de que solo haya un clúster, `axes` no es un arreglo de varias entradas.
        if num_clusters == 1:
            axes = [axes]

        for i, (cluster_num, imagenes) in enumerate(self.clusters.items()):
            ax = axes[i]
            ax.set_title(f"Clúster {cluster_num}", fontsize=12)
            ax.axis("off")

            # Crear un collage horizontal de imágenes en este clúster
            if len(imagenes) > 0:
                # Crear un collage concatenando imágenes horizontalmente
                collage = np.concatenate([img.reshape(64, 64) for img in imagenes], axis=1)
                ax.imshow(collage, cmap="gray")
            else:
                ax.text(0.5, 0.5, "Sin imágenes", ha='center', va='center', fontsize=10)

        plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajustar el diseño para el título
        plt.show()

    def obtener_imagenes_por_clust(self, cluster_num):
        """
        Devuelve las imágenes pertenecientes a un clúster específico.
        :param cluster_num: El número de clúster que se desea obtener.
        :return: Lista de imágenes en ese clúster.
        """
        return self.clusters.get(cluster_num, [])

    def agregar_imagen_a_clust(self, imagen, cluster_num):
        """
        Agrega una nueva imagen a un clúster específico.
        :param imagen: Imagen para agregar.
        :param cluster_num: Número de clúster al que la imagen pertenece.
        """
        if cluster_num not in self.clusters:
            self.clusters[cluster_num] = []
            img_redimensionada = self.redimensionar_imagen(imagen)
            if img_redimensionada is not None:
                self.clusters[cluster_num].append(img_redimensionada)
        self.clusters[cluster_num].append(img_redimensionada)

