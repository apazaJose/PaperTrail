import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

def generate_confusion_matrix():
    # Datos ficticios
    y_true = [0, 1, 2, 2, 0]
    y_pred = [0, 0, 2, 2, 1]
    cm = confusion_matrix(y_true, y_pred)

    # Crear y guardar el gráfico
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1, 2])
    disp.plot()
    plt.savefig("confusion_matrix.png")  # Guardar como imagen
    plt.close()  # Cerrar la figura para liberar recursos

def generate_cluster_plot():
    # Datos ficticios para clusters
    X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
    kmeans = KMeans(n_clusters=3)
    y_kmeans = kmeans.fit_predict(X)

    # Crear y guardar el gráfico
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='x')
    plt.savefig("cluster_plot.png")  # Guardar como imagen
    plt.close()  # Cerrar la figura para liberar recursos
