from src.domain.entities.Clustering.KMeansAlgorithm import KMeansAlgorithm
from src.domain.entities.Clustering.ClusteringService import ClusteringService
from src.application.services.DocumentClassifierApplication import DocumentClassifierApplication

# Simulación de un módulo externo que procesa imágenes
def process_image(image_path):
    """
    Procesa una imagen y genera características simuladas.
    :param image_path: Ruta de la imagen a procesar.
    :return: Lista de características.
    """
    print(f"Procesando la imagen: {image_path}")

    # Simulaciones de características de la imagen
    color_promedio = [120, 100, 80]  # Simula valores promedio de RGB
    escala_grises_promedio = 50  # Simula el promedio de escala de grises
    densidad_bordes = 0.15  # Simula la densidad de bordes (15%)
    numero_palabras = 50  # Simula la cantidad de palabras extraídas
    relevancia_palabras_clave = 5  # Simula el número de palabras clave encontradas

    # Construcción del vector de características
    vector_caracteristicas = [
        *color_promedio,              # Rojo, Verde, Azul
        escala_grises_promedio,       # Intensidad de gris promedio
        densidad_bordes,              # Densidad de bordes
        numero_palabras,              # Número de palabras
        relevancia_palabras_clave,    # Relevancia de palabras clave
    ]

    return vector_caracteristicas


# Preprocesador de características
def preprocess_features(features):
    """
    Realiza un preprocesamiento básico sobre las características.
    :param features: Lista de características.
    :return: Características preprocesadas.
    """
    # Aquí puedes agregar más lógica si es necesario, como normalización
    return features


# Configuración inicial del sistema
def main():
    """
    Punto de entrada del programa.
    """
    # Datos de entrenamiento simulados
    training_data = [
        [120, 100, 80, 50, 0.15, 50, 5],  # Factura
        [200, 190, 180, 80, 0.10, 30, 3],  # Recibo
        [50, 40, 30, 20, 0.25, 20, 1],    # Otro
    ]

    # Inicializar el algoritmo KMeans con 3 clusters
    kmeans_algorithm = KMeansAlgorithm(n_clusters=3)
    kmeans_algorithm.train(training_data)

    # Imprimir los centroides después de entrenar
    print("\nCentroides de los clusters:")
    print(kmeans_algorithm.kmeans.cluster_centers_)

    # Configuración del servicio de clustering
    clustering_service = ClusteringService(kmeans_algorithm)

    # Configuración de la aplicación con preprocesador
    document_classifier = DocumentClassifierApplication(
        clustering_service, preprocess_features
    )

    # Simula la clasificación de una nueva imagen
    image_path = r"rutaprueba"  # Cambia esto por la ruta real de tu imagen
    features = process_image(image_path)  # Obtén las características procesadas de la imagen

    # Clasificar el documento
    document_type = document_classifier.classify(features)

    # Mostrar el resultado
    print(f"\nLa imagen '{image_path}' fue clasificada como: {document_type}")


# Ejecuta el programa principal
if __name__ == "__main__":
    main()
