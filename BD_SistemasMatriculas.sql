-- Crear la base de datos
CREATE DATABASE BD_SistemasMatriculas;
GO

-- Usar la base de datos reci�n creada
USE BD_SistemasMatriculas;
GO

CREATE TABLE Roles (
    Id_Roles INT PRIMARY KEY IDENTITY(1,1), -- Genera valores autom�ticos empezando en 1
    Tipo_Roles NVARCHAR(100) NOT NULL      -- NVARCHAR es adecuado para texto
);

CREATE TABLE Usuario (
    Id_Usuario INT PRIMARY KEY IDENTITY(1,1), -- Genera valores autom�ticos empezando en 1
    Id_Roles INT NOT NULL,                   -- Llave for�nea que referencia Roles
    Nombre_Usuario NVARCHAR(100) NOT NULL,   -- NVARCHAR para almacenar nombres
    Contrase�a NVARCHAR(255) NOT NULL,       -- NVARCHAR para almacenar contrase�as (idealmente encriptadas)
    FOREIGN KEY (Id_Roles) REFERENCES Roles(Id_Roles) -- Llave for�nea definida correctamente
);


