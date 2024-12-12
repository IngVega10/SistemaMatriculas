import pyodbc

class Conexion:
    def __init__(self):
        # Configuración de la conexión a la base de datos
        self.server = 'DESKTOP-TH07C3D\SQLVEGA'  # Cambia a la IP de tu servidor
        self.database = 'BD_SistemasMatriculas'  # Nombre de la base de datos
        self.username = 'sa'  # Usuario de SQL Server
        self.password = '123'  # Contraseña de SQL Server
        self.connection = None

    def conectar(self):
        try:
            # Cadena de conexión
            self.connection = pyodbc.connect(
                f'DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
            )
            print("Conexión exitosa a la base de datos")
            return self.connection
        except pyodbc.Error as e:
            print("Error al conectar a la base de datos:", e)
            return None

    def cerrar_conexion(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada con éxito")
