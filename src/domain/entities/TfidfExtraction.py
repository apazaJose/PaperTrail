from sklearn.feature_extraction.text import TfidfVectorizer


class TfidfExtraction:
    def __init__(self):
        # Inicia el vectorizador TF-IDF con palabras de parada personalizadas
        custom_stop_words = ["de", "el", "y", "por", "la","esta", "es"] #Palabras restringidas sin valor para los calculos
        self.vectorizer = TfidfVectorizer(stop_words=custom_stop_words)

    def extract_features(self, text: str) -> dict:
        """
        Extrae las palabras con la mayor frecuencia TF-IDF de un texto.

        :param text: Texto de entrada.
        :return: Diccionario con palabras de mayor frecuencia y sus puntuaciones.
        """
        # Convertir el texto en una matriz TF-IDF
        tfidf_matrix = self.vectorizer.fit_transform([text])

        # Obtener las palabras y sus correspondientes valores TF-IDF
        feature_names = self.vectorizer.get_feature_names_out()
        tfidf_array = tfidf_matrix.toarray().flatten()

        # Mapear las palabras con sus puntuaciones TF-IDF
        result = {feature_names[i]: tfidf_array[i] for i in range(len(feature_names))}

        # Identificar las palabras con la puntuación más alta
        if result:
            max_value = max(result.values())
            most_frequent = {word: score for word, score in result.items() if score == max_value}
            return most_frequent
        else:
            return {}
