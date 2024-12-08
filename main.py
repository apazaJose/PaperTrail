import os
import cv2
import pytesseract
import shutil
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Función para preprocesar la imagen
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Escala de grises
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)    # Desenfoque para reducir ruido
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Binarización
    return thresh


# Función para extraer características basadas en texto
def extract_text_features(image):
    text = pytesseract.image_to_string(image, lang="esp")  # Cambia "eng" por "spa" si es español
    return {"text_length": len(text), "keywords": text.lower().count("factura")}


# Función para extraer características visuales
def extract_visual_features(image):
    edges = cv2.Canny(image, 100, 200)  # Detectar bordes
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_contours = len(contours)  # Número de contornos como característica
    return {"num_contours": num_contours}


# Función para clasificar un documento
def classify_document(image_path, model):
    # Preprocesar la imagen
    preprocessed_image = preprocess_image(image_path)

    # Extraer características
    text_features = extract_text_features(preprocessed_image)
    visual_features = extract_visual_features(preprocessed_image)

    # Combinar características
    features = list(text_features.values()) + list(visual_features.values())

    # Predecir la categoría
    category = model.predict([features])[0]
    print(f"El documento '{os.path.basename(image_path)}' pertenece a la categoría: '{category}'")
    return category


# Función para leer documentos desde un directorio
def get_documents_from_directory(directory):
    documents = []
    for file in os.listdir(directory):
        if file.endswith((".png", ".jpg", ".jpeg", ".pdf")):  # Tipos de archivos soportados
            documents.append(os.path.join(directory, file))
    return documents


# Función para clasificar y organizar documentos
def classify_and_organize_documents(directory, model):
    documents = get_documents_from_directory(directory)
    
    for document in documents:
        # Clasificar el documento
        category = classify_document(document, model)
        
        # Crear carpeta si no existe
        category_folder = os.path.join(directory, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        
        # Mover archivo a la carpeta correspondiente
        shutil.move(document, os.path.join(category_folder, os.path.basename(document)))
        print(f"Documento '{os.path.basename(document)}' clasificado como '{category}' y movido a '{category_folder}'")


# Función para entrenar el modelo (simulación)
def train_classifier():
    # ejemplo 
    X = [
        [50, 5], 
        [200, 15],
        [120, 10],
    ]
    y = ["factura", "nota", "receta"]  # Etiquetas de documentos

    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar el clasificador
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred = clf.predict(X_test)
    print("Precisión del modelo:", accuracy_score(y_test, y_pred))
    return clf


# Punto de entrada del programa
if __name__ == '__main__':
    print("Entrenando modelo...")
    model = train_classifier()

    # Directorio donde están los documentos
    document_directory = "C:\\Users\\HP VICTUS\\Documents\\ia" #direccion donde guardar los archivos

    print("Clasificando y organizando documentos...")
    classify_and_organize_documents(document_directory, model)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
