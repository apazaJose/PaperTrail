
from src.application.ProcessorImageService.AnalizadorDeBloquesDeTexto import AnalizadorDeBloquesDeTextoConMetricas
from src.application.ProcessorImageService.CalculadorDeDensidadDeTexto import CalculadorDeDensidadDeTexto
from src.application.ProcessorImageService.CalculadorDeTamanoYProporcion import CalculadorDeTamanoYProporcion
from src.application.ProcessorImageService.ContadorDeElementosVisuales import ContadorDeElementosVisuales
from src.application.ProcessorImageService.DetectorDeMargenes import DetectorDeMargenes
from src.domain.entities.imagenProcessor.ContrastProcessor import ContrastProcessor
from src.domain.entities.imagenProcessor.GrayscaleProcessor import GrayscaleProcessor
from src.domain.entities.imagenProcessor.NoiseReducer import NoiseReducer
from src.domain.entities.imagenProcessor.PerspectiveCorrector import PerspectiveCorrector
from src.domain.entities.imagenProcessor.ThresholdProcessor import ThresholdProcessor
from src.shared.OpenCv.OpenCVHandler import OpenCVHandler
from src.application.services.ImageOCRService import ImageOCRService
from src.domain.entities.imagenProcessor.OcrProcessor import OCRProcessor
from src.application.services.TfidfExtractionService import TfidfExtractionService
from src.application.services.WordFeature import tamaño_promedio_palabras,contar_lineas,contar_palabras,contar_fechas,contar_numeros


class ProcesadorDeImagenes:
    def __init__(self):
        self.open_cv_handler = OpenCVHandler()
        self.procesadorContraste =ContrastProcessor(self.open_cv_handler)
        self.procesadorEscalaGrises=GrayscaleProcessor(self.open_cv_handler)
        self.procesadorReducirRuido=NoiseReducer(self.open_cv_handler)
        self.procesadorUmbralizacion=ThresholdProcessor(self.open_cv_handler)

    def vectorizarImagen(self,image):
        #image es la imagen en fecto, no es la ruta de la imagen
        image = self.procesadorReducirRuido.process(image)

        adbt = AnalizadorDeBloquesDeTextoConMetricas(self.procesadorEscalaGrises,self.procesadorUmbralizacion)
        cantBloquesTexto = adbt.obtener_cantidad_bloques(image)
        areaBloqueTexto = adbt.obtener_area_total(image)
        tamanoPromBloqueTexto = adbt.obtener_promedio_area(image)

        densidadTexto=CalculadorDeDensidadDeTexto(self.procesadorEscalaGrises,self.procesadorUmbralizacion).calcular_densidad(image)

        TamanoImage = CalculadorDeTamanoYProporcion().calcular(image)

        NumElementos = ContadorDeElementosVisuales(self.procesadorEscalaGrises,self.procesadorUmbralizacion).contar(image)
        margenPromedio = DetectorDeMargenes(self.procesadorEscalaGrises).detectar(image)

        vector = (cantBloquesTexto,areaBloqueTexto,tamanoPromBloqueTexto,densidadTexto,TamanoImage,NumElementos,margenPromedio)
        return vector

    def vectorizarTextoImagenProcesada(self,image,path_tesseract) :
        #Este metodo recibe la imagen y la ubicacion del Tesseract
        ocr_processor = OCRProcessor(tesseract_cmd=path_tesseract)
        tfidf_service = TfidfExtractionService()
        procesarText = ImageOCRService(ocr_processor)
        image = self.procesadorEscalaGrises.process(image)

        #image = self.procesadorReducirRuido.process(image)
        #image= self.procesadorUmbralizacion.process(image)
        #processed_image_path = "processed_image3.png"
        #cv2.imwrite(processed_image_path, image)

        text = procesarText.extract_text_from_processed_image2(image)
        most_frequent_words = tfidf_service.extract(text)
        cantidad_palabras = contar_palabras(text)
        cantidadLineasTxt = contar_lineas(text)
        tamanio_prome_palabra = tamaño_promedio_palabras(text)
        cantidad_fechas = contar_fechas(text)
        contidad_numeros= contar_numeros(text)
        vector_image=(cantidad_palabras,tamanio_prome_palabra,cantidadLineasTxt,cantidad_fechas,contidad_numeros)
        return vector_image

    def vectorizarTexto(self,image,path_tesseract) :
        #Este metodo recibe la imagen y la ubicacion del Tesseract
        ocr_processor = OCRProcessor(tesseract_cmd=path_tesseract)
        tfidf_service = TfidfExtractionService()
        procesarText = ImageOCRService(ocr_processor)
        image = self.procesadorEscalaGrises.process(image)

        #image = self.procesadorReducirRuido.process(image)
        #image= self.procesadorUmbralizacion.process(image)
        #processed_image_path = "processed_image3.png"
        #cv2.imwrite(processed_image_path, image)

        text = procesarText.extract_text_from_processed_image2(image)
        return text

    def ObtenerVectorDatos(self, image, path_tesseract):
        """
        Combina los vectores generados por vectorizarImagen y vectorizarTextoImagenProcesada
        en un solo vector.
        """
        vector_imagen = self.vectorizarImagen(image)
        vector_texto = self.vectorizarTextoImagenProcesada(image, path_tesseract)

        # Combinar los vectores
        vector_combinado = vector_imagen + vector_texto

        return vector_combinado