import tkinter as tk

# Clase para crear una interfaz gráfica
class InterfazHTML: 
    def __init__(self, ventana, tamaño="900x450", titulo="titulo predefinido", color="white"): # Constructor
        self.ventana = ventana # Crear ventana
        self.ventana.geometry(tamaño) # Tamaño de la ventana
        self.ventana.configure(background=color) # Color de fondo
        self.ventana.title(titulo) # Título de la ventana

    def etiqueta(self,texto): # Método para crear etiquetas
        tk.Label(   
            self.ventana, # Ventana
            text=texto, # Texto de la etiqueta
            font=("cascadia", 12), # Fuente
            bg="white", # Color de fondo
            justify=tk.CENTER, # Justificación
        ).pack(
            fill=tk.BOTH, # Rellenar
        )

    def boton(self, texto, comando):
        tk.Button(
            self.ventana, 
            text=texto,
            font=("Cascadia  Code", 12), 
            bg="#A9F5F2", 
            fg="black", # Color de letra
            command=comando,  # Comando del botón
            relief="flat",  # Relieve 
        ).pack(
            fill=tk.BOTH,
        )

    def caja_texto(self):    # Método para crear caja de texto
        caja = tk.Text(  
            master=self.ventana,
            wrap="word", # Ajuste de texto
            height=10,
            width=40,
            state="disabled", # Estado de la caja
            fg="red", 
            bg="white", 
            
        )
        caja.pack(
            fill=tk.BOTH,
        )
        return caja # Retornar caja de texto para su uso posterior
        