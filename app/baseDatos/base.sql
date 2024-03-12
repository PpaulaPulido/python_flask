CREATE DATABASE agenda;
use agenda;
CREATE TABLE personas(
  id_persona int auto_increment primary key,
  nombre_persona varchar(60),
  apellido_persona varchar(60),
  email varchar(60),
  direccion varchar(60),
  telefono int,
  user_persona varchar(60),
  contrasena varchar(255)
);

describe personas;
select * from personas;