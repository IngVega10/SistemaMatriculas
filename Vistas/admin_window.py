import tkinter as tk
from tkinter import messagebox

class SuperUserView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("Plataforma de Superusuario")
        self.geometry("800x600")
        
        # Crear un panel lateral
        self.sidebar = tk.Frame(self, bg="lightgray", width=200, height=600, relief="sunken")
        self.sidebar.pack(side="left", fill="y")
        
        # Botones en el panel lateral
        self.btn_config = tk.Button(self.sidebar, text="Configuración Inicial", width=20, command=self.open_config)
        self.btn_config.pack(pady=10)
        
        self.btn_users = tk.Button(self.sidebar, text="Usuarios", width=20, command=self.open_users)
        self.btn_users.pack(pady=10)
        
        self.btn_reports = tk.Button(self.sidebar, text="Reportes", width=20, command=self.open_reports)
        self.btn_reports.pack(pady=10)

        # Crear un área de trabajo principal
        self.main_area = tk.Frame(self, bg="white", width=600, height=600)
        self.main_area.pack(side="right", fill="both", expand=True)
        
        # Inicializamos la vista principal vacía
        self.label = tk.Label(self.main_area, text="Seleccione una opción del menú", font=("Arial", 16))
        self.label.pack(pady=20)

    def open_config(self):
        """ Muestra la configuración inicial en el área principal """
        self.clear_main_area()
        config_label = tk.Label(self.main_area, text="Configuración Inicial", font=("Arial", 18))
        config_label.pack(pady=20)
        # Aquí agregarías las opciones o controles específicos para la configuración del Excel

    def open_users(self):
        """ Muestra la gestión de usuarios en el área principal """
        self.clear_main_area()
        users_label = tk.Label(self.main_area, text="Gestión de Usuarios", font=("Arial", 18))
        users_label.pack(pady=20)
        # Aquí agregarías las opciones para la gestión de usuarios

    def open_reports(self):
        """ Muestra la opción de reportes en el área principal """
        self.clear_main_area()
        reports_label = tk.Label(self.main_area, text="Generación de Reportes", font=("Arial", 18))
        reports_label.pack(pady=20)
        # Aquí agregarías las opciones para generar reportes

    def clear_main_area(self):
        """ Limpia el área principal antes de cargar una nueva vista """
        for widget in self.main_area.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = SuperUserView()
    app.mainloop()
