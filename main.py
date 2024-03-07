import tkinter as tk
from interfaz import InterfazHTML

def main():
    ventana_principal = tk.Tk() # Crear ventana principal

    interfaz = InterfazHTML(ventana_principal, "900x450", "Interfaz HTML", "black") # Crear objeto de la clase InterfazHTML
    
    interfaz.etiqueta("TRADUCTOR DE HTML") # Crear etiqueta
    interfaz.boton("Cargar archivo", boton_Carga ) # Crear botón
    interfaz.boton("Traducir", boton_Traducción) # Crear botón
    caja_texto = interfaz.caja_texto() # Crear caja de texto
    ventana_principal.mainloop() # Mostrar ventana


    caja_texto.insert(tk.END, "Texto de prueba") # Insertar texto en la caja de texto
# Funciones para los botones
def boton_Carga(): 
    print("Botón carga presionado")

def boton_Traducción():
    print("Boton Traducción presionado")


if __name__ == "__main__":
    main()