import tkinter as tk
from tkinter import messagebox

# Funciones para cada opción
def matriculas():
    messagebox.showinfo("Matrículas", "Funcionalidad de Matrículas aún no implementada.")

def pagos():
    messagebox.showinfo("Pagos", "Funcionalidad de Pagos aún no implementada.")

def reporte_matriculas():
    messagebox.showinfo("Reporte de Matrículas", "Funcionalidad de Reporte de Matrículas aún no implementada.")

# Clase para la Ventana Principal
class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Plataforma de Usuario")
        self.geometry("800x600")
        
        # Panel lateral
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=200, height=600)
        self.sidebar.pack(side="left", fill="y")
        
        # Botón de Matriculas
        self.btn_matriculas = tk.Button(self.sidebar, text="Matrículas", width=20, height=2, command=matriculas, bg="#34495e", fg="white", font=("Arial", 12))
        self.btn_matriculas.pack(pady=10)

        # Botón de Pagos
        self.btn_pagos = tk.Button(self.sidebar, text="Pagos", width=20, height=2, command=pagos, bg="#34495e", fg="white", font=("Arial", 12))
        self.btn_pagos.pack(pady=10)

        # Botón de Reporte de Matrículas
        self.btn_reporte_matriculas = tk.Button(self.sidebar, text="Reporte de Matrículas", width=20, height=2, command=reporte_matriculas, bg="#34495e", fg="white", font=("Arial", 12))
        self.btn_reporte_matriculas.pack(pady=10)
        
        # Área principal (donde se mostrará el contenido de cada sección)
        self.main_area = tk.Frame(self, bg="#ecf0f1", width=600, height=600)
        self.main_area.pack(side="right", fill="both", expand=True)
        
        # Mensaje de bienvenida o instrucciones en el área principal
        self.label_main = tk.Label(self.main_area, text="Bienvenido al sistema de matrículas", font=("Arial", 20), bg="#ecf0f1")
        self.label_main.pack(pady=50)

# Crear la ventana de usuario
if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
