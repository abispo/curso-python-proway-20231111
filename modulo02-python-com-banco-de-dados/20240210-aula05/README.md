# Acesso a Banco de Dados em Python utilizando o SQLAlchemy
SQLAlchemy é um ORM (Object Relational Mapper/Mapeador Objeto Relacional). Basicamente, o usamos para trabalhar com banco de dados utilizando orientação a objetos

## Atenção!
Apesar de rodar, existem algumas diferenças entre a versão 1.x e 2.x do SQLAlchemy. Acesse o guia de migração para mais detalhes
https://docs.sqlalchemy.org/en/20/changelog/migration_20.html

## Desafio!

Criar a mesma estrutura de models para as tabelas criadas na aula 02, na parte de formas normais (1FN e 2FN). A cada tabela criada, deve-se gerar uma migration e aplicar essa migration.

Para isso, vamos precisar do `alembic`. Aqui está o passo a passo para a instalação e configuração

1. Instalar o `alembic` com o comando `pip install alembic`
2. Criar a estrutura do alembic com o comando `alembic init alembic`
3. Alterar o arquivo `env.py` dentro da pasta alembic, o conteúdo deve estar idêntico ao código abaixo:
    ```python
    from logging.config import fileConfig

    import os

    from sqlalchemy import engine_from_config
    from sqlalchemy import pool

    from alembic import context

    from dotenv import load_dotenv

    load_dotenv()

    # this is the Alembic Config object, which provides
    # access to the values within the .ini file in use.
    config = context.config

    # Interpret the config file for Python logging.
    # This line sets up loggers basically.
    if config.config_file_name is not None:
        fileConfig(config.config_file_name)

    config.set_main_option(
        "sqlalchemy.url",
        os.getenv("CONNECTION_STRING")
    )

    # add your model's MetaData object here
    # for 'autogenerate' support
    # from myapp import mymodel
    # target_metadata = mymodel.Base.metadata
    from models import *
    target_metadata = Base.metadata

    # other values from the config, defined by the needs of env.py,
    # can be acquired:
    # my_important_option = config.get_main_option("my_important_option")
    # ... etc.


    def run_migrations_offline() -> None:
        """Run migrations in 'offline' mode.

        This configures the context with just a URL
        and not an Engine, though an Engine is acceptable
        here as well.  By skipping the Engine creation
        we don't even need a DBAPI to be available.

        Calls to context.execute() here emit the given string to the
        script output.

        """
        url = config.get_main_option("sqlalchemy.url")
        context.configure(
            url=url,
            target_metadata=target_metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
        )

        with context.begin_transaction():
            context.run_migrations()


    def run_migrations_online() -> None:
        """Run migrations in 'online' mode.

        In this scenario we need to create an Engine
        and associate a connection with the context.

        """
        connectable = engine_from_config(
            config.get_section(config.config_ini_section, {}),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

        with connectable.connect() as connection:
            context.configure(
                connection=connection, target_metadata=target_metadata
            )

            with context.begin_transaction():
                context.run_migrations()


    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()
    ```

* Para gerar uma migration, o comando é `alembic revision --autogenerate`
* Para aplicar uma migration gerada, o comando é `alembic upgrade head` 