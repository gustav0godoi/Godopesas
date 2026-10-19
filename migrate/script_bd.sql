CREATE DATABASE IF NOT EXISTS  godopesas;

USE godopesas;


CREATE TABLE IF NOT EXISTS  tb_usuarios (
 login VARCHAR(50) NOT NULL PRIMARY KEY,
 senha VARCHAR(200) NOT NULL
);


CREATE TABLE IF NOT EXISTS tb_categorias (
 id_categoria INT NOT NULL PRIMARY KEY auto_increment,
 nome VARCHAR(30) NOT NULL,
 login VARCHAR(50) NOT NULL,

 FOREIGN KEY (login) REFERENCES tb_usuarios (login)
);


CREATE TABLE IF NOT EXISTS tb_despesas (
 id_despesas INT NOT NULL PRIMARY KEY auto_increment,
 dt_cadastro DATE NOT NULL,
 valor DECIMAL(10,2) NOT NULL,
 descricao VARCHAR(200),
 login VARCHAR(50) NOT NULL,
 id_categoria INT ,

 FOREIGN KEY (login) REFERENCES tb_usuarios (login),
 FOREIGN KEY (id_categoria) REFERENCES tb_categorias (id_categoria)
);
