from tkinter import messagebox
from Modelos.mUsuario import Usuario
from Vistas.login import open_admin_window, open_user_window

# Mueve la importación dentro de la función
def validate_login(username, password):
    from Vistas.login import open_admin_window, open_user_window  # Importación diferida
    resultado = Usuario.autenticar(username, password)

    if "error" in resultado:
        messagebox.showerror("Error", resultado["error"])
    else:
        rol = resultado["rol"]
        if rol == "Admin":
            open_admin_window()
        elif rol == "Usuario":
            open_user_window()
        else:
            messagebox.showwarning("Advertencia", "Rol desconocido")

