from src.application.services.ProcesadorDeImagenes import ProcesadorDeImagenes
import cv2
def main():
    # Configurar OCR con la ruta de Tesseract
    tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = cv2.imread(r'C:\Users\Gustavo\Downloads\WhatsApp Image 2024-11-26 at 18.38.06.jpeg')
    #Cambiar las rutas a las rutas que maneja cada uno
    procesador = ProcesadorDeImagenes()
    vectorImagen = procesador.vectorizarTextoImagenProcesada(image,tesseract_cmd)
    print(vectorImagen)



if __name__ == "__main__":
    main()
