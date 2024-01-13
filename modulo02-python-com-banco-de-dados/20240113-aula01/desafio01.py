import csv
import os
import sqlite3

if __name__ == "__main__":
    
    # Criar a conexão com o banco
    conexao = sqlite3.connect("desafio01.sqlite3")
    
    # Criar o cursor
    cursor = conexao.cursor()

    # "Resetar a tabela"
    comando = "DROP TABLE IF EXISTS tb_cursos;"
    cursor.execute(comando)
    comando = "DROP TABLE IF EXISTS tb_estatisticas_cursos;"
    cursor.execute(comando)
    
    # Criar a tabela de cursos
    comando = """
    CREATE TABLE tb_cursos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        curso   TEXT    NOT NULL,
        carga_horaria   INTEGER NOT NULL,
        preco   REAL NOT NULL
    );
    """

    cursor.execute(comando)

    # Ler o arquivo cursos.csv
    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "cursos.csv")
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        
        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        for curso in arquivo_csv:
            comando = "INSERT INTO tb_cursos(curso, carga_horaria, preco) VALUES ('{curso}', {carga_horaria}, {preco})".format(
                **curso
            )
            cursor.execute(comando)
            conexao.commit()
            print(f"Informações sobre o curso '{curso.get('curso')}' inseridas com sucesso.")

    # Criar a tabela de estatísticas
    comando = """
        CREATE TABLE tb_estatisticas_cursos(
            qtd_cursos INTEGER NOT NULL,
            curso_maior_carga_horaria TEXT NOT NULL,
            curso_com_maior_preco TEXT NOT NULL
        );
    """
    cursor.execute(comando)

    # Pegar a quantidade de cursos cadastrados
    comando = "SELECT COUNT(*) FROM tb_cursos;"
    resultado = cursor.execute(comando)

    qtd_cursos = resultado.fetchone()[0]

    # Pegar o curso com a maior carga horária
    comando = "SELECT * FROM tb_cursos ORDER BY carga_horaria DESC LIMIT 1;"
    resultado = cursor.execute(comando)

    curso_maior_carga_horaria = resultado.fetchone()[1]
    
    # Pegar o curso com o maior preco
    comando = "SELECT * FROM tb_cursos ORDER BY preco DESC LIMIT 1;"
    resultado = cursor.execute(comando)

    curso_com_maior_preco = resultado.fetchone()[1]

    comando = """
    
        INSERT INTO tb_estatisticas_cursos (
            qtd_cursos,
            curso_maior_carga_horaria,
            curso_com_maior_preco
        ) VALUES ({}, '{}', '{}');
    """.format(qtd_cursos, curso_maior_carga_horaria, curso_com_maior_preco)
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
