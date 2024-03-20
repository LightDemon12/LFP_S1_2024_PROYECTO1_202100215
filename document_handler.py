import tkinter as tk
from tkinter import filedialog
from estructuras import BloqueInicio, BloqueEncabezado, BloqueCuerpo, Titulo, Fondo, Parrafo, Texto, Codigo, Negrita, Subrayado, Tachado, Cursiva, Salto, Tabla


def abrir_documento():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    # Abrir un cuadro de diálogo para seleccionar un archivo
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

    if ruta_archivo:
        print("Documento abierto:", ruta_archivo)
        return ruta_archivo  # Devolver la ruta del archivo seleccionado
    else:
        print("No se seleccionó ningún documento.")
        return None

    
# Definición de las palabras clave 

# Lista para almacenar instancias de la clase BloqueInicio
list_inicio = []
# Lista para almacenar instancias de la clase BloqueEncabezado
list_encabezado = []
# Lista para almacenar instancias de la clase BloqueCuerpo
list_cuerpo = []
# Lista para almacenar instancias de la clase BloqueTituloPagina
list_titulo_pagina = []
# Lista para almacenar instancias de la clase BloqueTitulo
list_titulo = []
# Lista para almacenar instancias de la clase BloqueFondo
list_fondo = []
# Lista para almacenar instancias de la clase BloqueParrafo
list_parrafo = []
# Lista para almacenar instancias de la clase BloqueTexto
list_texto = []
# Lista para almacenar instancias de la clase BloqueCodigo
list_codigo = []
# Lista para almacenar instancias de la clase BloqueNegrita
list_negrita = []
# Lista para almacenar instancias de la clase BloqueSubrayado
list_subrayado = []
# Lista para almacenar instancias de la clase BloqueTachado
list_tachado = []
# Lista para almacenar instancias de la clase BloqueCursiva
list_cursiva = []
# Lista para almacenar instancias de la clase BloqueSalto
list_salto = []
# Lista para almacenar instancias de la clase BloqueTabla
list_tabla = []


def procesar_inicio(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Inicio': {linea}")

def procesar_encabezado(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Encabezado': {linea}")

def procesar_titulo_pagina(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'TituloPagina': {linea}")

def procesar_cuerpo(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Cuerpo': {linea}")

def procesar_titulo(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Titulo': {linea}")

def procesar_fondo(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Fondo': {linea}")

def procesar_parrafo(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Parrafo': {linea}")

def procesar_texto(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Texto': {linea}")

def procesar_codigo(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Codigo': {linea}")

def procesar_negrita(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Negrita': {linea}")

def procesar_subrayado(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Subrayado': {linea}")

def procesar_tachado(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Tachado': {linea}")

def procesar_cursiva(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Cursiva': {linea}")

def procesar_salto(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Salto': {linea}")

def procesar_tabla(linea, numero_linea):
    print(f"Procesando línea {numero_linea} para 'Tabla': {linea}")

# Define el diccionario con las palabras clave y las funciones correspondientes


def procesar_documento(documento):
    palabras_clave = {
        "Inicio": procesar_inicio,
        "Encabezado": procesar_encabezado,
        "TituloPagina": procesar_titulo_pagina,
        "Cuerpo": procesar_cuerpo,
        "Titulo": procesar_titulo,
        "Fondo": procesar_fondo,
        "Parrafo": procesar_parrafo,
        "Texto": procesar_texto,
        "Codigo": procesar_codigo,
        "Negrita": procesar_negrita,
        "Subrayado": procesar_subrayado,
        "Tachado": procesar_tachado,
        "Cursiva": procesar_cursiva,
        "Salto": procesar_salto,
        "Tabla": procesar_tabla
    }
    
    # Mantener seguimiento del nivel de anidamiento y la fila actual
    nivel_anidamiento = 0
    fila_actual = 0
    # Pila para rastrear los bloques abiertos
    pila_bloques = []
    
    for linea in documento:
        # Incrementar el número de fila
        fila_actual += 1
        # Eliminar espacios en blanco al principio y al final de la línea
        linea = linea.strip()

        # Verificar si la línea es un bloque de apertura
        if linea.endswith("{") or linea.endswith("["):
            nivel_anidamiento += 1
            pila_bloques.append((linea, fila_actual))
            print(f"Se abrió un bloque en el nivel {nivel_anidamiento}")

        # Verificar si la línea es un bloque de cierre
        elif linea.endswith("}") or (linea.endswith(",") and linea[:-1].endswith("}")) or linea.endswith("]"):
            nivel_anidamiento -= 1
            if nivel_anidamiento < 0:
                print(f"Error en la fila {fila_actual}: Demasiados cierres de bloques")
                break
            
            if pila_bloques:
                bloque_abierto, fila_bloque_abierto = pila_bloques.pop()
                bloque_cierre = linea[-1]
                print(f"Se cerró el bloque {bloque_cierre} en el nivel {nivel_anidamiento} (fila {fila_actual})")
                # Extraer la palabra clave del bloque abierto
                palabra_clave = bloque_abierto.strip(":,{}[]")
                # Llamar a la función asociada con la palabra clave del bloque abierto
                if palabra_clave in palabras_clave:
                    funcion = palabras_clave[palabra_clave]
                    if funcion:
                        funcion(linea, fila_actual)  # Pasar la línea y el número de fila como argument
        else:
            # Si no es un bloque de apertura o cierre, y estamos en el nivel de anidamiento 1,
            # verificamos si la línea es una palabra clave para procesarla
            if nivel_anidamiento == 1:
                palabra = linea.split(":")[0].strip()
                if palabra in palabras_clave:
                    funcion = palabras_clave[palabra]
                    if funcion:
                        funcion(linea, fila_actual)






