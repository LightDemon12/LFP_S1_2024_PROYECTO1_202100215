
class Encabezado:
    def __init__(self, titulo_pagina):
        self.titulo_pagina = titulo_pagina
        self.instruccion = "encabezado"
    def __str__(self):
        return f'<title>{self.titulo_pagina}</title>'

class Titulo:
    def __init__(self, texto, posicion, tamaño, color):
        self.texto = texto
        self.posicion = posicion
        self.tamaño = tamaño
        self.color = color
        self.instruccion = "titulo"
    def __str__(self):
        return f'<{self.tamaño}><p align ="{self.posicion}"style="color: {self.color};, ">   {self.texto}  </p></{self.tamaño}>'

class Fondo:
    def __init__(self, color):
        self.color = color
        self.instruccion = "fondo"
    def __str__(self):
        return f'<style>body{{background-color: {self.color};}}</style>'

class Parrafo:
    def __init__(self, texto, posicion):
        self.texto = texto
        self.posicion = posicion
        self.instruccion = "parrafo"
    def __str__(self):
        return f'<p align="{self.posicion}">{self.texto}</p>'

class Texto:
    def __init__(self, fuente, color, tamaño):
        self.fuente = fuente
        self.color = color
        self.tamaño = tamaño
        self.instruccion = "texto"
        self.texto = "Lorem ipsum dolor sit amet"
    def __str__(self):
        return f'<span style="font-family: {self.fuente}; color: {self.color}; font-size: {self.tamaño}px;">{self.texto}</span>'

class Codigo:
    def __init__(self, texto, posicion):
        self.texto = texto
        self.posicion = posicion
        self.instruccion = "codigo"
    def __str__(self):
        return f'<div style="text-align: {self.posicion}; font-family: monospace;">{self.texto}</div>'

class Negrita:
    def __init__(self, texto):
        self.texto = texto
        self.instruccion = "negrita"
    def __str__(self):
        return f'<b>{self.texto}</b><br>'

class Subrayado:
    def __init__(self, texto):
        self.texto = texto
        self.instruccion = "subrayado"
    def __str__(self):
        return f'<u>{self.texto}</u><br>'

class Tachado:
    def __init__(self, texto):
        self.texto = texto
        self.instruccion = "tachado"
    def __str__(self):
        return f'<s>{self.texto}</s><br>'

class Cursiva:
    def __init__(self, texto):
        self.texto = texto
        self.instruccion = "cursiva"
    def __str__(self):
        return f'<i>{self.texto}</i><br>'

class Salto:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.instruccion = "salto"
    def __str__(self):
        salto = ""
        for _ in range(int(self.cantidad)):
            salto += "<br>\n"
        return salto

class Tabla:
    def __init__(self, filas, columnas, elementos):
        self.filas = filas
        self.columnas = columnas
        self.elementos = elementos
        self.instruccion = "tabla"

    def __str__(self):
        # Código para representar una tabla en HTML
        return f'<td>|{self.filas} {self.columnas} {self.elementos}|</td>'


Estructura = []
EncabezadoTitulo = []
# Diccionario para mapear las instrucciones de posición a HTML
instrucciones_posicion_html = {
    "izquierda": "left",
    "derecha": "right",
    "centro": "center"
}
# Diccionario para mapear las instrucciones de tamaño a HTML
instrucciones_tamaño_html = {
    "t1": "h1",
    "t2": "h2",
    "t3": "h3",
    "t4": "h4",
    "t5": "h5",
    "t6": "h6"
}
# Diccionario para mapear las instrucciones de color a HTML
instrucciones_color_html = {
    "rojo": "red",
    "azul": "blue",
    "verde": "green"
}

