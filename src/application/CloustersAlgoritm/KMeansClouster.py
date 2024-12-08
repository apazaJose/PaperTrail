from sklearn.cluster import KMeans
class KMeansClouster:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, arrayImagenesVectorizadas):
        # Este bloque solo debe ejecutarse la primera vez que se inicializa la instancia
        if not hasattr(self, '_initialized'):
            self._initialized = True
            # Inicialización de variables o configuración necesaria
            self.kmeans = None
            self.arrarImagenesVectorizadas = arrayImagenesVectorizadas
            self.numClousters= len(arrayImagenesVectorizadas)
            self.centroides = None

    # Métodos necesarios para la funcionalidad de la clase

    def inicializar_clusters(self,):
        # Crear la instancia de KMeans con el número de imágenes como número de clusters
        self.kmeans = KMeans(n_clusters=self.numClousters, random_state=42)
        self.kmeans.fit(self.arrarImagenesVectorizadas)

        # Guardar los centroides iniciales
        self.centroides = self.kmeans.cluster_centers_

        #Aqui ya se puede crear la forma o los directorios para guardas las imagnes sus respectoivo grupos.
        #inicializar los contenodres para guardas las imagenes

    def clasificarNuevaImagen(self,imagenVectorizada):
        # Predecir el clúster más cercano
        cluster_asignado = self.kmeans.predict(imagenVectorizada)[0]  # Predicción de clúster
        print(f"Predicción: La imagen pertenece al clúster {cluster_asignado}")

        # Ajustar el centroide de los clusters con la información de esta imagen
        self.kmeans.partial_fit(imagenVectorizada)  # Actualiza todos los centroides automáticamente


