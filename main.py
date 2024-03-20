import tkinter as tk
from tkinter import filedialog
from interfaz import InterfazHTML
import tkinter.messagebox as messagebox
from document_handler import abrir_documento
from analizador_lexico import leer_archivo, generar_html_tablas, generar_html
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
    boton_traduccion = interfaz.boton("Traducir archivo", lambda ventana=ventana_principal, caja_texto=caja_texto2: boton_Traduccion(ventana, caja_texto), fila=1, columna=2)
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
                    # Llamar a la función para procesar el documento después de cargarlo en la caja de texto

                    # Llamar a leer_archivo con la ruta del documento
                    palabras = leer_archivo(ruta_documento)
                    if palabras:
                        for palabra, tipo, linea, columna in palabras:
                            print(f'Palabra: {palabra}, Tipo: {tipo}, Línea: {linea}, Columna: {columna}')
                else:
                    messagebox.showerror("Error", "El archivo está vacío.")
        except Exception as e:
            print("Error al leer el archivo:", e)
    else:
        print("No se seleccionó ningún documento.")

def boton_Traduccion(ventana, caja_texto):
    global ruta_documento_global
    print("Botón Traducción presionado")
    if ruta_documento_global:
        print("Ruta del documento:", ruta_documento_global)
        # Obtener las palabras procesadas y las palabras clasificadas como errores
        palabras_procesadas, errores = leer_archivo(ruta_documento_global)
        if palabras_procesadas:
            # Limpiar la caja de texto
            caja_texto.delete(1.0, tk.END)
            # Insertar las palabras procesadas en la caja de texto
            for palabra, tipo, linea, columna in palabras_procesadas:
                caja_texto.insert(tk.END, f'TOKEN: {palabra}, TIPO: {tipo}, LÍNEA: {linea}, COLUMNA: {columna}\n')
            # Insertar las palabras clasificadas como errores en la caja de texto al final
            if errores:
                caja_texto.insert(tk.END, "\nPalabras clasificadas como errores:\n")
                for palabra, tipo, linea, columna in errores:
                    caja_texto.insert(tk.END, f'TOKEN: {palabra}, TIPO: {tipo}, LÍNEA: {linea}, COLUMNA: {columna}\n')
                # Mostrar ventana para generar HTML con tablas de errores
                mostrar_ventana_errores(palabras_procesadas, errores)
            else:
                # Mostrar ventana para generar HTML sin tablas de errores
                mostrar_ventana_sin_errores(palabras_procesadas)
        else:
            print("No se ha cargado ningún documento.")


def mostrar_ventana_sin_errores(palabras_procesadas):
    ventana_sin_errores = tk.Toplevel()
    ventana_sin_errores.title("Generar HTML sin errores")
    ventana_sin_errores.geometry("350x150")

    etiqueta_titulo = tk.Label(ventana_sin_errores, text="¡HTML generado sin errores!", font=("Arial", 14, "bold"), pady=10)
    etiqueta_titulo.pack()

    etiqueta_explicacion = tk.Label(ventana_sin_errores, text="Puedes generar tu archivo HTML sin problemas.", font=("Arial", 12))
    etiqueta_explicacion.pack()

    boton_generar_html = tk.Button(ventana_sin_errores, text="Generar HTML", command=lambda: generar_html_cerrar_ventana(palabras_procesadas, "archivo.html", ventana_sin_errores), font=("Arial", 12), padx=20, pady=10)
    boton_generar_html.pack(pady=10)

def mostrar_ventana_errores(palabras_procesadas, errores):
    ventana_con_errores = tk.Toplevel()
    ventana_con_errores.title("Generar HTML con errores")
    ventana_con_errores.geometry("350x200")

    etiqueta_titulo = tk.Label(ventana_con_errores, text="¡Se encontraron errores!", font=("Arial", 14, "bold"), pady=10)
    etiqueta_titulo.pack()

    etiqueta_explicacion = tk.Label(ventana_con_errores, text="Revisa los errores encontrados y genera tu archivo HTML.", font=("Arial", 12))
    etiqueta_explicacion.pack()

    boton_generar_html = tk.Button(ventana_con_errores, text="Generar HTML", command=lambda: generar_html_tablas_cerrar_ventana(palabras_procesadas, errores, "archivo.html", ventana_con_errores), font=("Arial", 12), padx=20, pady=10)
    boton_generar_html.pack(pady=10)

def generar_html_cerrar_ventana(palabras_procesadas, nombre_archivo, ventana):
    generar_html(palabras_procesadas, nombre_archivo)
    webbrowser.open_new_tab(nombre_archivo)
    ventana.destroy()

def generar_html_tablas_cerrar_ventana(palabras_procesadas, errores, nombre_archivo, ventana):
    generar_html_tablas(palabras_procesadas, errores, nombre_archivo)
    webbrowser.open_new_tab(nombre_archivo)
    ventana.destroy()



if __name__ == "__main__":
    main()
