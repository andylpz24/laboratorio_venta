create database laboratorio_ventas;
use laboratorio_ventas;

create table venta(
fecha datetime not null,
cliente varchar(50) not null,
productos_vendidos varchar(50) not null,
codigo_venta int primary key,
total_recaudado decimal(10,2) not null,
costo decimal(10,2) not null
);

create table venta_online(
codigo int primary key,
pagina varchar(50),
foreign key (codigo) references venta(codigo_venta) 
);

create table venta_local(
codigo int primary key,
local_ varchar(50),
foreign key (codigo) references venta(codigo_venta)
);

alter table venta_online
modify column pagina varchar(50) not null;

alter table venta_local
modify column local_ varchar(50) not null;

ALTER TABLE venta_local RENAME COLUMN codigo TO codigo_venta;