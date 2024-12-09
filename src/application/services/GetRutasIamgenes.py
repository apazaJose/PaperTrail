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

    rutas_imagenes = []
    for extension in ['*.jpg', '*.jpeg', '*.png']:
        rutas_imagenes.extend(glob.glob(os.path.join(directorio, extension)))

    imagenes_cargadas = []
    try:
        num_cluesteres = int(num_cluesteres)
    except ValueError:
        print("El número de clústeres debe ser un entero.")
        return []
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
        print (vector)
        datos.append(vector)


    # Inicializar KMeansClouster
    kmeans = KMeansClouster.get_instance(num_cluesteres, datos)
    etiquetas = kmeans.inicializar_clusters()

    # Organizar imágenes con ClusterImageOrganizer
    organizer = ClusterImageOrganizer.get_instance(imagenes_cargadas, etiquetas)

    # Ahora puedes usar el objeto organizer
    cluster = organizer.organizar_imagenes()
    organizer.visualizar_imagenes_por_clust()

    return cluster
