# Arquivo de configuração do SQLAlchemy

import os

from dotenv import load_dotenv

# create_engine é a função responsável por criar um conexão com o banco de dados
from sqlalchemy import create_engine

# A partir da função declarative_base, vamos criar a classe Base que todas as nossas models irão herdar.
# Model é o termo usado para indicar uma classe que está mapeada para uma tabela no banco de dados
from sqlalchemy.ext.declarative import declarative_base

# A função sessionmaker irá criar a sessão de acesso ao banco de dados. Podemos ter mais de 1 sessão pro mesmo banco, ou bancos diferentes
from sqlalchemy.orm import sessionmaker

# Carregando as variáveis de ambiente a partir do arquivo .env
load_dotenv()

# Definimos a connection string de acesso
connection_string = os.getenv("CONNECTION_STRING")

# A variável conexao representa a conexão com o banco de dados, que utiliza a connection_string abaixo. O argumento echo=True vai mostrar no terminal os comandos SQL que serão executados
conexao = create_engine(connection_string, echo=True)

# Base é a classe de onde todas as nossas models herdarão. Se uma classe que foi criada não estiver herdando de Base, ela não será mapeada para uma tabela no banco de dados
Base = declarative_base()

# Aqui estamos criando a sessão de acesso ao banco, utilizando o objeto conexao que foi criado anteriormente
Session = sessionmaker(bind=conexao)
sessao = Session()