/*
Terceira Forma Normal (3FN)

Uma tabela está na Terceira Forma Normal (3FN) Se:
 * Ela está na Segunda Forma Normal;
 * Todos os campos não chave da tabela dependem exclusivamente da chave primária

*/

USE 20231111_python_com_banco_de_dados_fns;

CREATE TABLE IF NOT EXISTS tb_pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	data_pedido DATETIME NOT NULL,
	descricao VARCHAR(300) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_itens(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL,
	valor_unitario FLOAT NOT NULL
);

INSERT INTO tb_pedidos (data_pedido, descricao) VALUES
	("2023-12-01 13:45:11", "Pedido pra mamãe"),
	("2023-12-02 21:34:51", "Dia dos namorados");

INSERT INTO tb_itens (nome, valor_unitario) VALUES
	("Caneta Esferográfica", 9.90),
	("Mochila do Naruto", 89.90),
	("Guarda-Chuva", 34.90),
	("Mouse Gamer", 83.90),
	("Popit", 121.90);

SELECT * FROM tb_pedidos tp ;
SELECT * FROM tb_itens ti ;

# Tabela que relaciona pedidos e itens
CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	pedido_id INT NOT NULL,
	item_id INT NOT NULL,
	quantidade INT NOT NULL,
	subtotal FLOAT NOT NULL,
	PRIMARY KEY(pedido_id, item_id),
	FOREIGN KEY(pedido_id) REFERENCES tb_pedidos(id),
	FOREIGN KEY(item_id) REFERENCES tb_itens(id)
);

# Inserir registros na tb_pedidos_itens
INSERT INTO tb_pedidos_itens (pedido_id, item_id, quantidade, subtotal) VALUES
	(1, 1, 3, 29.7),
	(1, 2, 1, 89.9),
	(1, 3, 1, 34.90),
	(2, 3, 1, 34.90),
	(2, 4, 1, 83.90);
	
SELECT * FROM tb_pedidos_itens tpi ;

/*
A tabela tb_pedidos_itens, não está na 3FN, pois a coluna 'subtotal' depende de colunas
que não são chave primária (coluna quantidade e coluna valor_unitario). Nesse caso, devemos
excluir essa coluna para a tabela estar de acordo com as regras da 3FN.
*/

# Apagando a coluna subtotal
ALTER TABLE tb_pedidos_itens DROP COLUMN subtotal;

SELECT * FROM tb_pedidos_itens tpi ;

# Não temos mais a informação de subtotal disponível diretamente. Porém, podemos calcular
# esse dado na hora da consulta. Podemos utilizar uma view para salvar essa consulta
CREATE VIEW vw_total_pedidos AS
SELECT
	tp.id,
	tp.data_pedido,
	tp.descricao,
	ti.nome,
	ti.valor_unitario,
	tpi.quantidade,
	FORMAT(ti.valor_unitario * tpi.quantidade, 2) AS "Subtotal"
FROM tb_pedidos tp 
INNER JOIN tb_pedidos_itens tpi 
ON tp.id = tpi.pedido_id
INNER JOIN tb_itens ti 
ON tpi.item_id = ti.id;

SELECT * FROM vw_total_pedidos ;