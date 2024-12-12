from Controlador.conexion import Conexion  # Importamos Conexion

class Usuario:
    def __init__(self, id_usuario=None, nombre_usuario=None, contraseña=None, rol=None):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.rol = rol

    @staticmethod
    def autenticar(nombre_usuario, contraseña):
        """
        Autentica a un usuario en la base de datos.
        Retorna un diccionario con los datos del usuario si la autenticación es exitosa.
        """
        conexion = Conexion()  # Creación de objeto de conexión
        conn = conexion.conectar()  # Conectamos a la base de datos
        if not conn:
            return {"error": "No se pudo conectar con la base de datos"}

        try:
            cursor = conn.cursor()
            query = """
            SELECT IdUsuario, Nombre_Usuario, Rol
            FROM Usuario
            WHERE Nombre_Usuario = ? AND Contraseña = ?
            """
            cursor.execute(query, (nombre_usuario, contraseña))
            result = cursor.fetchone()

            if result:
                return {
                    "id_usuario": result[0],
                    "nombre_usuario": result[1],
                    "rol": result[2]
                }
            else:
                return {"error": "Usuario o contraseña incorrectos"}

        except Exception as e:
            return {"error": f"Ocurrió un error al autenticar: {e}"}
        finally:
            conexion.cerrar_conexion()  # Cerramos la conexión

    @staticmethod
    def obtener_usuarios():
        """
        Retorna una lista de todos los usuarios registrados en la base de datos.
        """
        conexion = Conexion()
        conn = conexion.conectar()
        if not conn:
            return {"error": "No se pudo conectar con la base de datos"}

        try:
            cursor = conn.cursor()
            query = "SELECT IdUsuario, Nombre_Usuario, Rol FROM Usuario"
            cursor.execute(query)
            resultados = cursor.fetchall()

            usuarios = [
                {"id_usuario": row[0], "nombre_usuario": row[1], "rol": row[2]}
                for row in resultados
            ]
            return usuarios

        except Exception as e:
            return {"error": f"Ocurrió un error al obtener los usuarios: {e}"}
        finally:
            conexion.cerrar_conexion()
