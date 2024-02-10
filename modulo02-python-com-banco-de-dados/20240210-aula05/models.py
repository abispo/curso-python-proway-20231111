from sqlalchemy import (
    Column, Integer, String,
    Date, ForeignKey, Text,
    Table, DateTime, Float,
    func
)

from sqlalchemy.orm import relationship

from config import Base

# Tabela associativa entre as models Postagem e Categoria
# Possui uma sintaxe de criação diferente do padrão
postagens_categorias = Table(
    "tb_postagens_categorias",
    Base.metadata,
    Column("postagem_id", Integer, ForeignKey("tb_postagens.id"), primary_key=True),
    Column("categoria_id", Integer, ForeignKey("tb_categorias.id"), primary_key=True)
)

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
    criado_em = Column(DateTime, server_default=func.now())
    atualizado_em = Column(DateTime, onupdate=func.now())

    perfil = relationship("Perfil", back_populates="usuario", uselist=False)
    postagens = relationship("Postagem", back_populates="usuario")


class Perfil(Base):

    __tablename__ = "tb_perfis"

    id = Column(Integer, ForeignKey("tb_usuarios.id"), primary_key=True)
    nome = Column(String(200), nullable=False)
    data_nascimento = Column(Date, nullable=True)

    usuario = relationship("Usuario", back_populates="perfil", uselist=False)


class Postagem(Base):

    __tablename__ = "tb_postagens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("tb_usuarios.id"), nullable=False)
    titulo = Column(String(200), nullable=False)
    corpo = Column(Text, nullable=False)

    usuario = relationship("Usuario", back_populates="postagens", uselist=False)
    categorias = relationship("Categoria", secondary=postagens_categorias, back_populates="postagens")


class Categoria(Base):

    __tablename__ = "tb_categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(200), nullable=False)

    postagens = relationship("Postagem", secondary=postagens_categorias, back_populates="categorias")


# Models da aula 2 1fn
class Cliente(Base):

    __tablename__ = "tb_clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(300), nullable=False)
    tipo_logradouro = Column(String(20), nullable=False)
    logradouro = Column(String(200), nullable=False)
    numero = Column(String(10), nullable=False)
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    uf = Column(String(2), nullable=False)


class Telefone(Base):

    __tablename__ = "tb_telefones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("tb_clientes.id"), nullable=False)
    telefone = Column(String(30), nullable=False)


# Models da aula 2 2fn
class Servico(Base):

    __tablename__ = "tb_servicos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(200), nullable=False)
    valor_hora = Column(Float, nullable=False)


class Controle(Base):

    __tablename__ = "tb_controle"

    id = Column(Integer, primary_key=True, autoincrement=True)
    servico_id = Column(Integer, ForeignKey("tb_servicos.id"), nullable=False)
    total_horas = Column(Integer, nullable=False)