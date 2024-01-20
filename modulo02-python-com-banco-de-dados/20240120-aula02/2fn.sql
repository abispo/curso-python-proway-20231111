/*
Segunda Forma Normal (2FN)

A Segunda Forma Normal (2FN), exige que:
	* A tabela esteja na 1FN
 	* Todas as colunas não chave da tabela dependem de todas as partes da chave primária.
 	* Chamamos isso de Dependência Funcional Total
*/

USE 20231111_python_com_banco_de_dados_fns;

# Criar a tabela de controle de serviços
CREATE TABLE IF NOT EXISTS tb_controle(
	id INT AUTO_INCREMENT,
	servico_id INT NOT NULL,
	servico VARCHAR(200) NOT NULL,
	valor_hora FLOAT NOT NULL,
	total_horas INT NOT NULL,
	PRIMARY KEY (id, servico_id)
);

# Inserir dados na tabela tb_controle
INSERT INTO tb_controle (servico_id, servico, valor_hora, total_horas) VALUES
	(1, "Manutenção de PC", 80, 6),
	(1, "Manutenção de PC", 80, 10),
	(2, "Desenvolvimento de Sites", 150, 10),
	(3, "Configuração de Servidor", 100, 3),
	(4, "Aulas de Programação", 50, 12);
	
SELECT * FROM tb_controle tc ;

/*
Nesse caso, a tabela tb_controle está na 1FN, pois possui pelo menos 1 chave primária, não
possui atributos multivalorados e não possui campos compostos.
Porém, ela não está na Segunda Forma Normal (2FN) pois as colunas servico e valor_hora
existem em função apenas da coluna servico_id. Ou seja, essas colunas dependem apenas de
parte da chave primária, e não dela inteiroa. A coluna total_horas depende da informação
de controle e de qual serviço foi realizado, ou seja, ela depende de todas as partes
da chave primária.
*/

# Renomear a tabela fora da 1FN
RENAME TABLE tb_controle TO tb_controle_pre_2fn;

# Criar a tabela de serviços
CREATE TABLE IF NOT EXISTS tb_servicos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL,
	valor_hora FLOAT NOT NULL
);

# Inserir valores na tabela
INSERT INTO tb_servicos (nome, valor_hora) VALUES
	("Manutenção de PC", 80),
	("Desenvolvimento de Sites", 150),
	("Configuração de Servidor", 100),
	("Aulas de Programação", 50);
	
SELECT * FROM tb_servicos;

# Criar a tabela de controle de serviços seguindo a 2FN
CREATE TABLE IF NOT EXISTS tb_controle(
	id INT AUTO_INCREMENT,
	servico_id INT NOT NULL,
	total_horas INT NOT NULL,
	PRIMARY KEY(id, servico_id),
	FOREIGN KEY(servico_id) REFERENCES tb_servicos(id)
);

# Inserir os dados
INSERT INTO tb_controle (servico_id, total_horas) VALUES
	(1, 6),
	(1, 10),
	(2, 10),
	(3, 3),
	(4, 12);
	
SELECT * FROM tb_controle tc ;

# Verificar o total por serviço realizado
SELECT ts.nome, ts.valor_hora, tc.total_horas, ts.valor_hora * tc.total_horas AS "Total"
FROM tb_servicos ts 
INNER JOIN tb_controle tc 
ON tc.servico_id = ts.id ;
