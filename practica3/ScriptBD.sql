create table libro(
	ISBN varchar(45) not null primary key,
	nombre varchar(45) not null,
	autor varchar(45) not null,
	editorial varchar(45) not null,
	precio float not null,
	portada varchar(45) not null
	--En la portada se guarda la ruta del archivo, la imagen esta guardada en el servidor 	
)


create table pedido(
	id int unsigned auto_increment primary key,
	fecha date not null,
	hora_inicio varchar(15) not null,
	hora_fin varchar(15) not null
)

create table sesion(
	id int unsigned auto_increment primary key,
	id_pedido int unsigned not null,
	id_libro varchar(45) not null,
	foreign key (id_pedido) references pedido(id),
	foreign key (id_libro) references libro(ISBN)
)

create table usuario(
	id int unsigned auto_increment primary key,
	ip varchar(15) not null,
	nombre varchar(45) not null
)

create table usuarioSesion(
	id int unsigned auto_increment primary key,
	id_usuario int unsigned not null,
	id_pedido int unsigned not null,
	
)