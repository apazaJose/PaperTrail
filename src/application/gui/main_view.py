from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
# Pequeñas ventanas
from kivy.uix.popup import Popup

# Manejo de Imagenes
import cv2

# Manejo de Texto
from kivy.uix.label import Label

import cv2
from src.application.services.ProcesadorDeImagenes import ProcesadorDeImagenes

Window.size = (1300, 800)


Builder.load_string("""

                                
<MisPestanas>

    do_default_tab: True
    default_tab: pestana2
    tab_pos: 'left_top'   # Pestañas a la izquierda
    tab_width: 100        # Ancho de las pestañas
    tab_height: 100       # Altura de las pestañas (por defecto es 40) 
    canvas.before:
        Color:
            rgba: 0.0745, 0.3412, 0.4588, 1  # Color en formato RGBA
        Rectangle:
            pos: self.pos
            size: self.size 

    TabbedPanelItem:
        text: ""
        background_normal: 'assets/images/1_Blaco.jpg'
        background_down: 'assets/images/1_Azul.jpg'
        id: pestana1

        BoxLayout:
            orientation: "vertical"
            size_hint: 1, 1
        
            BoxLayout:
                size_hint: 1, 0.1
                orientation: "horizontal"
                canvas.before:
                    Color:
                        rgba: 0.0745, 0.3412, 0.4588, 1  # Color en formato RGBA
                    Rectangle:
                        pos: self.pos
                        size: self.size 
                        
                BoxLayout:
                    size_hint_Y: 1
                    size_hint_x: None
                    width: 50  # Ancho fijo
                
                BoxLayout:
                    size_hint: 0.9, 1          
                    Label:
                        size_hint: 1, 1
                        font_size: 25
                        text: 'Datos del Documento'
                        halign: 'left'  # Alineación horizontal a la izquierda
                        valign: 'middle'  # Alineación vertical centrada
                        text_size: self.width, None  
       
            BoxLayout:
                size_hint: 1, 0.9
                orientation: 'horizontal'
                
                BoxLayout:
                    size_hint: 0.4, 1
                    orientation: 'vertical'
                    canvas.before:
                        Color:
                            rgba: 0.843, 0.894, 0.910, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            
                    BoxLayout:
                        size_hint: 1, 1
                        
                        AnchorLayout:
                            size_hint: 1, 1
                            anchor_x: 'center'
                            anchor_y: 'center'
                            
                            BoxLayout:
                                size_hint: 0.8, 0.9
                                canvas.before:
                                    Color:
                                        rgba: 0.743, 0.794, 0.810, 1
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                                
                                BoxLayout:
                                    size_hint: 1, 1
                                    
                                    Image:
                                        id: subVentana_3_Imajen
                                        source: ""
                                        allow_stretch: True
                                        keep_ratio: True
                                    
                                    #----------------------------------------------------------
                                    # SubVentana_3
                                    #----------------------------------------------------------
                                    # Imajen de la (SubVentana_1) de la imajen del texto que Escogimos
                                    #----------------------------------------------------------
                            
                            
                    
                    AnchorLayout:
                        size_hint: 1,None
                        height: 150
                        anchor_x: 'center'
                        anchor_y: 'center'
                        
                        Button:
                            size_hint: None,1
                            size_hint: None, 1
                            width: 150
                            text: ''
                            background_normal: 'assets/images/5_Vacio.png'  # Ruta de la imagen
                            background_down: 'assets/images/5_Vacio.png'  # Ruta de la imagen cuando el botón es presionado
                            on_press: app.funcion_predictoria()
                            ##****************************************************#****************************************************
                            # Boton 5 Predecir con Kmeans o Otro en (desarollo) -- y mostrar alguna Grafica o imajen SubVentana_4
                            ##****************************************************#****************************************************
                            
                BoxLayout:
                    size_hint: 0.6, 1
                    orientation: 'vertical'
                    
                    BoxLayout:
                        size_hint: 1, 0.1
                        orientation: 'horizontal'
                        canvas.before:
                            Color:
                                rgba: 0.239, 0.682, 0.796, 1 
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        
                        BoxLayout:
                            size_hint_Y: 1
                            size_hint_x: None
                            width: 25  # Ancho fijo
                        
                        BoxLayout:
                            size_hint: 1,1        
                            Label:
                                font_size: 20
                                text: 'Analisis del Documento'
                                halign: 'left'  # Alineación horizontal a la izquierda
                                valign: 'middle'  # Alineación vertical centrada
                                text_size: self.width, None
                        
                    BoxLayout:
                        size_hint: 1, 0.9
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1 
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        
                        AnchorLayout:
                            size_hint: 1, 1
                            anchor_x: 'center'
                            anchor_y: 'center'
                            
                            BoxLayout:
                                size_hint: 0.9, 0.9
                                canvas.before:
                                    Color:
                                        rgba: 0.8, 0.8, 0.810, 1
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                                
                                BoxLayout:
                                    size_hint: 1, 1
                                    
                                    #---------------------------------------------------------
                                    # SubVentana_4
                                    #---------------------------------------------------------
                                    # Graficos o Imajenes (en Desarollo)
                                    #---------------------------------------------------------
                                
                            
    
    
    
    #################################################################################################
    # Pestaña 2                                                                                     #
    #################################################################################################
    TabbedPanelItem:
        id: pestana2  
        background_normal: 'assets/images/2_Blanco.jpg'  # Ruta de la imagen
        background_down: 'assets/images/2_Azul.jpg'  # Ruta de la imagen cuando el botón es presionado 
        text: ""  # El texto está vacío porque solo queremos la image

        BoxLayout:
            orientation: "vertical"
            
            BoxLayout:
                orientation: "horizontal"
                size_hint: 1, 0.1
                canvas.before:
                    Color:
                        rgba: 0.0745, 0.3412, 0.4588, 1  # Color en formato RGBA
                    Rectangle:
                        pos: self.pos
                        size: self.size
                
                BoxLayout:
                    size_hint_Y: 1
                    size_hint_x: None
                    width: 50  # Ancho fijo
                
                BoxLayout:
                    size_hint: 0.9, 1          
                    Label:
                        size_hint: 1, 1
                        font_size: 25
                        text: 'Escanear Documentos'
                        halign: 'left'  # Alineación horizontal a la izquierda
                        valign: 'middle'  # Alineación vertical centrada
                        text_size: self.width, None                                   # Ajusta el texto al ancho disponible del Label
                    Button:
                        size_hint: None, 1
                        width: 150
                        text: 'Play'
                        on_press: app.funcion_apresurada()
                
            BoxLayout:
                size_hint: 1, 0.9
                orientation: "horizontal"
                
                BoxLayout:
                    orientation: "vertical"
                    size_hint: 0.6, 1
                    canvas.before:
                        Color:
                            rgba: 0.843, 0.894, 0.910, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            
                    AnchorLayout:
                        size_hint: 1,1
                        anchor_x: 'center'
                        anchor_y: 'center'
                        
                        BoxLayout:
                            size_hint: None,0.9
                            size_hint_x: 0.6
                            canvas.before:
                                Color:
                                    rgba: 0.743, 0.794, 0.810, 1
                                Rectangle:
                                    pos: self.pos
                                    size: self.size
                        
                            BoxLayout:
                                size_hint: 1,1
                                Image:
                                    id: subVentana_1_Imajen
                                    source: ""
                                    allow_stretch: True
                                    keep_ratio: True
                                
                                #---------------------------------------------------------
                                # SubVentana_1
                                #---------------------------------------------------------
                                # Imajen o Ruta de la imagen
                                #---------------------------------------------------------
                             
                    AnchorLayout:
                        size_hint: 1, None
                        height: 150
                        anchor_x: 'center'
                        anchor_y: 'center'
                        
                        BoxLayout:
                            orientation: 'horizontal'
                            size_hint: 0.8,1

                        
                            Button:
                                text: ''
                                size_hint: None, 1
                                width: 150
                                background_normal: 'assets/images/3_Blanco.jpg'  # Ruta de la imagen
                                background_down: 'assets/images/3_Blanco.jpg'  # Ruta de la imagen cuando el botón es presionado
                                on_press: root.seleccionar_imagen()
                                #****************************************************
                                # Boton_1 = Explorar en Busqueda de la Imajen
                                #****************************************************
                                
                                
                                
                            Button:
                                text: ''
                                size_hint: None, 1
                                width: 150
                                background_normal: 'assets/images/5_Transparente_Nueve.jpg'  # Ruta de la imagen
                                background_down: 'assets/images/5_Transparente_Nueve.jpg'  # Ruta de la imagen cuando el botón es presionado  
                                on_press: app.limpiar_imagen(self)
                                
                                #****************************************************
                                # Boton_2 = Borrar Todo 
                                #****************************************************
                              
                                
                            Button:
                                text: ''
                                size_hint: None, 1
                                width: 150
                                background_normal: 'assets/images/6_Transparente.png'  # Ruta de la imagen
                                background_down: 'assets/images/6_Transparente.png'  # Ruta de la imagen cuando el botón es presionado  
                                on_press: app.filtrar_imagen()
                                
                                #**********************************************************************************************
                                # Boton_3 = Aplicar Filtros Y Extraer Texto con Tessercat  y mostrar el texto en SubVentana_2
                                #**********************************************************************************************
                                
                            Button:
                                text: ''
                                size_hint: None, 1
                                width: 150
                                background_normal: 'assets/images/4_Blanco.jpg'  # Ruta de la imagen
                                background_down: 'assets/images/4_Blanco.jpg'  # Ruta de la imagen cuando el botón es presionado  
                                on_press: app.guardar_texto_a_txt()
                                
                                #****************************************************
                                # Boton_4 = Guardar el Texto obtenido de la Imajen
                                #****************************************************
                                
                                
                BoxLayout:
                    size_hint: 0.4, 1
                    orientation: 'vertical'
                    
                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint: 1, 0.1
                        canvas.before:
                            Color:
                                rgba: 0.239, 0.682, 0.796, 1 
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        
                        BoxLayout:
                            size_hint_Y: 1
                            size_hint_x: None
                            width: 25  # Ancho fijo
                        
                        BoxLayout:
                            size_hint: 1,1        
                            Label:
                                font_size: 20
                                text: 'Extraccion de Texto'
                                halign: 'left'  # Alineación horizontal a la izquierda
                                valign: 'middle'  # Alineación vertical centrada
                                text_size: self.width, None
                    
                    AnchorLayout:
                        size_hint: 1, 0.9
                        anchor_x: 'center'
                        anchor_y: 'center'
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1 
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        
                        BoxLayout:
                            size_hint: None, 0.9
                            size_hint_x: 0.9
                            
                            canvas.before:
                                Color:
                                    rgba: 0.8, 0.8, 0.810, 1
                                Rectangle:
                                    pos: self.pos
                                    size: self.size
                                    
                            BoxLayout:
                                size_hint: 1, 1
                                
                                ScrollView:
                                    size_hint: (1, 1)  # Ajusta al tamaño del contenedor
                                    do_scroll_x: False
                                    do_scroll_y: True
            
                                    TextInput:
                                        id: subVentana_2_ver_texto
                                        text: "Aquí se mostrará el texto extraído."
                                        readonly: True
                                        multiline: True                               
                                
                            #---------------------------------------------------------
                            # SubVentana_2
                            #---------------------------------------------------------
                            # Texto Extraido con TesseracT y mostrado
                            #---------------------------------------------------------
                        

""")



