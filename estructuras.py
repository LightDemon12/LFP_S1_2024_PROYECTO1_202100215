class BloqueInicio:
    def __init__(self, encabezado, cuerpo, linea, columna):
        self.encabezado = encabezado
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna

class BloqueEncabezado:
    def __init__(self, titulo_pagina, linea, columna):
        self.titulo_pagina = titulo_pagina
        self.linea = linea
        self.columna = columna

class BloqueCuerpo:
    def __init__(self, elementos, linea, columna):
        self.elementos = elementos
        self.linea = linea
        self.columna = columna

# Clases para los elementos del cuerpo

class Titulo:
    def __init__(self, texto, posicion, tamaño, color, linea, columna):
        self.texto = texto
        self.posicion = posicion
        self.tamaño = tamaño
        self.color = color
        self.linea = linea
        self.columna = columna

class Fondo:
    def __init__(self, color, linea, columna):
        self.color = color
        self.linea = linea
        self.columna = columna

class Parrafo:
    def __init__(self, texto, posicion, linea, columna):
        self.texto = texto
        self.posicion = posicion
        self.linea = linea
        self.columna = columna

class Texto:
    def __init__(self, fuente, color, tamaño, linea, columna):
        self.fuente = fuente
        self.color = color
        self.tamaño = tamaño
        self.linea = linea
        self.columna = columna

class Codigo:
    def __init__(self, texto, posicion, linea, columna):
        self.texto = texto
        self.posicion = posicion
        self.linea = linea
        self.columna = columna

class Negrita:
    def __init__(self, texto, linea, columna):
        self.texto = texto
        self.linea = linea
        self.columna = columna

class Subrayado:
    def __init__(self, texto, linea, columna):
        self.texto = texto
        self.linea = linea
        self.columna = columna

class Tachado:
    def __init__(self, texto, linea, columna):
        self.texto = texto
        self.linea = linea
        self.columna = columna

class Cursiva:
    def __init__(self, texto, linea, columna):
        self.texto = texto
        self.linea = linea
        self.columna = columna

class Salto:
    def __init__(self, cantidad, linea, columna):
        self.cantidad = cantidad
        self.linea = linea
        self.columna = columna

class Tabla:
    def __init__(self, filas, columnas, elementos, linea, columna):
        self.filas = filas
        self.columnas = columnas
        self.elementos = elementos
        self.linea = linea
        self.columna = columna

class ElementoTabla:
    def __init__(self, fila, columnaE, texto, linea, columna):
        self.fila = fila
        self.columna = columnaE
        self.texto = texto
        self.linea = linea
        self.columna = columna
