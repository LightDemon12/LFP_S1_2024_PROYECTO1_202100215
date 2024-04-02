
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
    def __init__(self, fuente, color, tamaño, texto):
        self.fuente = fuente
        self.color = color
        self.tamaño = tamaño
        self.texto = texto
        self.instruccion = "texto"

    def __str__(self):
        return f'<span style="font-family: {self.fuente}; color: {self.color}; font-size: {self.tamaño}px;">{self.texto}</span>'

class Codigo:
    def __init__(self, texto, posicion):
        self.texto = texto
        self.posicion = posicion
        self.instruccion = "codigo"
    def __str__(self):
        return f'<pre style="text-align: {self.posicion}; font-family: monospace;">{self.texto}</pre>'

class Negrita:
    def __init__(self, texto):
        self.texto = texto
        self.instruccion = "negrita"
    def __str__(self):
        return f'<strong>{self.texto}</strong><br>'

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
        return f'<del>{self.texto}</del><br>'

class Cursiva:
    def __init__(self, texto):
        self.texto = texto
        self.instruccion = "cursiva"
    def __str__(self):
        return f'<em>{self.texto}</em><br>'

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
        self.html = self.generar_tabla_html_string()

class Tabla:
    def __init__(self, filas, columnas, elementos):
        self.filas = filas
        self.columnas = columnas
        self.elementos = elementos
        self.instruccion = "tabla"
        self.html = self.generar_tabla_html_string()

    def generar_tabla_html_string(self):
        html = "<table>\n"
        for i in range(self.filas):
            html += "  <tr>\n"
            for j in range(self.columnas):
                index = i * self.columnas + j
                if index < len(self.elementos):
                    html += f"    <td>{self.elementos[index]}</td>\n"
            html += "  </tr>\n"
        html += "</table>"
        return html

    def __str__(self):
        return self.html



class Token:
    def __init__(self, valor, tipo, linea, columna):
        self.valor = valor
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

class Reservada(Token):
    def __init__(self, valor, linea, columna):
        super().__init__(valor, 'RESERVADA', linea, columna)

class Instruccion(Token):
    def __init__(self, valor, linea, columna):
        super().__init__(valor, 'INSTRUCCION', linea, columna)

class Numero(Token):
    def __init__(self, valor, linea, columna):
        super().__init__(valor, 'NUMERO', linea, columna)

class Palabra(Token):
    def __init__(self, valor, linea, columna):
        super().__init__(valor, 'PALABRA', linea, columna)

class CaracterEspecial(Token):
    def __init__(self, valor, linea, columna):
        super().__init__(valor, 'CARACTER_ESPECIAL', linea, columna)

class Error:
    def __init__(self, valor, tipo, linea, columna):
        self.valor = valor
        self.tipo = tipo
        self.linea = linea
        self.columna = columna