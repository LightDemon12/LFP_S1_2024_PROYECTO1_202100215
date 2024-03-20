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
    elif palabra.isalpha() and not palabra.isdigit():
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
                        tipo_palabra = 'PALABRA' if not palabra_actual.isdigit() else ('DIGITO' if palabra_actual.isnumeric() else 'DIGITO')
                        palabras.append((palabra_actual, tipo_palabra, linea_actual, columna_actual - len(palabra_actual)))
                        for i, letra in enumerate(palabra_actual):
                            tipo_caracter = 'CARACTER' if not letra.isdigit() else 'NUMERO'
                            palabras.append((letra, tipo_caracter, linea_actual, columna_actual - len(palabra_actual) + i))
                        palabra_actual = ''
                    palabras.append((caracter, 'CARACTER_ESPECIAL', linea_actual, columna_actual))
                elif caracter.isalnum():
                    palabra_actual += caracter
                elif caracter.isspace():
                    if palabra_actual:
                        tipo_palabra = 'PALABRA' if not palabra_actual.isdigit() else ('DIGITO' if palabra_actual.isnumeric() else 'DIGITO')
                        palabras.append((palabra_actual, tipo_palabra, linea_actual, columna_actual - len(palabra_actual)))
                        for i, letra in enumerate(palabra_actual):
                            tipo_caracter = 'CARACTER' if not letra.isdigit() else 'DIGITO'
                            palabras.append((letra, tipo_caracter, linea_actual, columna_actual - len(palabra_actual) + i))
                        palabra_actual = ''
                else:
                    palabras.append((caracter, 'ERROR', linea_actual, columna_actual))
                columna_actual += 1
            
            if palabra_actual:
                tipo_palabra = 'PALABRA' if not palabra_actual.isdigit() else ('DIGITO' if palabra_actual.isnumeric() else 'DIGITO')
                palabras.append((palabra_actual, tipo_palabra, linea_actual, columna_actual - len(palabra_actual)))
                for i, letra in enumerate(palabra_actual):
                    tipo_caracter = 'CARACTER' if not letra.isdigit() else 'NUMERO'
                    palabras.append((letra, tipo_caracter, linea_actual, columna_actual - len(palabra_actual) + i))
                
            return palabras
    except FileNotFoundError:
        print("El archivo no se pudo encontrar.")
        return None
