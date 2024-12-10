from sklearn.cluster import KMeans


class KMeansClouster:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, clousters=None, arrayImagenesVectorizadas=None):
        """
        Constructor para inicializar la clase KMeansClouster con el número de clústeres y el arreglo de imágenes vectorizadas.
        """
        if not self._initialized:
            self._initialized = True
            self.kmeans = None
            self.arrarImagenesVectorizadas = arrayImagenesVectorizadas
            self.numClousters = clousters
            self.centroides = None

    @classmethod
    def get_instance(cls):
        """
        Método de clase para obtener la única instancia de la clase (patrón Singleton).
        Si la instancia no existe, se crea una nueva; de lo contrario, se devuelve la existente.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


    def inicializar_clusters(self):
        """
        Ajustar KMeans con los datos de imágenes vectorizadas y configurar los clústeres.
        Devuelve las etiquetas que indican la asignación de cada imagen a su clúster correspondiente.
        """
        # Crear instancia de KMeans con el número de clusters
        self.kmeans = KMeans(n_clusters=self.numClousters, random_state=42)

        # Ajustar KMeans con los datos de imágenes vectorizadas
        self.kmeans.fit(self.arrarImagenesVectorizadas)

        # Guardar los centroides de los clusters después de ajustar el modelo
        self.centroides = self.kmeans.cluster_centers_

        # Clasificar todas las imágenes en sus respectivos clústeres
        etiquetas = self.kmeans.predict(self.arrarImagenesVectorizadas)

        # Devolver las etiquetas para saber qué imagen pertenece a qué clúster
        print("Centroides calculados:", self.centroides)
        print("Etiquetas asignadas a cada imagen:", etiquetas)
        print(etiquetas)
        return etiquetas  # Este es el array donde se indica qué clúster le corresponde a cada imagen.

    def clasificar_y_recalcular(self, imagenVectorizada):
        """
        Clasifica una nueva imagen en el clúster más cercano y actualiza los centroides de los clústeres.
        :param imagenVectorizada: La nueva imagen vectorizada para clasificar.
        :return: El número del clúster asignado.
        """
        # Clasificar la nueva imagen en el clúster más cercano
        cluster_asignado = self.kmeans.predict([imagenVectorizada])[0]
        print(f"Predicción: La imagen vectorizada se asignó al clúster {cluster_asignado}")

        # Usar partial_fit para actualizar los centroides de KMeans con la nueva imagen
        self.kmeans.partial_fit([imagenVectorizada])  # Actualiza los centroides
        self.centroides = self.kmeans.cluster_centers_  # Actualiza los centroides locales

        # Devolver el número del clúster asignado
        print("Nuevos centroides después de la actualización:", self.centroides)
        return cluster_asignado

