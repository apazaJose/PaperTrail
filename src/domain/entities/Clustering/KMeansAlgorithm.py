from sklearn.cluster import KMeans

class KMeansAlgorithm:
    def __init__(self, n_clusters):
        """
        Inicializa el algoritmo K-means con un número definido de clusters.
        :param n_clusters: Número de clusters.
        """
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)

    def train(self, training_data):
        """
        Entrena el modelo K-means con datos de entrenamiento.
        :param training_data: Lista de características para entrenar.
        """
        self.kmeans.fit(training_data)

    def predict_cluster(self, features):
        """
        Predice el cluster al que pertenece un conjunto de características.
        :param features: Lista de características.
        :return: El cluster predicho.
        """
        return self.kmeans.predict([features])[0]
