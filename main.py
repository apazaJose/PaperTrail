



 #def main():
  #  # Configurar OCR con la ruta de Tesseract
   # tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #image = cv2.imread(r'C:\Users\Gustavo\Downloads\WhatsApp Image 2024-11-26 at 18.38.06.jpeg')
    #Cambiar las rutas a las rutas que maneja cada uno
    #procesador = ProcesadorDeImagenes()
    #vectorImagen = procesador.vectorizarTextoImagenProcesada(image,tesseract_cmd)
    #print(vectorImagen)

from src.application.services.ProcesadorDeImagenes import ProcesadorDeImagenes
import cv2
from src.application.services.GetRutasIamgenes import obtener_imagenes
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from src.application.gui.main_view import MisPestanas
import os


class IniciarPestanas(App):
    kmeans = None
    organizer = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.texto_1 = None
        self.texto_2 = None

    # -- Metodo Para Limpiar Todo
    #-------------------------------------------------------------------------------------------------
    def limpiar_imagen(self, instance):
        print("llamando a Borra de Main")
        self.root.limpiar_todo()





    # Cuando se (PRESIONA) el (BOTON), (Filtrar)
    # Al finalisar llama al metodo de tesseract
    # -------------------------------------------------------------------------------------------------
    def filtrar_imagen(self):
        texto = "Boton de Filtros"
        self.mostrar_popup(texto)
        self.root.mostrar_texto_pantalla(texto)




    # Funcion para Guardar txt
    # -------------------------------------------------------------------------------------------------
    def guardar_texto_a_txt(self):
        # Verificar si hay texto disponible para guardar
        print("llamando a guardar texto a txt de Main")

        # Accede a la instancia de MisPestanas y su atributo RUTA_IMAGEN_PURA
        # Accede a la instancia de MisPestanas y su atributo RUTA_IMAGEN_PURA
        ruta_imagen = self.root.RUTA_IMAGEN_PURA

        if ruta_imagen:
            texto_procesado = f"¡Imagen cargada! Ruta: {ruta_imagen}"
        else:
            texto_procesado = "No hay imagen"

        # Mostrar el texto procesado en un Popup como ejemplo
        self.mostrar_popup(texto_procesado)




    # Funcion Ficticia de Prediccion y Muetestra Resultado
    # -------------------------------------------------------------------------------------------------
    def funcion_predictoria(self):
        # Función que devuelve un texto
        texto_resultado = self.mi_funcion_logica()
        self.mostrar_popup(texto_resultado)

    def mi_funcion_logica(self):
        # Aquí puedes realizar cualquier operación
        return "Texto generado por la función."

    def mostrar_popup(self, texto):
        # Crear un Popup para mostrar el texto
        popup = Popup(title='Resultado',
                      content=Label(text=texto),
                      size_hint=(0.4, 0.3),
                      auto_dismiss=True)
        popup.open()

    def funcion_apresurada(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Campo de texto 1
        layout.add_widget(Label(text="Ingrese número de clusters", size_hint=(1, 0.2)))
        input_texto_1 = TextInput(hint_text="ejem: 3", size_hint=(1, 0.2))
        layout.add_widget(input_texto_1)

        # Campo de texto 2
        layout.add_widget(Label(text="Ingrese la dirección de las imágenes:", size_hint=(1, 0.2)))
        input_texto_2 = TextInput(hint_text="C:\Windows", size_hint=(1, 0.2))
        layout.add_widget(input_texto_2)

        # Botón para guardar
        def guardar_textos(instance):
            self.texto_1 = input_texto_1.text
            self.texto_2 = input_texto_2.text

            # Validar que el número de clusters sea un entero
            if not self.texto_1.isdigit():
                print("El número de clusters debe ser un número entero.")
                return

            # Validar que la ruta exista
            if not os.path.isdir(self.texto_2):
                print("La ruta proporcionada no es válida.")
                return

            # Llamar a la función para obtener imágenes, esta es la funcion aqui instanciar kmeansy organicer
            imagenes, kmeans, organizer = obtener_imagenes(self.texto_2,self.texto_1)

            self.kmeans = kmeans
            self.organizer = organizer

            for imagen in imagenes:
                print(imagen)

            popup.dismiss()

        guardar_button = Button(text="Guardar", size_hint=(1, 0.2))
        guardar_button.bind(on_press=guardar_textos)
        layout.add_widget(guardar_button)

        # Crear el Popup
        popup = Popup(
            title="Ingresar datos",
            content=layout,
            size_hint=(0.8, 0.6),
            auto_dismiss=False
        )
        popup.open()
    def build(self):
        print("Construyendo la interfaz...")
        return MisPestanas()

if __name__ == "__main__":
    print("Iniciando la aplicación...")
    IniciarPestanas().run()

