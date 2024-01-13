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
    pass
