from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from src.application.gui.main_view import MisPestanas


class IniciarPestanas(App):



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




    def build(self):
        print("Construyendo la interfaz...")
        return MisPestanas()

if __name__ == "__main__":
    print("Iniciando la aplicación...")
    IniciarPestanas().run()

