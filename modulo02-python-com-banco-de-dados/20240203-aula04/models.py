from sqlalchemy import Column, Integer, String

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
