import tkinter as tk
from tkinter import filedialog



def abrir_documento():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    # Abrir un cuadro de diálogo para seleccionar un archivo
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

    if ruta_archivo:
        print("Documento abierto:", ruta_archivo)
        return ruta_archivo  # Devolver la ruta del archivo seleccionado
    else:
        print("No se seleccionó ningún documento.")
        return None






