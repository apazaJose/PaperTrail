from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import matplotlib.pyplot as plt
from ...domain.entities.imagenProcessor.evaluation_graphs import generate_confusion_matrix, generate_cluster_plot

class EvaluationWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Generar los gráficos y guardarlos como imágenes
        generate_confusion_matrix()  # Llamada a la función de generación de matriz de confusión
        generate_cluster_plot()  # Llamada a la función de generación de gráfico de clusters

        # Mostrar los gráficos generados en la vista
        self.add_widget(Image(source="confusion_matrix.png"))  # Mostrar la matriz de confusión
        self.add_widget(Image(source="cluster_plot.png"))  # Mostrar el gráfico de clusters

class EvaluationApp(App):
    def build(self):
        return EvaluationWindow()

if __name__ == "__main__":
    EvaluationApp().run()
