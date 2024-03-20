from estructuras import BloqueInicio, BloqueEncabezado, BloqueCuerpo, Titulo, Fondo, Parrafo, Texto, Codigo, Negrita, Subrayado, Tachado, Cursiva, Salto, Tabla, ElementoTabla


def leer_documento(ruta_archivo):
    if not ruta_archivo:
        print("No se proporcionó ninguna ruta de archivo.")
        return None

    estructura = []  # Lista para almacenar la estructura del documento
    bloque_encabezado_actual = None
    bloque_cuerpo_actual = None

    try:
        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.readlines()

            for linea_numero, linea in enumerate(contenido, start=1):
                # Eliminar espacios en blanco al principio y al final de la línea
                linea = linea.strip()
                # Verificar si la línea está vacía
                if not linea:
                    continue
                # Verificar el tipo de línea y crear instancias de las clases correspondientes
                if linea.startswith("Inicio:"):
                    bloque_cuerpo_actual = None  # Reiniciar el bloque de cuerpo actual al inicio del documento
                    bloque_inicio = BloqueInicio(bloque_encabezado_actual, None, linea_numero, 1, 2)
                    estructura.append(bloque_inicio)
                # Resto de la lógica para clasificar las líneas
                elif linea.startswith("Encabezado:"):
                    titulo_pagina = linea.split(":")[1].strip()
                    bloque_encabezado_actual = BloqueEncabezado(titulo_pagina, linea_numero)
                    if bloque_cuerpo_actual:
                        bloque_cuerpo_actual.encabezado = bloque_encabezado_actual
                elif linea.startswith("Cuerpo:"):
                    bloque_cuerpo_actual = BloqueCuerpo([], linea_numero)
                    if bloque_inicio:
                        bloque_inicio.cuerpo = bloque_cuerpo_actual
                elif linea.startswith("Titulo:"):
                    elementos = linea.split(":")[1].split(";")
                    texto = elementos[0].split('"')[1]
                    posicion = elementos[1].split('"')[1]
                    tamaño = elementos[2].split('"')[1]
                    color = elementos[3].split('"')[1]
                    titulo = Titulo(texto, posicion, tamaño, color, linea_numero)
                    bloque_cuerpo_actual.elementos.append(titulo)
                elif linea.startswith("Fondo:"):
                    color = linea.split(":")[1].strip().split('"')[1]
                    fondo = Fondo(color, linea_numero)
                    bloque_cuerpo_actual.elementos.append(fondo)
                elif linea.startswith("Parrafo:"):
                    elementos = linea.split(":")[1].split(";")
                    texto = elementos[0].split('"')[1]
                    posicion = elementos[1].split('"')[1]
                    parrafo = Parrafo(texto, posicion, linea_numero)
                    bloque_cuerpo_actual.elementos.append(parrafo)
                elif linea.startswith("Texto:"):
                    elementos = linea.split(":")[1].split(";")
                    fuente = elementos[0].split('"')[1]
                    color = elementos[1].split('"')[1]
                    tamaño = elementos[2].split('"')[1]
                    texto = Texto(fuente, color, tamaño, linea_numero)
                    bloque_cuerpo_actual.elementos.append(texto)
                elif linea.startswith("Codigo:"):
                    texto = linea.split(":")[1].strip().split('"')[1]
                    posicion = linea.split(":")[2].strip().split('"')[1]
                    codigo = Codigo(texto, posicion, linea_numero)
                    bloque_cuerpo_actual.elementos.append(codigo)
                elif linea.startswith("Negrita:"):
                    texto = linea.split(":")[1].strip().split('"')[1]
                    negrita = Negrita(texto, linea_numero)
                    bloque_cuerpo_actual.elementos.append(negrita)
                elif linea.startswith("Subrayado:"):
                    texto = linea.split(":")[1].strip().split('"')[1]
                    subrayado = Subrayado(texto, linea_numero)
                    bloque_cuerpo_actual.elementos.append(subrayado)
                elif linea.startswith("Tachado:"):
                    texto = linea.split(":")[1].strip().split('"')[1]
                    tachado = Tachado(texto, linea_numero)
                    bloque_cuerpo_actual.elementos.append(tachado)
                elif linea.startswith("Cursiva:"):
                    texto = linea.split(":")[1].strip().split('"')[1]
                    cursiva = Cursiva(texto, linea_numero)
                    bloque_cuerpo_actual.elementos.append(cursiva)
                elif linea.startswith("Salto:"):
                    cantidad = linea.split(":")[1].strip()
                    salto = Salto(cantidad, linea_numero)
                    bloque_cuerpo_actual.elementos.append(salto)


    except FileNotFoundError:
        print("El archivo no pudo ser encontrado.")
        return None

    return estructura