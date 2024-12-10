
# Creación del Entorno Virtual (venv)

Abran un cmd en la direccion de la direccion de el proyecto y siguan los siguientes pasos 
## 1. Verificar la instalación de Python

Usaremos python 3.10

Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando el siguiente comando en tu terminal o línea de comandos:

```bash
python3 --version
```

## 2. Crear el entorno virtual

Dentro de la carpeta raíz de tu proyecto, ejecuta el siguiente comando para crear un entorno virtual llamado `venv`:

- En sistemas Windows:
  ```bash
  python -m venv venv
  ```

- En sistemas Linux o macOS:
  ```bash
  python3 -m venv venv
  ```

Esto creará una carpeta llamada `venv` que contendrá el entorno virtual.

## 3. Activar el entorno virtual

Para activar el entorno virtual, usa uno de los siguientes comandos según tu sistema operativo:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

Después de activar el entorno virtual, deberías ver algo como `(venv)` al inicio de tu línea de comandos.

## 4. Instalar dependencias

Con el entorno virtual activado, instala las dependencias necesarias para el proyecto usando el archivo `requirements.txt` (si está disponible):

```bash
pip install -r requirements.txt
```

## 5. Desactivar el entorno virtual

Cuando termines de trabajar, desactiva el entorno virtual ejecutando:

```bash
deactivate
```

¡Eso es todo! Ahora tienes un entorno virtual configurado para tu proyecto.

## 6. Instalar Tesseract
Es necesario instalar Tesseract para poder usar pytesseract
* Link de descarga para windows: https://github.com/UB-Mannheim/tesseract/wiki
* Descargar el instalador .exe del programa 
* Ejecutar el instalador de tesseract
  * Presionar boton siguiente
  * Aceptar Terminos y condiciones
  * Presionar boton aceptar
  * Seleccionar la opcion de instalar para cualquier ususario
  * Presionar boton siguiente
  * Presionar el icono de [+] en la opcion de 'Aditional language data'
    * Marcar el check [ ] de 'Math/equation detection module' 
    * Marcar el check [ ] de 'Spanish' para el idioma espaniol
    * Presionar el boton siguiente
* Instalar el programa en la ruta por defecto (C:\Program Files\Tesseract-OCR)
* Presionar boton siguiente
* Presionar boton instalar
* Presionar e boton terminar
* Para MacOs
  ```bash
  brew install tesseract
  ```

¡Eso es todo! Ahora tienes tesseract para tu proyecto.

## 7. Ejecutar el programa
Es necesario tener activado el entorno virtual de python, si ya creaste uno puedes ejecutar lo siguiente dentro el directorio que estes usando para ejecutar el programa:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```
Una vez activado el entorno virtual ejecutar lo siguiente:
  ```
 (venv) PS D:\reemplazar por tu directorio> python main.py 
 
  ```
Ejemplo de uso:
  ```
 (venv) PS D:\Ingenieria de Sistemas II-2024\IA\Ia2\PaperTrail> python main.py 
 
  ```
¡Eso es todo! Ahora puedes empezar a probar el proyecto.

Dudas o consultas comunicarse al WhatsApp: 67508670
  