class MisPestanas(TabbedPanel):
    RUTA_IMAGEN_PURA = ""  # Ruta de la imagen seleccionada

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Habilitar soporte para arrastrar y soltar archivos
        Window.bind(on_dropfile=self.cargar_archivo)

    def cargar_archivo(self, window, RUTA_IMAGEN_PURA):
        """Manejar archivos arrastrados a la ventana"""
        RUTA_IMAGEN_PURA = RUTA_IMAGEN_PURA.decode("utf-8")  # Convertir de bytes a string
        self.ids.subVentana_1_Imajen.source = RUTA_IMAGEN_PURA
        self.ids.subVentana_3_Imajen.source = RUTA_IMAGEN_PURA  # Mostrar la imagen arrastrada
        self.RUTA_IMAGEN_PURA = RUTA_IMAGEN_PURA

        # Procesar la imagen con Tesseract
        texto_extraido = self.procesar_imagen_con_tesseract(RUTA_IMAGEN_PURA)
        self.mostrar_texto_pantalla(texto_extraido)

    def seleccionar_imagen(self):
        """Abre un diálogo para seleccionar una imagen."""
        from kivy.uix.filechooser import FileChooserListView

        def on_file_selected(instance, value, touch):
            ruta = value[0] if value else None
            if ruta and self.validar_imagen(ruta):
                self.RUTA_IMAGEN_PURA = ruta
                self.ids.subVentana_1_Imajen.source = ruta
                self.ids.subVentana_3_Imajen.source = ruta

                # Procesar la imagen con Tesseract
                texto_extraido = self.procesar_imagen_con_tesseract(ruta)
                self.mostrar_texto_pantalla(texto_extraido)
            popup.dismiss()

        filechooser = FileChooserListView(filters=['*.png', '*.jpg', '*.jpeg'])
        popup = Popup(title="Seleccionar Imagen", content=filechooser, size_hint=(0.9, 0.9))
        popup.open()
        filechooser.bind(on_submit=on_file_selected)

    def procesar_imagen_con_tesseract(self, ruta):
        """Procesa la imagen seleccionada con Tesseract y extrae texto."""
        tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Cambia según tu sistema
        procesador = ProcesadorDeImagenes()

        try:
            imagen = cv2.imread(ruta)
            texto = procesador.vectorizarTexto(imagen, tesseract_cmd)
            return texto
        except Exception as e:
            print(f"Error procesando la imagen con Tesseract: {e}")
            return "Error al procesar la imagen."

    def validar_imagen(self, ruta):
        """Valida que el archivo sea una imagen y cumpla con las dimensiones mínimas."""
        try:
            imagen = cv2.imread(ruta)
            if imagen is None:
                return False
            alto, ancho, _ = imagen.shape
            return alto >= 100 and ancho >= 100
        except Exception as e:
            print(f"Error validando imagen: {e}")
            return False

    def limpiar_todo(self):
        """Limpia la imagen cargada."""
        self.RUTA_IMAGEN_PURA = ""

        # Limpia la imagen en la interfaz
        self.ids.subVentana_1_Imajen.source = ""
        self.ids.subVentana_3_Imajen.source = ""
        self.ids.subVentana_2_ver_texto.text = ""

    def mostrar_texto_pantalla(self, texto):
        """Actualiza el widget de texto con el contenido recibido."""
        self.ids.subVentana_2_ver_texto.text = texto

    def obtener_ruta_imagen(self):
        """Devuelve la ruta de la imagen cargada."""
        return getattr(self, "RUTA_IMAGEN_PURA", None)


class Iniciar_Pestannas(App):
    def build(self):
        return MisPestanas()


if __name__ == "__main__":
    Iniciar_Pestannas().run()
