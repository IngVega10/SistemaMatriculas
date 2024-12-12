import tkinter as tk
from tkinter import messagebox
from Controlador.validate_login import validate_login

# Ventana de usuario
def open_user_window():
    user_window = tk.Toplevel()
    user_window.title("Plataforma de Usuario")
    user_window.geometry("400x300")

    tk.Label(user_window, text="Bienvenido, Usuario", font=("Arial", 16)).pack(pady=20)
    tk.Button(user_window, text="Salir", command=user_window.destroy).pack(pady=10)

# Ventana Admin
def open_admin_window():
    admin_window = tk.Toplevel()
    admin_window.title("Plataforma de Administrador")
    admin_window.geometry("400x300")

    tk.Label(admin_window, text="Bienvenido, Administrador", font=("Arial", 16)).pack(pady=20)
    tk.Button(admin_window, text="Salir", command=admin_window.destroy).pack(pady=10)

def main():
    root = tk.Tk()
    root.title("Sistema de Matrículas")
    root.geometry("400x300")

    tk.Label(root, text="Inicio de Sesión", font=("Arial", 18)).pack(pady=20)

    tk.Label(root, text="Usuario:").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Contraseña:").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    tk.Button(
        root,
        text="Ingresar",
        command=lambda: validate_login(username_entry.get(), password_entry.get()),
    ).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
