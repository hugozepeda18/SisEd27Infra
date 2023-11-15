USE 'escuela';

DROP TABLE IF EXISTS asistencia_diaria;
DROP TABLE IF EXISTS reporte_administrativo;
DROP TABLE IF EXISTS curso;
DROP TABLE IF EXISTS alumno;
DROP TABLE IF EXISTS grupo;

CREATE TABLE alumno
(
 matricula        BIGINT NOT NULL PRIMARY KEY,
 nombre           VARCHAR(200) NOT NULL,
 apellido_paterno VARCHAR(100) NOT NULL,
 apellido_materno VARCHAR(100) NULL,
 curp             VARCHAR(50) NOT NULL,
 grado            INT NULL,
 grupo            VARCHAR(10) NOT NULL,
 sexo             VARCHAR(10) NOT NULL,
 edad             INT NOT NULL,
 turno            VARCHAR(10) NOT NULL,
 correo           VARCHAR(200) NULL,
 incidencias      INT DEFAULT  0,
 incidencias_graves INT DEFAULT  0,
 incidencias_muy_graves INT DEFAULT  0
);

CREATE TABLE personal
(
	id  INT NOT NULL AUTO_INCREMENT,
    nombre_completo VARCHAR(250) NOT NULL,
    funsion VARCHAR(250) NOT NULL,
    turno VARCHAR(10) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE incidencias
(
	id  INT NOT NULL AUTO_INCREMENT,
    alumno_id BIGINT NOT NULL,
    fecha DATE NOT NULL,
    descripcion VARCHAR(500) NOT NULL,
    accion VARCHAR(500) NULL,
    aspecto VARCHAR(500) NULL,
    personal_id INT NOT NULL,
    tipo INT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_alumno FOREIGN KEY (alumno_id) REFERENCES alumno(matricula),
    CONSTRAINT fk_personal FOREIGN KEY (personal_id) REFERENCES personal(id)
);

CREATE TABLE user
(
	id  INT NOT NULL AUTO_INCREMENT,
    personal_id INT NOT NULL,
    email VARCHAR(250) NOT NULL,
    password VARCHAR(250) NOT NULL,
    role VARCHAR(50) NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_personal_user FOREIGN KEY (personal_id) REFERENCES personal(id)
);

CREATE TABLE asistencia
(
    id INT NOT NULL AUTO_INCREMENT,
    alumno_id BIGINT NOT NULL,
    fecha DATE NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_alumno_asistencia FOREIGN KEY (alumno_id) REFERENCES alumno(matricula)
);