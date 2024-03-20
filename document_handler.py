import tkinter as tk
from tkinter import filedialog
from estructuras import BloqueInicio, BloqueEncabezado, BloqueCuerpo, Titulo, Fondo, Parrafo, Texto, Codigo, Negrita, Subrayado, Tachado, Cursiva, Salto, Tabla


def abrir_documento():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    # Abrir un cuadro de diálogo para seleccionar un archivo
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

    if ruta_archivo:
        print("Documento abierto:", ruta_archivo)
        return ruta_archivo
    else:
        print("No se seleccionó ningún documento.")
        return None
    
    
  