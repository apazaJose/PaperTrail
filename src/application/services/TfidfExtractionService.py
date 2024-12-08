from src.domain.entities.TfidfExtraction import TfidfExtraction
from src.domain.entities.TfidfExtractorPort import TfidfExtractorPort

class TfidfExtractionService(TfidfExtractorPort):
    def __init__(self):
        # Inicia el extractor de TF-IDF
        self.tfidf_extractor = TfidfExtraction()

    def extract(self, text: str) -> dict:
        """
        Llama al método de extracción de TF-IDF del dominio.
        :param text: Texto de entrada.
        :return: Diccionario con las características TF-IDF.
        """
        return self.tfidf_extractor.extract_features(text)
