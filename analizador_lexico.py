def clasificar_palabra(palabra, linea_actual, columna_actual):
    caracteres_especiales = ['{', '}', ':', '"', ',', ';', '[', ']']
    caracteres = []
    tipo_palabra = None
    linea_palabra = linea_actual
    columna_palabra = columna_actual
    
    for caracter in palabra:
        if caracter == '\n':
            linea_palabra += 1
            columna_palabra = 1
        else:
            if caracter in caracteres_especiales:
                caracteres.append((caracter, 'ESPECIAL', linea_palabra, columna_palabra))
            elif caracter.isalpha():
                caracteres.append((caracter, 'LETRA', linea_palabra, columna_palabra))
            elif caracter.isdigit():
                caracteres.append((caracter, 'DIGITO', linea_palabra, columna_palabra))
            else:
                caracteres.append((caracter, 'OTRO', linea_palabra, columna_palabra))
            columna_palabra += 1
    
    # Determinar el tipo de la palabra
    if palabra.startswith('"') and palabra.endswith('"'):
        tipo_palabra = 'CADENA'
    elif palabra.isalpha():
        tipo_palabra = 'IDENTIFICADOR'
    elif palabra.isdigit():
        tipo_palabra = 'NUMERO'
    else:
        tipo_palabra = 'OTRO'

    return caracteres, tipo_palabra, linea_palabra, columna_palabra


def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
            palabras = []
            palabra_actual = ''
            linea_actual = 1
            columna_actual = 1
            
            for caracter in contenido:
                if caracter == '\n':
                    linea_actual += 1
                    columna_actual = 1
                elif caracter in ['{', '}', ':', '"', ',', ';', '[', ']']:
                    if palabra_actual:
                        palabras.append((palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        palabra_actual = ''
                    palabras.append((caracter, linea_actual, columna_actual))
                elif caracter.isspace():
                    if palabra_actual:
                        palabras.append((palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        palabra_actual = ''
                else:
                    palabra_actual += caracter
                columna_actual += 1
            
            if palabra_actual:
                palabras.append((palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                
            return palabras
    except FileNotFoundError:
        print("El archivo no se pudo encontrar.")
        return None

ruta_archivo = "prueba.txt"  # Cambia esto por la ruta del archivo seleccionado
palabras = leer_archivo(ruta_archivo)

if palabras:
    for palabra, linea, columna in palabras:
        print(f'Palabra: {palabra}, Línea: {linea}, Columna: {columna}')

