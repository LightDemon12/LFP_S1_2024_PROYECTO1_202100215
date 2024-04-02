import tkinter as tk
from tkinter import filedialog
from Interfaz.interfaz import InterfazHTML
import tkinter.messagebox as messagebox
from Logica.document_handler import abrir_documento
from Logica.analizador_lexico import  generar_html_tablas,  generar_html_tablas_sin_errores, limpiar_listas_secundarias,buscar_palabras_clave,leer_archivo
from Logica.lector import leer_documento, crear_html, limpiar_listas
import webbrowser

# Variable global para almacenar la ruta del documento
ruta_documento_global = ""

def main():
    ventana_principal = tk.Tk() # Crear ventana principal
    ventana_principal.geometry("1200x720")  # Ajustar el tamaño de la ventana
    interfaz = InterfazHTML(ventana_principal, "1200x720", "Interfaz HTML", "#579BF4") # Crear objeto de la clase InterfazHTML
    etiqueta = interfaz.etiqueta("TRADUCTOR DE HTML", fila=0, columna=0, columnspan=4) # Crear etiqueta
    caja_texto1 = interfaz.caja_texto(fila=2, columna=0, columnspan=2, height=35, width=70) # Crear caja de texto y ajustar tamaño
    boton_carga = interfaz.boton("Cargar archivo", lambda ventana=ventana_principal, caja_texto=caja_texto1: boton_Carga(ventana, caja_texto), fila=1, columna=1)
    caja_texto2 = interfaz.caja_texto(fila=2, columna=2, columnspan=2, height=35, width=70) # Crear caja de texto y ajustar tamaño
    boton_traduccion = interfaz.boton("Traducir archivo", lambda ventana=ventana_principal, caja_texto=caja_texto2: boton_Traduccion(ventana, caja_texto, caja_texto2), fila=1, columna=3)
    boton_actualizar = interfaz.boton("Actualizar Contenido", lambda ventana=ventana_principal, caja_texto2=caja_texto2, caja_texto1=caja_texto1: actualizar_contenido(caja_texto1, ventana,caja_texto2), fila=1, columna=2)
    ventana_principal.mainloop() # Mostrar ventana
# Cambia la definición de la función boton_Carga para aceptar dos argumentos
def boton_Carga(ventana_principal, caja_texto1): 
    print("Botón carga presionado")
    global ruta_documento_global
    ruta_documento = abrir_documento()
    if ruta_documento:
        print("Ruta del documento cargado:", ruta_documento)
        ruta_documento_global = ruta_documento  # Actualizar la variable global con la ruta del documento
        try:
            with open(ruta_documento, 'r', encoding='utf-8') as archivo:
                contenido = archivo.readlines()  # Leer el contenido del archivo por líneas
                if contenido:  # Verificar si el contenido no está vacío
                    caja_texto1.delete(1.0, tk.END)  # Limpiar la caja de texto
                    caja_texto1.insert(tk.END, ''.join(contenido))  # Insertar el contenido en la caja de texto
                    leer_documento(ruta_documento)  # Llamar a la función leer_documento
                else:
                    messagebox.showerror("Error", "El archivo está vacío.")
        except Exception as e:
            print("Error al leer el archivo:", e)
    else:
        print("No se seleccionó ningún documento.")

def copiar_contenido_a_archivo(archivo, contenido):
    try:
        with open(archivo, "w", encoding="utf-8") as archivo_destino:
            archivo_destino.write(contenido)
        print("Contenido de la caja de texto copiado y sobrescrito en el archivo seleccionado.")
    except Exception as e:
        print(f"Error al copiar y sobrescribir el contenido en el archivo: {e}")

