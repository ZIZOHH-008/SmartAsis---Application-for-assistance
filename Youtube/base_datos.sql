CREATE DATABASE base_datos;  -- Base de datos para productos
USE base_datos;

-- Tabla estudiante
CREATE TABLE estudiante (
    id_est INT PRIMARY KEY NOT NULL AUTO_INCREMENT, -- Clave primaria
    codigoEst CHAR(10) NOT NULL DEFAULT 'N/A',  -- Código del estudiante
    nombreEst VARCHAR(20) NOT NULL DEFAULT 'N/A', -- Nombre del estudiante
    apellidoEst VARCHAR(20) NOT NULL DEFAULT 'N/A', -- Apellido del estudiante
    gradoEst VARCHAR(20) NOT NULL DEFAULT 'N/A',  -- Grado del estudiante
    edadEst VARCHAR(20) NOT NULL DEFAULT 'N/A',  -- Edad del estudiante
    telEst VARCHAR(20) NOT NULL DEFAULT 'N/A'  -- Teléfono del estudiante
) ENGINE=InnoDB;

-- Tabla asistencia
CREATE TABLE asistencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    fecha DATE,
    presente BOOLEAN,
    FOREIGN KEY (estudiante_id) REFERENCES estudiante(id_est)  
);

-- Tabla profesor
CREATE TABLE profesor (
    codigo_prof CHAR(10) PRIMARY KEY NOT NULL,
    usuario_prof VARCHAR(20) NOT NULL
) ENGINE=InnoDB;


INSERT INTO profesor (codigo_prof, usuario_prof) VALUES 
('SmartAsis', '2024'),
('Fredy Cajamarca', '1122'),
('Robinson Montenegro', '1234'),
('Laura', '4321'),
('Martha Pemberthy', '4433');


-- Inserción de datos en la tabla productos
INSERT INTO estudiante (codigoEst, nombreEst, apellidoEst, gradoEst, edadEst, telEst) VALUES
	('5505', 'Juan Manuel', 'Parra', '11-3', '16', '3193548479'),
    ('5506', 'Juan Pablo', 'Bejarano', '11-3', '16', '3187043824'),
	('5507', 'Donoban', 'Granobles', '11-3', '17', '3187154054'),
    ('5508', 'Oscar Felipe', 'Bravo', '11-3', '17', '3004252646'),
	('5509', 'Camila', 'Ramírez', '11-3', '16', '3001234567'),
    ('5510', 'Daniela', 'Santos', '11-3', '17', '3123456789'),
    ('5511', 'Andrés', 'Pérez', '11-3', '16', '3134567890'),
    ('5512', 'Sofía', 'Gómez', '11-3', '16', '3145678901'),
    ('5513', 'Mateo', 'Martínez', '11-3', '17', '3156789012'),
    ('5514', 'Valentina', 'López', '11-3', '16', '3167890123'),
    ('5515', 'Santiago', 'Díaz', '11-3', '17', '3178901234'),
    ('5516', 'Isabella', 'Rodríguez', '11-3', '16', '3189012345'),
    ('5517', 'Tomás', 'Castro', '11-3', '17', '3190123456'),
    ('5518', 'Martina', 'Moreno', '11-3', '16', '3201234567'),
	('5519', 'Emilio', 'Hernández', '11-3', '17', '3002345678'),
    ('5520', 'Paula', 'Jiménez', '11-3', '16', '3013456789'),
    ('5521', 'Samuel', 'Torres', '11-3', '17', '3024567890'),
    ('5522', 'Luciana', 'Suárez', '11-3', '16', '3035678901'),
    ('5523', 'Felipe', 'Medina', '11-3', '17', '3046789012'),
    ('5524', 'Alejandra', 'Navarro', '11-3', '16', '3057890123'),
    ('5525', 'Julián', 'Guerrero', '11-3', '17', '3068901234'),
    ('5526', 'Adriana', 'Castaño', '11-3', '16', '3079012345'),
    ('5527', 'Carlos', 'Ortiz', '11-3', '17', '3080123456'),
    ('5528', 'Laura', 'Mendoza', '11-3', '16', '3091234567');
    
    
    









