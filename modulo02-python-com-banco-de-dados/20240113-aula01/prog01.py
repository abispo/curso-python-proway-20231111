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

        cursor.execute(comando)

        conexao.commit()
