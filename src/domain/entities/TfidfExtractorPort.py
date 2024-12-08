from abc import ABC, abstractmethod

class TfidfExtractorPort(ABC):
    @abstractmethod
    def extract(self, text: str) -> dict:
        """
        Método para extraer características usando TF-IDF.
        :param text: Texto que se procesará.
        :return: Diccionario con las características extraídas.
        """
        pass
