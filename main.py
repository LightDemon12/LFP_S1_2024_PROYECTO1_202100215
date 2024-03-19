import tkinter as tk
from interfaz import InterfazHTML

def main():
    ventana_principal = tk.Tk() # Crear ventana principal

    interfaz = InterfazHTML(ventana_principal, "690x320", "Interfaz HTML", "#579BF4") # Crear objeto de la clase InterfazHTML
    
    interfaz.etiqueta("TRADUCTOR DE HTML", fila=0, columna=0, columnspan=4) # Crear etiqueta
    interfaz.boton("Cargar archivo", boton_Carga, fila=1, columna=1) # Crear botón
    interfaz.boton("Traducir", boton_Traducción, fila=1, columna=2) # Crear botón
    caja_texto = interfaz.caja_texto(fila=2, columna=0, columnspan=2) # Crear caja de texto
    caja_texto = interfaz.caja_texto(fila=2, columna=2, columnspan=2) # Crear caja de texto
    ventana_principal.mainloop() # Mostrar ventana

# Funciones para los botones
def boton_Carga(): 
    print("Botón carga presionado")

def boton_Traducción():
    print("Boton Traducción presionado")

if __name__ == "__main__":
    main()