def procesar_bloque_titulo(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    # Inicializar los atributos del título
    texto = None
    posicion = None
    tamaño = None
    color = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "texto" in linea:
            texto = linea.split('"')[1]
        elif "posicion" in linea:
            posicion = linea.split('"')[1]
            # Convertir posición a su equivalente HTML si existe
            posicion_html = instrucciones_posicion_html.get(posicion)
            if posicion_html:
                posicion = posicion_html
        elif "tamaño" in linea:
            tamaño = linea.split('"')[1]
            # Convertir tamaño a su equivalente HTML si existe
            tamaño_html = instrucciones_tamaño_html.get(tamaño)
            if tamaño_html:
                tamaño = tamaño_html
        elif "color" in linea:
            color = linea.split('"')[1]
            # Convertir color a su equivalente HTML si existe
            color_html = instrucciones_color_html.get(color)
            if color_html:
                color = color_html
    # Crear un objeto de la clase Titulo con la información obtenida
    nuevo_titulo = Titulo(texto, posicion, tamaño, color)
    # Agregar el nuevo título a la lista Estructura
    Estructura.append(nuevo_titulo)

def procesar_bloque_encabezado(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    # Inicializar el atributo del encabezado
    titulo_pagina = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "TituloPagina" in linea:
            titulo_pagina = linea.split('"')[1]
    # Crear un objeto de la clase Encabezado con la información obtenida
    nuevo_encabezado = Encabezado(titulo_pagina)
    # Agregar el nuevo encabezado a la lista EncabezadoTitulo
    EncabezadoTitulo.append(nuevo_encabezado)

def procesar_bloque_fondo(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    # Inicializar el atributo del fondo
    color = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "color" in linea:
            color = linea.split('"')[1]
            # Convertir color a su equivalente HTML si existe
            color_html = instrucciones_color_html.get(color)
            if color_html:
                color = color_html
    # Crear un objeto de la clase Fondo con la información obtenida
    nuevo_fondo = Fondo(color)
    # Agregar el nuevo fondo a la lista Estructura
    Estructura.append(nuevo_fondo)

def procesar_bloque_parrafo(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    # Inicializar los atributos del párrafo
    texto = None
    posicion = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "texto" in linea:
            texto = linea.split('"')[1]
        elif "posicion" in linea:
            posicion = linea.split('"')[1]
            # Convertir posición a su equivalente HTML si existe
            posicion_html = instrucciones_posicion_html.get(posicion)
            if posicion_html:
                posicion = posicion_html
    # Crear un objeto de la clase Parrafo con la información obtenida
    nuevo_parrafo = Parrafo(texto, posicion)
    # Agregar el nuevo párrafo a la lista Estructura
    Estructura.append(nuevo_parrafo)

def procesar_bloque_texto(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    # Inicializar los atributos del texto
    fuente = None
    color = None
    tamaño = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "fuente" in linea:
            fuente = linea.split('"')[1]
        elif "color" in linea:
            color = linea.split('"')[1]
            # Convertir color a su equivalente HTML si existe
            color_html = instrucciones_color_html.get(color)
            if color_html:
                color = color_html
        elif "tamaño" in linea:
            tamaño = linea.split('"')[1]
            # Convertir tamaño a su equivalente HTML si existe
            tamaño_html = instrucciones_tamaño_html.get(tamaño)
            if tamaño_html:
                tamaño = tamaño_html
    # Crear un objeto de la clase Texto con la información obtenida
    nuevo_texto = Texto(fuente, color, tamaño)
    # Agregar el nuevo texto a la lista Estructura
    Estructura.append(nuevo_texto)

def procesar_bloque_codigo(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    # Inicializar los atributos del código
    texto = None
    posicion = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "texto" in linea:
            texto = linea.split('"')[1]
        elif "posicion" in linea:
            posicion = linea.split('"')[1]
            # Convertir posición a su equivalente HTML si existe
            posicion_html = instrucciones_posicion_html.get(posicion)
            if posicion_html:
                posicion = posicion_html
    # Crear un objeto de la clase Codigo con la información obtenida
    nuevo_codigo = Codigo(texto, posicion)
    # Agregar el nuevo código a la lista Estructura
    Estructura.append(nuevo_codigo)

def procesar_bloque_negrita(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    
    # Inicializar el atributo de la negrita
    texto = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "texto" in linea:
            texto = linea.split('"')[1]
    # Crear un objeto de la clase Negrita con la información obtenida
    nuevo_negrita = Negrita(texto)
    # Agregar el nuevo texto a la lista Estructura
    Estructura.append(nuevo_negrita)

def procesar_bloque_subrayado(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    # Inicializar el atributo del subrayado
    texto = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "texto" in linea:
            texto = linea.split('"')[1]
    # Crear un objeto de la clase Subrayado con la información obtenida
    nuevo_subrayado = Subrayado(texto)
    # Agregar el nuevo subrayado a la lista Estructura
    Estructura.append(nuevo_subrayado)

def procesar_bloque_tachado(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    # Inicializar el atributo del tachado
    texto = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "texto" in linea:
            texto = linea.split('"')[1]
    # Crear un objeto de la clase Tachado con la información obtenida
    nuevo_tachado = Tachado(texto)
    # Agregar el nuevo tachado a la lista Estructura
    Estructura.append(nuevo_tachado)

def procesar_bloque_cursiva(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")
    # Inicializar el atributo de la cursiva
    texto = None
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "texto" in linea:
            texto = linea.split('"')[1]
    # Crear un objeto de la clase Cursiva con la información obtenida
    nuevo_cursiva = Cursiva(texto)
    # Agregar el nuevo cursiva a la lista Estructura
    Estructura.append(nuevo_cursiva)

def procesar_bloque_salto(bloque):
    # Dividir el bloque en líneas
    lineas = bloque.split(";")   
    # Inicializar el atributo del salto
    cantidad = None   
    # Recorrer cada línea y extraer la información entre comillas
    for linea in lineas:
        if "cantidad" in linea:
            cantidad_str = linea.split('"')[1]
            cantidad = int(cantidad_str) if cantidad_str.isdigit() else None   
    # Crear un objeto de la clase Salto con la información obtenida
    nuevo_salto = Salto(cantidad)   
    # Agregar el nuevo salto a la lista Estructura
    Estructura.append(nuevo_salto)
    
def procesar_bloque_elemento(bloque, Estructura):

    print(bloque)
    
    # Copiar el bloque de texto a una variable de cadena (str)
    bloque_str = bloque.strip()
    
    # Reemplazar las comas por saltos de línea
    bloque_str = bloque_str.replace(",", "\n")
    
    # Eliminar las comillas dobles y cualquier texto innecesario
    bloque_str = bloque_str.replace('"', '').replace('fila:', '').replace('columna:', '').strip()
    

    
    # Dividir el bloque en líneas individuales
    lineas = bloque_str.split("\n")

    for i, linea in enumerate(lineas):

        # Si es la primera línea, convertir a entero y asignar a fila
        if i == 0:
            fila = int(linea)
        # Si es la segunda línea, convertir a entero y asignar a columna
        elif i == 1:
            columna = int(linea)
        # Si es la tercera línea, asignar como está a elemento
        elif i == 2:
            elemento = linea
            
            # Crear un objeto de la clase Tabla con la información obtenida
            nueva_tabla = Tabla(fila, columna, elemento)
            
            # Agregar el objeto de Tabla a la lista Estructura
            Estructura.append(nueva_tabla)
    
    return lineas



















def leer_documento(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            
            # Lista de palabras clave
            palabras_clave = ["Encabezado", "Titulo", "Fondo", "Parrafo", "Texto", "Codigo", "Negrita", "Subrayado", "Tachado", "Cursiva", "Salto", "elemento"]
            
            # Diccionario para almacenar los bloques procesados junto con su posición
            bloques_procesados = {}
            
            # Bucle para buscar y procesar todas las ocurrencias de cada palabra clave
            for palabra_clave in palabras_clave:
                indice_busqueda = 0
                while True:
                    indice_palabra_clave = contenido.find(palabra_clave, indice_busqueda)
                    if indice_palabra_clave != -1:
                        inicio_bloque = contenido.find("{", indice_palabra_clave)
                        fin_bloque = contenido.find("}", inicio_bloque)
                        if inicio_bloque != -1 and fin_bloque != -1:
                            bloque = contenido[inicio_bloque + 1:fin_bloque]
                            # Almacenar el bloque junto con su posición
                            bloques_procesados[(palabra_clave, indice_palabra_clave)] = bloque
                            # Actualizar el índice de búsqueda para la próxima iteración
                            indice_busqueda = fin_bloque + 1
                        else:
                            break  # Si no se encuentra el bloque, salir del bucle while
                    else:
                        break  # Si no se encuentra la palabra clave, salir del bucle while
            
            # Ordenar los bloques procesados por su posición en el archivo
            bloques_ordenados = sorted(bloques_procesados.items(), key=lambda x: x[0][1])
            
            # Procesar los bloques en el orden correcto
            for clave, bloque in bloques_ordenados:
                palabra_clave, _ = clave
                print(bloque)
                # Llamar a la función para procesar el bloque correspondiente
                if palabra_clave == "Encabezado":
                    procesar_bloque_encabezado(bloque)
                elif palabra_clave == "Titulo":
                    procesar_bloque_titulo(bloque)
                elif palabra_clave == "Fondo":
                    procesar_bloque_fondo(bloque)
                elif palabra_clave == "Parrafo":
                    procesar_bloque_parrafo(bloque)
                elif palabra_clave == "Texto":
                    procesar_bloque_texto(bloque)
                elif palabra_clave == "Codigo":
                    procesar_bloque_codigo(bloque)
                elif palabra_clave == "Negrita":
                    procesar_bloque_negrita(bloque)
                elif palabra_clave == "Subrayado":
                    procesar_bloque_subrayado(bloque)
                elif palabra_clave == "Tachado":
                    procesar_bloque_tachado(bloque)
                elif palabra_clave == "Cursiva":
                    procesar_bloque_cursiva(bloque)
                elif palabra_clave == "Salto":
                    procesar_bloque_salto(bloque)
                elif palabra_clave == "elemento":
                    procesar_bloque_elemento(bloque, Estructura)
            # Imprimir los elementos de la estructura después de procesar todos los bloques
            for elemento in Estructura:
                print(elemento)
            for elemento in EncabezadoTitulo:
                print(elemento)
    except FileNotFoundError:
        print("El archivo no pudo ser encontrado.")










def crear_html(nombre_archivo2):
    try:
        with open(nombre_archivo2, "w", encoding="utf-8") as archivo:
            archivo.write("""
<!DOCTYPE html>
<html>
<head>

""")
            # Imprimir los elementos de la lista EncabezadoTitulo
            for elemento in EncabezadoTitulo:
                archivo.write(str(elemento))
                archivo.write("\n")  # Agregar un salto de línea después de cada elemento
            
            archivo.write("""
</head>
<body>
""")
            # Imprimir los elementos de la estructura después de procesar todos los bloques
            for elemento in Estructura:
                archivo.write(str(elemento))
                archivo.write("\n")  # Agregar un salto de línea después de cada elemento
            
            archivo.write("""
</body>
</html>
""")
        print(f"Se ha creado el archivo HTML '{nombre_archivo2}' correctamente.")
    except Exception as e:
        print(f"No se pudo crear el archivo HTML: {e}")



def limpiar_listas():
    global Estructura, EncabezadoTitulo
    Estructura.clear()
    EncabezadoTitulo.clear()



























