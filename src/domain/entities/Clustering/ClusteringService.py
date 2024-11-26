class ClusteringService:
    def __init__(self, kmeans_algorithm):
        """
        Servicio que usa el algoritmo K-means para clasificar documentos.
        :param kmeans_algorithm: Instancia del algoritmo KMeansAlgorithm.
        """
        self.kmeans = kmeans_algorithm

    def classify(self, features):
        """
        Clasifica características ya procesadas de un documento.
        :param features: Lista de características de la imagen.
        :return: Tipo de documento clasificado.
        """
        cluster = self.kmeans.predict_cluster(features)
        return self._map_cluster_to_document_type(cluster)

    def _map_cluster_to_document_type(self, cluster):
        """
        Mapeo de clusters a tipos de documentos.
        :param cluster: El cluster predicho.
        :return: Tipo de documento.
        """
        cluster_mapping = {
            0: "Factura",
            1: "Recibo",
            2: "Otro"
        }
        return cluster_mapping.get(cluster, "Desconocido")
