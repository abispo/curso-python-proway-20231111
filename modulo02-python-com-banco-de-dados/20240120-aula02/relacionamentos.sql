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

# A linha abaixo dará erro, pois já existe um registro com a chave primária igual a 1
INSERT INTO tb_perfis (id, nome, data_nascimento) VALUES (1, "Teste", "1900-01-01");

/*
No caso acima, criamos uma relação de Um para Um (1:1) entre a tabela tb_usuarios e a tabela
tb_perfis, pois a coluna chave primária da tabela tb_perfis, também é chave estrangeira
que aponta para a tabela tb_usuarios. Dessa maneira, nenhum usuário terá mais de 1 perfil
na tabela de perfis.

*/

# Exemplo: Mostrar email, nome e data de nascimento do usuário
SELECT tu.email, tp.nome, tp.data_nascimento FROM tb_usuarios tu 
INNER JOIN tb_perfis tp 
ON tu.id = tp.id;

-- ///// --

# Criar a tabela de postagens
CREATE TABLE IF NOT EXISTS tb_postagens(
	id INT PRIMARY KEY AUTO_INCREMENT,
	usuario_id INT NOT NULL,
	titulo VARCHAR(200) NOT NULL,
	corpo TEXT NOT NULL,
	FOREIGN KEY (usuario_id) REFERENCES tb_usuarios(id)
);

# Inserir registros
INSERT INTO tb_postagens (usuario_id, titulo, corpo) VALUES
	(1, "Python é legal", "Python é uma linguagem bem legal."),
	(1, "Java é poderoso", "Java tem muitos recursos."),
	(2, "Linux é maneiro", "Estou aprendendo Linux para ser devops.");
SELECT * FROM tb_postagens tp ;

# No caso acima, a regra de negócio é a seguinte: Um usuário pode fazer diversas postagens,
# porém uma postagem é feita apenas por 1 usuário. Nesse cenário temos uma relação de
# Um para Muitos (1:N) entre as tabelas tb_usuarios e tb_postagens. Nas relações 1:N, a
# chave estrangeira ficará sempre na tabela dependente (a tabela que fica do lado N da relação).

# Exemplo: Mostrando os posts feitos por um usuário

SELECT tp.nome, tu.email, tpo.titulo FROM tb_perfis tp 
INNER JOIN tb_usuarios tu 
ON tp.id = tu.id
INNER JOIN tb_postagens tpo
ON tu.id = tpo.usuario_id 
WHERE tpo.usuario_id = 1;

-- ///// --
