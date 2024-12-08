class DocumentClassifierApplication:
    def __init__(self, clustering_service, preprocessor):
        """
        Inicializa la aplicación de clasificación de documentos.
        :param clustering_service: Instancia del servicio de clustering.
        :param preprocessor: Función para preprocesar características.
        """
        self.clustering_service = clustering_service
        self.preprocessor = preprocessor

    def classify(self, features):
        """
        Clasifica un conjunto de características de una imagen.
        :param features: Características extraídas de la imagen.
        :return: Tipo de documento clasificado.
        """
        # Preprocesar las características
        preprocessed_features = self.preprocessor(features)

        # Clasificar el documento
        return self.clustering_service.classify(preprocessed_features)
