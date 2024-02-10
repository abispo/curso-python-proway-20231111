# Acesso a Banco de Dados em Python utilizando o SQLAlchemy
SQLAlchemy é um ORM (Object Relational Mapper/Mapeador Objeto Relacional). Basicamente, o usamos para trabalhar com banco de dados utilizando orientação a objetos

## Atenção!
Apesar de rodar, existem algumas diferenças entre a versão 1.x e 2.x do SQLAlchemy. Acesse o guia de migração para mais detalhes
https://docs.sqlalchemy.org/en/20/changelog/migration_20.html

## Desafio!

Replicar a estrutura das tabelas da aula 02 (relacionamentos) em models no SQLAlchemy. Ou seja, você irá criar as seguintes models:

* Usuario
* Perfil
* Postagem
* Categoria

Não esqueça de criar as [relações entre as tabelas](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html). Para isso, você precisará usar a classe `ForeignKey`, que está no pacote `sqlalchemy`.