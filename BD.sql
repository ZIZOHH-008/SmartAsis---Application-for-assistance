-- foreign key () References ()
-- FOREIGN KEY (profesor_id) REFERENCES Profesores(profesor_id)

CREATE DATABASE SmartAsisBD;
USE SmartAsisBD;

CREATE TABLE acudiente(
    ced_acu INT PRIMARY KEY NOT NULL,
    nom_acu VARCHAR(20) NOT NULL,
    apelli_acu VARCHAR(20) NOT NULL,
    relacion_acu VARCHAR(15) NOT NULL,
    fechaNaci_acu DATE NOT NULL,
    edad_acu INT NOT NULL,
    tel_acu INT(15) NOT NULL,
    direc_acu VARCHAR(20)
) ENGINE=InnoDB;

CREATE TABLE grado(
    num_grad INT PRIMARY KEY NOT NULL,
    nom_gra VARCHAR(20),
    niv_gra VARCHAR(20)
) ENGINE=InnoDB;


CREATE TABLE estudiante(
    id_est INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    apelli_est VARCHAR(20) NOT NULL,
    nom_est VARCHAR(20) NOT NULL,
    grad_est INT NOT NULL,
    edad_est VARCHAR(20) NOT NULL,
    sexo_est VARCHAR(20) NOT NULL,
    direc_est INT NOT NULL,
    tel_est VARCHAR(20) NOT NULL,
    email_est INT NOT NULL
) ENGINE=InnoDB;

CREATE TABLE profesor(
    ced_prof INT PRIMARY KEY NOT NULL,
    nom_prof VARCHAR(20) NOT NULL,
    apelli_prof VARCHAR(20) NOT NULL,
    fechaNaci_prof DATE NOT NULL,
    edad_prof INT NOT NULL,
    tel_prof INT NOT NULL,
    direc_prof VARCHAR(20) NOT NULL,
    especialidad_prof VARCHAR(20)
) ENGINE=InnoDB;

CREATE TABLE asignatura(
    id_asig INT PRIMARY KEY NOT NULL,
    dias_asig INT NOT NULL,
    id_prof2 INT
) ENGINE=InnoDB;


CREATE TABLE jornada(
    id_jor INT PRIMARY KEY NOT NULL,
    nom_jor VARCHAR(20) NOT NULL,
    ini_jor INT(20) NOT NULL,
    fin_jor INT(20) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE sede(
    id_sed INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nom_sed VARCHAR(20) NOT NULL,
    direc_sed VARCHAR(20) NOT NULL,
    tel_sed INT
) ENGINE=InnoDB;

CREATE TABLE asistencia(
    id_asis INT PRIMARY KEY NOT NULL,
    fir_asis DATE NOT NULL,
    fecha_asis DATE NOT NULL,
    hor_asis INT(15),
    nom_asis VARCHAR(20),
    moti_asis VARCHAR(20),
    id_sa1 INT(20),
    id_prof1 INT(20),
    id_grado1 INT (20),
    id_sed1 INT(20)
) ENGINE=InnoDB;
