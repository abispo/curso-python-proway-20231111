from config import Base, conexao

from models import *

if __name__ == "__main__":
    Base.metadata.create_all(conexao)