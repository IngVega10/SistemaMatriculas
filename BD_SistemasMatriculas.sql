-- Crear la base de datos
CREATE DATABASE BD_SistemasMatriculas;
GO

-- Usar la base de datos recién creada
USE BD_SistemasMatriculas;
GO

CREATE TABLE Roles (
    Id_Roles INT PRIMARY KEY IDENTITY(1,1), -- Genera valores automáticos empezando en 1
    Tipo_Roles NVARCHAR(100) NOT NULL      -- NVARCHAR es adecuado para texto
);

CREATE TABLE Usuario (
    Id_Usuario INT PRIMARY KEY IDENTITY(1,1), -- Genera valores automáticos empezando en 1
    Id_Roles INT NOT NULL,                   -- Llave foránea que referencia Roles
    Nombre_Usuario NVARCHAR(100) NOT NULL,   -- NVARCHAR para almacenar nombres
    Contraseña NVARCHAR(255) NOT NULL,       -- NVARCHAR para almacenar contraseñas (idealmente encriptadas)
    FOREIGN KEY (Id_Roles) REFERENCES Roles(Id_Roles) -- Llave foránea definida correctamente
);


