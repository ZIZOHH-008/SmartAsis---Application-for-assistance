CREATE DATABASE base_datos;  -- Base de datos para productos
USE base_datos;

CREATE TABLE productos (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	codigo CHAR(10) NOT NULL DEFAULT '0',
	nombre VARCHAR(20) NOT NULL DEFAULT '0',
	modelo VARCHAR(20) NOT NULL DEFAULT '0',
	precio DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
	cantidad INT NOT NULL DEFAULT 0
) ENGINE=InnoDB;

-- Inserción de datos en la tabla productos
INSERT INTO productos (codigo, nombre, modelo, precio, cantidad) VALUES
	('5505', 'Julian', 'Castillo', 9.0, 16),
	('5506', 'Isabella', 'Salazar', 11.5, 14),
	('5507', 'Sebastian', 'Pérez', 10.2, 10),
	('5508', 'Camila', 'Morales', 15.8, 30),
	('5509', 'Mateo', 'Vargas', 12.3, 22),
	('5510', 'Gabriel', 'Suarez', 7.5, 18),
	('5511', 'Victoria', 'Gonzalez', 13.0, 25),
	('5512', 'Nicolas', 'Cano', 14.5, 19),
	('5513', 'Daniela', 'Martinez', 16.0, 20),
	('5514', 'Andres', 'Moreno', 8.0, 12),
	('5515', 'Lorenzo', 'Cordero', 9.9, 15),
	('5516', 'Sara', 'Alvarez', 10.7, 17),
	('5517', 'Diego', 'Rios', 12.0, 21),
	('5518', 'Lucia', 'Pinto', 14.2, 26),
	('5519', 'Rafael', 'Salas', 11.0, 23),
	('5495', 'Juan', 'Parra', 11.3, 14),
	('5496', 'Maria', 'Lopez', 12.5, 20),
	('5497', 'Carlos', 'Gomez', 10.0, 15),
	('5498', 'Ana', 'Martinez', 9.5, 25),
	('5499', 'Pedro', 'Diaz', 14.0, 18),
	('5500', 'Luisa', 'Fernandez', 13.5, 30),
	('5501', 'Sofia', 'Castro', 15.0, 22),
	('5502', 'Diego', 'Ramirez', 16.2, 19),
	('5503', 'Valentina', 'Torres', 17.5, 23),
	('5504', 'Mateo', 'Hernandez', 8.0, 12);
    
SELECT * FROM productos;

