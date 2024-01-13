"""
Python com Banco de Dados

Podemos acessar bancos de dados utilizando a linguagem Python simplesmente através de uma biblioteca, que podemos chamar de conector.

Por padrão, o Python já vem com uma biblioteca para conectar com bancos de dados do tipo SQLite
"""

# Importamos a biblioteca para trabalharmos com bancos de dados SQLite
import sqlite3

"""
Para nos conectarmos em qualquer banco de dados, geralmente seguimos essa ordem:
    1. Definimos a connection string do banco
    2. Criamos uma conexão com o banco a partir dessa connection string
    3. Criamos um cursor a partir da conexão, onde poderemos executar os códigos
    4. Recebemos os resultados
"""

# Criando a connection string
connection_string = "db.sqlite3"

# Criando a conexão com o banco de dados
conexao = sqlite3.connect(connection_string)

# Criando o cursor a partir da conexão
cursor = conexao.cursor()

if __name__ == "__main__":

    # "Resetando" o banco de dados
    comando = "DROP TABLE IF EXISTS tb_estados"
    cursor.execute(comando)
    
    comando = """

    CREATE TABLE IF NOT EXISTS tb_estados(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        uf TEXT NOT NULL
    );
    """

    # Executando o comando definido acima
    cursor.execute(comando)

    # Inserindo dados na tabela
    lista_estados = [
        {"nome": "Acre", "sigla": "AC"},
        {"nome": "Alagoas", "sigla": "AL"},
        {"nome": "Amapá", "sigla": "AP"},
        {"nome": "Amazonas", "sigla": "AM"},
        {"nome": "Bahia", "sigla": "BA"},
        {"nome": "Ceará", "sigla": "CE"},
        {"nome": "Distrito Federal", "sigla": "DF"},
        {"nome": "Espírito Santo", "sigla": "ES"},
        {"nome": "Goiás", "sigla": "GO"},
        {"nome": "Maranhão", "sigla": "MA"},
        {"nome": "Mato Grosso", "sigla": "MT"},
        {"nome": "Mato Grosso do Sul", "sigla": "MS"},
        {"nome": "Minas Gerais", "sigla": "MG"},
        {"nome": "Pará", "sigla": "PA"},
        {"nome": "Paraíba", "sigla": "PB"},
        {"nome": "Paraná", "sigla": "PR"},
        {"nome": "Pernambuco", "sigla": "PE"},
        {"nome": "Piauí", "sigla": "PI"},
        {"nome": "Rio de Janeiro", "sigla": "RJ"},
        {"nome": "Rio Grande do Norte", "sigla": "RN"},
        {"nome": "Rio Grande do Sul", "sigla": "RS"},
        {"nome": "Rondônia", "sigla": "RO"},
        {"nome": "Roraima", "sigla": "RR"},
        {"nome": "Santa Catarina", "sigla": "SC"},
        {"nome": "São Paulo", "sigla": "SP"},
        {"nome": "Sergipe", "sigla": "SE"},
        {"nome": "Tocantins", "sigla": "TO"}
    ]

    for estado in lista_estados:

        nome = estado.get("nome")
        uf = estado.get("sigla")

        # Montar o comando de inserção de dados
        comando = "INSERT INTO tb_estados (nome, uf) VALUES ('{}', '{}');".format(
            nome, uf
        )

        # Passar o comando para o cursor executá-lo
        cursor.execute(comando)

        # "Confirmar" a transação no banco chamando o método commit() da conexão
        conexao.commit()

        print(f"O estado '{nome}' foi salvo com o id {cursor.lastrowid}.")

    # Para trazer dados de consultas, podemos utilizar 3 métodos
    
    comando = "SELECT * FROM tb_estados;"
    resultado = cursor.execute(comando)

    # fetchone(): Trás apenas o primeiro resultado da consulta. Se a consulta não trouxe resultados, retorna None
    print(f"Resultado com fetchone(): {resultado.fetchone()}.")

    # fetchmany(quantidade): Trás um número de registros igual ao valor de quantidade. Se a consulta não trouxe resultados, retorna uma lista vazia.
    print(f"Resultado com fetchmany(): {resultado.fetchmany(10)}.")

    # fetchall(): Trás todos os registros da consulta. Se a consulta não trouxe resultados, retorna uma lista vazia.
    print(f"Resultado com fetchall(): {resultado.fetchall()}.")

    print("*** ATUALIZAR REGISTRO ***")
    comando = "UPDATE tb_estados SET nome = 'DEUTSCH' WHERE uf = 'SC';"
    cursor.execute(comando)
    print(f"Linhas afetadas: {cursor.rowcount}")

    print("*** APAGAR REGISTRO ***")
    comando = "DELETE FROM tb_estados WHERE uf = 'SP' OR uf = 'RJ';"
    cursor.execute(comando)
    print(f"Linhas afetadas: {cursor.rowcount}")

    conexao.commit()
