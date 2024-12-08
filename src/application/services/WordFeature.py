import re

def contar_lineas(texto: str) -> int:
    lineas = texto.splitlines()
    return len(lineas)

def tamaño_promedio_palabras(texto: str) -> float:
    palabras = texto.split()
    if palabras:
        return sum(len(palabra) for palabra in palabras) / len(palabras)
    return 0.0



def contar_palabras(texto: str) -> int:
    palabras = texto.split()
    return len(palabras)

def contar_numeros(texto: str) -> int:
    numeros = re.findall(r'\d+', texto)
    return len(numeros)

def contar_fechas(texto: str) -> int:
    fechas = re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2}\b', texto)
    return len(fechas)
