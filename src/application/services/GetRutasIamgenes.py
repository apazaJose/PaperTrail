import os
import glob


def obtener_imagenes(directorio):
    # Validar si el directorio existe
    if not os.path.isdir(directorio):
        print("El directorio no existe.")
        return []

    # Obtener todas las imágenes en el directorio (archivos con extensión .jpg, .jpeg, .png)
    imagenes = glob.glob(os.path.join(directorio, '*.[jp][pn]g'))

    return imagenes
