import os
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Datos ficticios: textos de ejemplo y etiquetas
def get_sample_data():
    documents = [
        "Factura de compra total $100 cliente Pedro",
        "Receta médica paciente Juan medicamento Paracetamol",
        "Formulario de solicitud de vacaciones empleado Carlos",
        "Nota informativa sobre nuevas políticas de la empresa",
        "Factura de compra total $200 cliente María",
        "Receta médica paciente Ana medicamento Ibuprofeno",
    ]
    labels = ["factura", "receta", "formulario", "nota", "factura", "receta"]

    return documents, labels

def train_classifier(model_type="nb"):
    print("Entro a la funcion")
    # Obtener datos de ejemplo
    documents, labels = get_sample_data()

    # Paso 1: Vectorización del texto
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)  # Transformar textos a vectores TF-IDF
    y = np.array(labels)  # Convertir etiquetas a formato numpy

    # Paso 2: Dividir datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Paso 3: Entrenar el modelo supervisado
    if model_type == "nb":
        model = MultinomialNB()  # Naive Bayes
    elif model_type == "svm":
        model = SVC(kernel="linear", probability=True)  # SVM
    else:
        raise ValueError("Tipo de modelo no soportado. Use 'nb' o 'svm'.")

    model.fit(X_train, y_train)

    # Paso 4: Evaluar el modelo
    y_pred = model.predict(X_test)
    print("Reporte de clasificación:")  
    print(classification_report(y_test, y_pred))    
    print("Precisión:", accuracy_score(y_test, y_pred))

    # Paso 5: Guardar el modelo y el vectorizador
    model_path = os.path.join(os.path.dirname(__file__), f"{model_type}_classifier.pkl")
    vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

    with open(model_path, "wb") as model_file:
        pickle.dump(model, model_file)

    with open(vectorizer_path, "wb") as vec_file:
        pickle.dump(vectorizer, vec_file)

    print(f"Modelo guardado en: {model_path}")
    print(f"Vectorizador guardado en: {vectorizer_path}")


def classify_document(text, model_type="nb"):
    # Cargar el modelo y el vectorizador
    model_path = os.path.join(os.path.dirname(__file__), f"{model_type}_classifier.pkl")
    vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)

    with open(vectorizer_path, "rb") as vec_file:
        vectorizer = pickle.load(vec_file)

    # Transformar el texto de entrada y hacer la predicción
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return prediction
