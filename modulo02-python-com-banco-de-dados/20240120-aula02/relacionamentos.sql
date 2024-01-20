/*
Níveis de relacionamento entre tabelas

Podemos entender como cardinalidade o nível de relacionamento entre as tabelas em um
banco de dados, ou seja, como se dão as relações entre os registros das tabelas.

Temos 3 tipos de relacionamento possíveis entre 2 tabelas, que são os seguintes:
	1:1			=> Relacionamento Um para Um
	1:N			=> Relacionamento Um para Muitos
	N:N			=> Relacionamento Muitos para Muitos
	
Para ilustrar esses tipos de relacionamentos, vamos montar uma estrutura de tabelas que
irá simular um sistema de mensagens e posts (estilo twitter). Teremos as seguintes entidades:
	- Pessoa que pode fazer uma postagem
		- A pessoa terá dados de acesso e dados pessoais
	- A Postagem feita por uma Pessoa
	- As Categorias (hashtags) a que uma Postagem pertence
*/

# Vamos separar os dados de usuário em 2 tabelas: tb_usuarios e tb_perfis

CREATE TABLE IF NOT EXISTS tb_usuarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(200) NOT NULL,
	senha VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_perfis(
	id INT PRIMARY KEY,
	nome VARCHAR(200) NOT NULL,
	data_nascimento DATE NULL,
	FOREIGN KEY(id) REFERENCES tb_usuarios(id)
);

# Inserir alguns usuários
INSERT INTO tb_usuarios(email, senha) VALUES
	("maria@email.com", "maria123"),
	("joao@email.com", "joao123"),
	("jose@email.com", "jose123");
SELECT * FROM tb_usuarios tu ;

INSERT INTO tb_perfis (id, nome, data_nascimento) VALUES
	(1, "Maria Antonieta das Dores", "1965-01-13"),
	(2, "João Silva", "1968-04-12"),
	(3, "José Anchieta", "1958-12-05");
SELECT * FROM tb_perfis tp ;

INSERT INTO tb_perfis (id, nome, data_nascimento) VALUES (1, "Teste", "1900-01-01");