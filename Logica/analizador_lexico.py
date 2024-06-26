
import html
from Logica.Estructuras import Token, Reservada, Instruccion, Numero, Palabra, CaracterEspecial, Error
caracteres = []
def clasificar_palabra(palabra, linea_actual, columna_actual):
    caracteres_especiales = ['{', '}', ':', '"', ',', ';', '[', ']','=','.', '#']

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
palabras_procesadas = []
errores = []

def leer_archivo(ruta_archivo):
    palabras_reservadas = ["Inicio", "Encabezado", "Cuerpo", "Titulo", "Fondo", "Parrafo", "Texto", "Codigo", "Negrita", "Subrayado", "Tachado", "Cursiva", "Salto", "Tabla"]
    instrucciones = ["TituloPagina", "texto", "posicion", "tamaño", "color", "cantidad", "elemento", "filas", "columnas"]
    palabras_procesadas = []
    errores = []
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
            palabra_actual = ''
            linea_actual = 1
            columna_actual = 1
            
            for caracter in contenido:
                if caracter == '\n':
                    linea_actual += 1
                    columna_actual = 1
                elif caracter in ['{', '}', ':', '"', ',', ';', '[', ']', '=', '.', '#']:
                    if palabra_actual:
                        if palabra_actual in palabras_reservadas:
                            palabras_procesadas.append(Reservada(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        elif palabra_actual in instrucciones:
                            palabras_procesadas.append(Instruccion(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        elif palabra_actual.isdigit():
                            palabras_procesadas.append(Numero(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        else:
                            palabras_procesadas.append(Palabra(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        palabra_actual = ''
                    palabras_procesadas.append(CaracterEspecial(caracter, linea_actual, columna_actual))
                elif caracter.isalnum():
                    palabra_actual += caracter
                elif caracter.isspace():
                    if palabra_actual:
                        if palabra_actual in palabras_reservadas:
                            palabras_procesadas.append(Reservada(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        elif palabra_actual in instrucciones:
                            palabras_procesadas.append(Instruccion(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        elif palabra_actual.isdigit():
                            palabras_procesadas.append(Numero(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        else:
                            palabras_procesadas.append(Palabra(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                        palabra_actual = ''
                else:
                    errores.append(Error(caracter, 'TIPO_DE_ERROR', linea_actual, columna_actual))
                columna_actual += 1
            
            if palabra_actual:
                if palabra_actual in palabras_reservadas:
                    palabras_procesadas.append(Reservada(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                elif palabra_actual in instrucciones:
                    palabras_procesadas.append(Instruccion(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                elif palabra_actual.isdigit():
                    palabras_procesadas.append(Numero(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                else:
                    palabras_procesadas.append(Palabra(palabra_actual, linea_actual, columna_actual - len(palabra_actual)))
                
            return palabras_procesadas, errores
    except FileNotFoundError:
        print("El archivo no se pudo encontrar.")
        return None, None
    
def buscar_palabras_clave(palabras_procesadas, errores):
    palabras_clave = ["Inicio", "Cuerpo", "Encabezado"]
    
    for palabra_clave in palabras_clave:
        encontrada = False
        for token in palabras_procesadas:
            if token.valor == palabra_clave:
                encontrada = True
                break
        if not encontrada:
            errores.append(Error(palabra_clave, 'NO ENCONTRADO', "NO EXISTE", "NO EXISTE"))



def generar_html_tablas(palabras_procesadas, errores, archivo_salida):
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write('<html>\n')
        f.write('<head><title>Información de Análisis</title>\n')
        f.write('<style>\n')
        f.write('table {margin-left: auto; margin-right: auto; border-collapse: collapse; width: 80%;}\n')
        f.write('th, td {padding: 10px; border: 1px solid black; text-align: center;}\n')
        f.write('h2 {text-align: center;}\n')
        f.write('</style>\n')
        f.write('</head>\n')
        f.write('<body>\n')

        # Tabla de palabras procesadas y caracteres especiales
        f.write('<h2>Palabras Procesadas y Caracteres Especiales</h2>\n')
        f.write('<table>\n')
        f.write('<tr><th>TOKEN</th><th>TIPO</th><th>LÍNEA</th><th>COLUMNA</th></tr>\n')
        for palabra in palabras_procesadas:
            # Escapar caracteres especiales HTML antes de escribirlos en el archivo
            token = html.escape(palabra.valor)
            tipo = html.escape(palabra.tipo)
            f.write(f'<tr><td>{token}</td><td>{tipo}</td><td>{palabra.linea}</td><td>{palabra.columna}</td></tr>\n')
        
        # Incluir caracteres especiales en la tabla
        for caracter in caracteres:
            f.write(f'<tr><td>{html.escape(caracter)}</td><td>CARACTER_ESPECIAL</td><td>-</td><td>-</td></tr>\n')

        f.write('</table>\n')

        # Tabla de errores
        f.write('<h2>Errores</h2>\n')
        f.write('<table>\n')
        f.write('<tr><th>CARACTER</th><th>TIPO</th><th>LÍNEA</th><th>COLUMNA</th></tr>\n')
        for error in errores:
            f.write(f'<tr><td>{error.valor}</td><td>{error.tipo}</td><td>{error.linea}</td><td>{error.columna}</td></tr>\n')
        f.write('</table>\n')
        f.write('</body>\n')
        f.write('</html>\n')



def generar_html_tablas_sin_errores(palabras_procesadas, errores, archivo_salida):
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write('<html>\n')
        f.write('<head><title>Información de Análisis</title>\n')
        f.write('<style>\n')
        f.write('table {margin-left: auto; margin-right: auto; border-collapse: collapse; width: 80%;}\n')
        f.write('th, td {padding: 10px; border: 1px solid black; text-align: center;}\n')
        f.write('h2 {text-align: center;}\n')
        f.write('</style>\n')
        f.write('</head>\n')
        f.write('<body>\n')

        # Tabla de palabras procesadas y caracteres especiales
        f.write('<h2>Palabras Procesadas y Caracteres Especiales</h2>\n')
        f.write('<table>\n')
        f.write('<tr><th>TOKEN</th><th>TIPO</th><th>LÍNEA</th><th>COLUMNA</th></tr>\n')
        for palabra in palabras_procesadas:
            # Escapar caracteres especiales HTML antes de escribirlos en el archivo
            token = html.escape(palabra.valor)
            tipo = html.escape(palabra.tipo)
            f.write(f'<tr><td>{token}</td><td>{tipo}</td><td>{palabra.linea}</td><td>{palabra.columna}</td></tr>\n')
        f.write('</table>\n')

        # Incluir caracteres especiales en la tabla
        for caracter in caracteres:
            f.write(f'<p>{html.escape(caracter)}</p>\n')

        f.write('</body>\n')
        f.write('</html>\n')


def limpiar_listas_secundarias():
    global caracteres, palabras_procesadas, errores
    caracteres.clear()
    palabras_procesadas.clear()
    errores.clear()


































