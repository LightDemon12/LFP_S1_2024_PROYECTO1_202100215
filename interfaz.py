import tkinter as tk

class InterfazHTML: 
    def __init__(self, ventana, tamaño="900x450", titulo="titulo predefinido", color="#C5CAF5"):
        # Inicialización de la ventana principal
        self.ventana = ventana 
        self.ventana.geometry(tamaño) 
        self.ventana.configure(background=color) 
        self.ventana.title(titulo) 

    def etiqueta(self, texto, fila, columna, columnspan=1, color_fondo="white", justificacion=tk.CENTER):
        # Método para crear etiquetas
        etiqueta = tk.Label(   
            self.ventana, 
            text=texto, 
            font=("cascadia", 12), 
            bg=color_fondo, 
            justify=justificacion
        )
        # Posicionamiento de la etiqueta en la ventana
        etiqueta.grid(row=fila, column=columna, columnspan=columnspan, padx=10, pady=10)

    def boton(self, texto, comando, fila, columna, columnspan=1):
        # Método para crear botones
        boton = tk.Button(
            self.ventana, 
            text=texto,
            font=("Cascadia  Code", 12), 
            bg="#7382F5", 
            fg="black", 
            command=comando, 
            relief="flat",  
        )
        # Posicionamiento del botón en la ventana
        boton.grid(row=fila, column=columna, columnspan=columnspan, padx=10, pady=10)

    def caja_texto(self, fila, columna, rowspan=1, columnspan=1):
        # Método para crear cajas de texto
        caja = tk.Text(  
            master=self.ventana,
            wrap="word", 
            height=10,
            width=40,
            fg="red", 
            bg="white", 
        )
        # Posicionamiento de la caja de texto en la ventana
        caja.grid(row=fila, column=columna, rowspan=rowspan, columnspan=columnspan, padx=10, pady=10)
        return caja 
