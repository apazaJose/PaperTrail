from sklearn.feature_extraction.text import TfidfVectorizer

class TfidfExtraction:
    def __init__(self):
        # Inicia el vectorizador TF-IDF
        self.vectorizer = TfidfVectorizer()

    def extract_features(self, text: str) -> dict:
        """
        Extrae las características de un texto usando el algoritmo TF-IDF.
        :param text: Texto de entrada.
        :return: Diccionario con las palabras y sus puntuaciones TF-IDF.
        """
        # Convertir el texto en una matriz TF-IDF
        tfidf_matrix = self.vectorizer.fit_transform([text])

        # Obtener las palabras y sus correspondientes valores TF-IDF
        feature_names = self.vectorizer.get_feature_names_out()

        # Convertir la matriz a un arreglo y mapearlo con las palabras
        tfidf_array = tfidf_matrix.toarray().flatten()
        result = {feature_names[i]: tfidf_array[i] for i in range(len(feature_names))}
        return result