def actualizar_contenido(caja_texto1, ventana_principal, caja_texto2):
    global ruta_documento_global
    if ruta_documento_global:
        caja_texto2.delete(1.0, tk.END)
        contenido_texto = caja_texto1.get(1.0, tk.END)  # Obtener el contenido de la caja de texto
        if contenido_texto.strip():  # Verificar si hay contenido en la caja de texto
            copiar_contenido_a_archivo(ruta_documento_global, contenido_texto)
        else:
            print("La caja de texto está vacía. No se copia nada en el archivo.")
        leer_documento(ruta_documento_global)  # Llamar a la función leer_documento con la ruta del archivo
        reiniciar_programa()  # Reiniciar el programa
    else:
        print("No se ha cargado ningún documento.")

def reiniciar_programa():
    global ruta_documento_global  # Agregar esta línea para reiniciar la variable global
    limpiar_listas()
    limpiar_listas_secundarias()

def boton_Traduccion(ventana, caja_texto, caja_texto2):
    global ruta_documento_global
    print("Botón Traducción presionado")
    leer_documento(ruta_documento_global)
    if ruta_documento_global:
        print("Ruta del documento:", ruta_documento_global)
        # Obtener las palabras procesadas y las palabras clasificadas como errores
        palabras_procesadas, errores = leer_archivo(ruta_documento_global)
        # Llamar a la función para buscar palabras clave
        errores_palabras_clave = buscar_palabras_clave(palabras_procesadas, errores)
        if palabras_procesadas:
            # Limpiar la caja de texto
            caja_texto.delete(1.0, tk.END)
            # Insertar las palabras procesadas en la caja de texto
            for token in palabras_procesadas:
                caja_texto.insert(tk.END, f'TOKEN: {token.valor}, TIPO: {token.tipo}, LÍNEA: {token.linea}, COLUMNA: {token.columna}\n')
            # Insertar los errores de palabras clave en la caja de texto
            if errores_palabras_clave:
                caja_texto.insert(tk.END, "\nErrores de palabras clave:\n")
                for error in errores_palabras_clave:
                    caja_texto.insert(tk.END, f'PALABRA: {error.valor}\n')
            # Insertar las palabras clasificadas como errores en la caja de texto al final
            if errores:
                caja_texto.insert(tk.END, "\nPalabras clasificadas como errores:\n")
                for error in errores:
                    caja_texto.insert(tk.END, f'TOKEN: {error.valor}, TIPO: {error.tipo}, LÍNEA: {error.linea}, COLUMNA: {error.columna}\n')
                # Mostrar ventana para generar HTML con tablas de errores
                mostrar_ventana_errores(palabras_procesadas, errores)
            else:
                # Mostrar ventana para generar HTML sin tablas de errores
                mostrar_ventana_sin_errores(palabras_procesadas, errores, caja_texto2)
        else:
            print("No se ha cargado ningún documento.")

def mostrar_ventana_sin_errores(palabras_procesadas, errores, caja_texto2):
    ventana_sin_errores = tk.Toplevel()
    ventana_sin_errores.title("Generar HTML sin errores")
    ventana_sin_errores.geometry("500x300")
    etiqueta_titulo = tk.Label(ventana_sin_errores, text="¡HTML generado sin errores!", font=("Arial", 14, "bold"), pady=10)
    etiqueta_titulo.pack()
    etiqueta_explicacion = tk.Label(ventana_sin_errores, text="Ingresa los nombres del archivo HTML y de la tabla de reporte:", font=("Arial", 12))
    etiqueta_explicacion.pack()
    # Campo de entrada para el nombre del archivo HTML
    etiqueta_html = tk.Label(ventana_sin_errores, text="Nombre del archivo HTML:", font=("Arial", 12))
    etiqueta_html.pack()
    entrada_html = tk.Entry(ventana_sin_errores, font=("Arial", 12))
    entrada_html.pack()
    # Campo de entrada para el nombre del archivo de la tabla de reporte
    etiqueta_tabla = tk.Label(ventana_sin_errores, text="Nombre del archivo de la tabla:", font=("Arial", 12))
    etiqueta_tabla.pack()
    entrada_tabla = tk.Entry(ventana_sin_errores, font=("Arial", 12))
    entrada_tabla.pack()
    def generar_html():
        nombre_html = entrada_html.get().strip()
        nombre_tabla = entrada_tabla.get().strip()
        if nombre_html and nombre_tabla:  # Verificar si ambos campos están completos
            generar_html_y_cerrar_ventana(ventana_sin_errores, nombre_html + ".html", palabras_procesadas, errores, nombre_tabla + ".html", caja_texto2)

        else:
            messagebox.showerror("Error", "Por favor, completa ambos campos.")
    # Botón para generar HTML y cerrar ventana
    boton_generar_html = tk.Button(ventana_sin_errores, text="Generar HTML", command=generar_html, font=("Arial", 12), padx=20, pady=10)
    boton_generar_html.pack(pady=10)


