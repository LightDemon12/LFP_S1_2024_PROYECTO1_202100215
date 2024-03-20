class BloqueInicio:
    def __init__(self, encabezado, cuerpo, linea, numero, otro_parametro):
        self.encabezado = encabezado
        self.cuerpo = cuerpo
        self.linea = linea
        self.numero = numero
        self.otro_parametro = otro_parametro


class BloqueEncabezado:
    def __init__(self, titulo_pagina, linea):
        self.titulo_pagina = titulo_pagina
        self.linea = linea


class BloqueCuerpo:
    def __init__(self, elementos, linea):
        self.elementos = elementos
        self.linea = linea


# Clases para los elementos del cuerpo

class Titulo:
    def __init__(self, texto, posicion, tamaño, color, linea):
        self.texto = texto
        self.posicion = posicion
        self.tamaño = tamaño
        self.color = color
        self.linea = linea


class Fondo:
    def __init__(self, color, linea):
        self.color = color
        self.linea = linea


class Parrafo:
    def __init__(self, texto, posicion, linea):
        self.texto = texto
        self.posicion = posicion
        self.linea = linea


class Texto:
    def __init__(self, fuente, color, tamaño, linea):
        self.fuente = fuente
        self.color = color
        self.tamaño = tamaño
        self.linea = linea


class Codigo:
    def __init__(self, texto, posicion, linea):
        self.texto = texto
        self.posicion = posicion
        self.linea = linea


class Negrita:
    def __init__(self, texto, linea):
        self.texto = texto
        self.linea = linea


class Subrayado:
    def __init__(self, texto, linea):
        self.texto = texto
        self.linea = linea


class Tachado:
    def __init__(self, texto, linea):
        self.texto = texto
        self.linea = linea


class Cursiva:
    def __init__(self, texto, linea):
        self.texto = texto
        self.linea = linea


class Salto:
    def __init__(self, cantidad, linea):
        self.cantidad = cantidad
        self.linea = linea


class Tabla:
    def __init__(self, filas, columnas, elementos, linea):
        self.filas = filas
        self.columnas = columnas
        self.elementos = elementos
        self.linea = linea


