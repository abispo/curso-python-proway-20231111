from sqlalchemy import Column, Integer, String, Date, ForeignKey

from config import Base

class Dica(Base):
    
    # Indica o nome da tabela que será criada no banco
    __tablename__ = "tb_dicas"

    # Campo id, do tipo inteiro, chave primária e auto incremento
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Campo texto, tipo string com tamanho máximo de 300 e que não permite nulos
    texto = Column(String(300), nullable=False)

    def __str__(self):
        return f"{str(self.id).zfill(2)}. {self.texto}"


class Usuario(Base):

    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    senha = Column(String(200), nullable=False)


class Perfil(Base):

    __tablename__ = "tb_perfis"

    id = Column(Integer, ForeignKey("tb_usuarios.id"), primary_key=True)
    nome = Column(String(200), nullable=False)
    data_nascimento = Column(Date, nullable=True)