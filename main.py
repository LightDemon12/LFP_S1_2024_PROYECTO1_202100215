import tkinter as tk
from interfaz import InterfazHTML
from document_handler import abrir_documento
import tkinter.messagebox as messagebox

# Variable global para almacenar la ruta del documento
ruta_documento_global = ""

def main():
    ventana_principal = tk.Tk() # Crear ventana principal
    ventana_principal.geometry("1200x720")  # Ajustar el tamaño de la ventana

    interfaz = InterfazHTML(ventana_principal, "1200x720", "Interfaz HTML", "#579BF4") # Crear objeto de la clase InterfazHTML

    etiqueta = interfaz.etiqueta("TRADUCTOR DE HTML", fila=0, columna=0, columnspan=4) # Crear etiqueta
    boton_carga = interfaz.boton("Cargar archivo", lambda: boton_Carga(caja_texto1), fila=1, columna=1) # Crear botón
    boton_traduccion = interfaz.boton("Traducir", boton_Traduccion, fila=1, columna=2) # Crear botón
    caja_texto1 = interfaz.caja_texto(fila=2, columna=0, columnspan=2, height=35, width=70) # Crear caja de texto y ajustar tamaño
    caja_texto2 = interfaz.caja_texto(fila=2, columna=2, columnspan=2, height=35, width=70) # Crear caja de texto y ajustar tamaño
    ventana_principal.mainloop() # Mostrar ventana

# Función para cargar el documento
def boton_Carga(caja_texto1): 
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
                else:
                    messagebox.showerror("Error", "El archivo está vacío.")
        except Exception as e:
            print("Error al leer el archivo:", e)
    else:
        print("No se seleccionó ningún documento.")

def boton_Traduccion():
    global ruta_documento_global
    print("Boton Traducción presionado")
    if ruta_documento_global:
        print("Ruta del documento:", ruta_documento_global)
    else:
        print("No se ha cargado ningún documento.")

if __name__ == "__main__":
    main()
