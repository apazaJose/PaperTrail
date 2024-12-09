import os
import glob
import cv2
import numpy as np
from src.application.services.ProcesadorDeImagenes import ProcesadorDeImagenes
from src.application.CloustersAlgoritm.KMeansClouster import KMeansClouster
from src.application.CloustersAlgoritm.ClusterImageOrganizer import ClusterImageOrganizer


def obtener_imagenes(directorio, num_cluesteres):
    """
    Obtiene todas las imágenes en el directorio proporcionado y las organiza en clústeres.
    """
    # Validar si el directorio existe
    if not os.path.isdir(directorio):
        print("El directorio no existe.")
        return []

    # Convertir num_cluesteres a entero
    try:
        num_cluesteres = int(num_cluesteres)
    except ValueError:
        print("El número de clústeres debe ser un entero.")
        return []

    # Obtener todas las imágenes en el directorio
    rutas_imagenes = glob.glob(os.path.join(directorio, '*.[jp][pn]g'))
    imagenes_cargadas = []

    for ruta in rutas_imagenes:
        try:
            imagen = cv2.imread(ruta)
            if imagen is not None:
                imagenes_cargadas.append(imagen)
            else:
                print(f"No se pudo cargar la imagen: {ruta}")
        except Exception as e:
            print(f"Error al cargar la imagen {ruta}: {e}")

    # Procesar las imágenes con ProcesadorDeImagenes
    procesador = ProcesadorDeImagenes()
    datos = []
    tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    for imagen in imagenes_cargadas:
        vector = procesador.ObtenerVectorDatos(imagen, tesseract_cmd)
        datos.append(vector)

    # Depuración: verificar longitudes de los vectores
    vector_lengths = [len(v) for v in datos]
    print("Longitudes de los vectores:", vector_lengths)

    # Rellenar vectores más cortos con ceros
    max_length = max(vector_lengths)
    datos = [np.pad(v, (0, max_length - len(v)), mode='constant') for v in datos]

    # Convertir datos a matriz numpy
    datos = np.array(datos)

    # Inicializar KMeansClouster
    kmeans = KMeansClouster.get_instance(num_cluesteres, datos)
    etiquetas = kmeans.inicializar_clusters()

    # Organizar imágenes con ClusterImageOrganizer
    organizer = ClusterImageOrganizer.get_instance(imagenes_cargadas, etiquetas)
    cluster = organizer.organizar_imagenes()

    # Visualizar las imágenes por clúster
    organizer.visualizar_imagenes_por_clust()

    return cluster
