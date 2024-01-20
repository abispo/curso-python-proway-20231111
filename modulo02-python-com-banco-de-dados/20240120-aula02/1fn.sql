/*
Primeira Forma Normal (1FN)

A Primeira Forma Normal define que cada coluna da tabela deve conter apenas valores atômicos
ou indivisíveis, ou seja, valores únicos e não compostos. Exige também que exista pelo menos
uma coluna que seja chave primária na tabela. Além disso, não podemos ter colunas
multivaloradas.
*/

# Criar o banco de dados
CREATE DATABASE IF NOT EXISTS 20231111_python_com_banco_de_dados_fns;

# Definir o banco de dados padrão
USE 20231111_python_com_banco_de_dados_fns;

# Criar a tabela tb_clientes
CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL,
	endereco VARCHAR(200) NOT NULL,
	telefone VARCHAR (50) NOT NULL
);

# Inserir dados na tabela tb_clientes
INSERT INTO tb_clientes (nome, endereco, telefone) VALUES
	("João da Silva", "Rua XV de Novembro, 1000, Centro, Blumenau, SC", "4798327810"),
	("Neide Carvalho", "Praça da Liberdade, 12, Liberdate, São Paulo, SP", "1187433291,11984348695"),
	("Maria Souza", "Rua dos Bandeirantes, 240, Centro, Pomerode, SC", "47901112371");
	
# Consultar os dados da tabela tb_clientes
SELECT * FROM tb_clientes tc ;

/*
A tabela tb_clientes não está na Primeira Forma Normal, pois:
 * A coluna 'endereco' não é indivisível (pode ser quebrada em outras colunas)
 * A coluna 'telefone' possui alguns registros multivalorados

Vamos fazer com que a tabela de clientes siga as regras da 1FN.
*/

# Vamos primeiro renomear a tabela atual
RENAME TABLE tb_clientes TO tb_clientes_pre_1fn;

# Criar a tabela de clientes com a estrutura correta
CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL,
	tipo_logradouro VARCHAR(50) NOT NULL,
	logradouro VARCHAR(200) NOT NULL,
	numero VARCHAR(10) NOT NULL,
	bairro VARCHAR(100) NOT NULL,
	cidade VARCHAR(100) NOT NULL,
	estado CHAR(2) NOT NULL
);

/*
("João da Silva", "Rua XV de Novembro, 1000, Centro, Blumenau, SC", "4798327810"),
("Neide Carvalho", "Praça da Liberdade, 12, Liberdade, São Paulo, SP", "1187433291,11984348695"),
("Maria Souza", "Rua dos Bandeirantes, 240, Centro, Pomerode, SC", "47901112371");
*/

INSERT INTO tb_clientes (nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado) VALUES
	("João da Silva", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC"),
	("Neide Carvalho", "Praça", "da Liberdade", "12", "Liberdade", "São Paulo", "SP"),
	("Maria Souza", "Rua", "dos Bandeirantes", "240", "Centro", "Pomerode", "SC");
	
# Segundo passo: Criar a tabela de telefones dos clientes
CREATE TABLE IF NOT EXISTS tb_telefones(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cliente_id INT NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	FOREIGN KEY(cliente_id) REFERENCES tb_clientes(id)
);

# Inserir os telefones
INSERT INTO tb_telefones (cliente_id, telefone) VALUES
	(1, "4798327810"),
	(2, "1187433291"),
	(2, "11984348695"),
	(3, "47901112371");
	
SELECT * FROM tb_telefones tt ;

# Selecionado os telefones dos clientes
SELECT tc.nome, tt.telefone FROM tb_clientes tc 
INNER JOIN tb_telefones tt 
ON tc.id = tt.cliente_id ;

/*
Agora sim temos a tabela tb_clientes respeitando todas as regras para ser considerada uma
tabela que está na Primeira Forma Normal. Dessa maneira eliminamos os campos multivalorados
 e também as colunas com valores compostos. Isso implica em uma facilidade na hora de
 fazer as consultas e também em um aumento de performance.
*/
