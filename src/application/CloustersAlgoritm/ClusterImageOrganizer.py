from matplotlib import pyplot as plt
import numpy as np
from cv2.gapi.wip.draw import Image
from PIL import Image


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
            self.etiquetas = etiquetas if etiquetas is not None else []
            self.clusters = self.organizar_imagenes()

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
            if isinstance(img, np.ndarray):  # Si es un array numpy, convertir a imagen con PIL
                img = Image.fromarray(img)
            # Convertir la imagen a escala de grises
            img = img.convert("L")
            # Redimensionar la imagen a la dimensión objetivo
            img = img.resize(target_size, Image.Resampling.LANCZOS)  # LANCZOS es mejor para redimensionar
            return np.array(img)  # Devolver como array numpy
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

        # En caso de que solo haya un clúster, axes no es un arreglo de varias entradas.
        if num_clusters == 1:
            axes = [axes]

        for i, (cluster_num, imagenes) in enumerate(self.clusters.items()):
            ax = axes[i]
            ax.set_title(f"Clúster {cluster_num}", fontsize=12)
            ax.axis("off")

            # Crear un collage horizontal de imágenes en este clúster
            if len(imagenes) > 0:
                try:
                    collage = np.concatenate([img.reshape(64, 64) for img in imagenes], axis=1)
                    ax.imshow(collage, cmap="gray")
                except Exception as e:
                    print(f"Error al crear el collage para el clúster {cluster_num}: {e}")
            else:
                ax.text(0.5, 0.5, "Sin imágenes", ha='center', va='center', fontsize=10)

        plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajustar el diseño para el título
        plt.show()

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