def mostrar_ventana_errores(palabras_procesadas, errores):
    ventana_con_errores = tk.Toplevel()
    ventana_con_errores.title("Generar HTML con errores")
    ventana_con_errores.geometry("500x300")
    etiqueta_titulo = tk.Label(ventana_con_errores, text="¡Se encontraron errores!", font=("Arial", 14, "bold"), pady=10)
    etiqueta_titulo.pack()
    etiqueta_explicacion = tk.Label(ventana_con_errores, text="Revisa los errores encontrados y genera tu archivo HTML.", font=("Arial", 12))
    etiqueta_explicacion.pack()
    # Campo de entrada para el nombre del archivo
    etiqueta_nombre_archivo = tk.Label(ventana_con_errores, text="Nombre del archivo:")
    etiqueta_nombre_archivo.pack()
    entrada_nombre_archivo = tk.Entry(ventana_con_errores)
    entrada_nombre_archivo.pack()
    

    # Función para generar el HTML con tablas de errores y cerrar la ventana
    def generar_html_tablas_cerrar_ventana():
        nombre_archivo = entrada_nombre_archivo.get() + ".html"
        generar_html_tablas(palabras_procesadas, errores, nombre_archivo)
        webbrowser.open_new_tab(nombre_archivo)
        ventana_con_errores.destroy()
    boton_generar_html = tk.Button(ventana_con_errores, text="Generar HTML", command=generar_html_tablas_cerrar_ventana, font=("Arial", 12), padx=20, pady=10)
    boton_generar_html.pack(pady=10)


def generar_html_y_cerrar_ventana(ventana, nombre_archivo, palabras_procesadas, errores, nombre_archivo2, caja_texto2):
    try:
        # Llamar a la función crear_html con el nombre de archivo nombre_archivo2
        crear_html(nombre_archivo2)
        # Capturar el contenido generado por crear_html
        with open(nombre_archivo2, "r", encoding="utf-8") as archivo_html:
            contenido_html = archivo_html.read()
        # Insertar el contenido en la caja de texto 2
        caja_texto2.delete("1.0", tk.END)  # Limpiar la caja de texto 2
        caja_texto2.insert(tk.END, contenido_html)
        # Generar HTML con tablas sin errores
        generar_html_tablas_sin_errores(palabras_procesadas, errores, nombre_archivo)
        # Abrir archivos en el navegador
        webbrowser.open_new_tab(nombre_archivo)
        webbrowser.open_new_tab(nombre_archivo2)
        # Cerrar la ventana
        ventana.destroy()
        print(f"Se ha generado el archivo HTML '{nombre_archivo}' correctamente.")
    except Exception as e:
        print(f"No se pudo generar el archivo HTML: {e}")

def generar_html_tablas_cerrar_ventana(palabras_procesadas, errores, nombre_archivo, ventana):
    generar_html_tablas(palabras_procesadas, errores, nombre_archivo)
    webbrowser.open_new_tab(nombre_archivo)
    ventana.destroy()

if __name__ == "__main__":
    main()


