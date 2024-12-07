
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


class ProcesadorDeImagenes:
    def __init__(self):
        self.open_cv_handler = OpenCVHandler()
        self.procesadorContraste =ContrastProcessor(self.open_cv_handler)
        self.procesadorEscalaGrises=GrayscaleProcessor(self.open_cv_handler)
        self.procesadorReducirRuido=NoiseReducer(self.open_cv_handler)
        self.procesadorUmbralizacion=ThresholdProcessor(self.open_cv_handler)

    def vectorizarImagen(self,image):
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

