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

load_dotenv()

# Definimos a connection string de acesso
connection_string = os.getenv("CONNECTION_STRING")
