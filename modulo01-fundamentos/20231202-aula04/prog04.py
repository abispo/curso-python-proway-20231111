"""
Trabalhando com arquivos csv (Comma Separated Values - Valores Separados por Vírgula)

Escrevendo em arquivos csv com writer e DictWriter
"""

import csv
import os

if __name__ == "__main__":
    
    carrinho_de_compras = [
        [1, "Pilha AAA", 2, 19.90],
        [2, "Fone de ouvido", 1, 56.40],
        [3, "Teclado Gamer", 1, 111.90],
        [4, "Mousepad homem aranha", 1, 9.90],
        [5, "Monitor Samsung", 1, 680.10],
    ]

    # Abrindo o arquivo
    nome_arquivo = os.path.join(os.getcwd(), "arquivos", "compras.csv")
    with open(nome_arquivo, mode='w', encoding='utf-8', newline="") as arquivo:

        # Criamos o objeto csv writer
        arquivo_csv = csv.writer(arquivo, delimiter=';')

        # Escrevemos na primeira linha do arquivo, os nomes das colunas
        arquivo_csv.writerow(["id", "nome", "quantidade", "valor_unitario"])

        # O método writerows recebe uma lista de listas
        arquivo_csv.writerows(carrinho_de_compras)

    # ------------------------------------------------

    # Trabalhando com o DictWriter
    carrinho_de_compras = [
        {"id": 1, "nome": "Pilha AAA", "quantidade": 2, "valor_unitario": 19.90},
        {"id": 2, "nome": "Fone de ouvido", "quantidade": 1, "valor_unitario": 56.40},
        {"id": 3, "nome": "Teclado Gamer", "quantidade": 1, "valor_unitario": 111.90},
    ]

    # Criamos o arquivo
    nome_arquivo = os.path.join(os.getcwd(), "arquivos", "compras.csv")
    with open(nome_arquivo, mode='w', encoding='utf-8', newline="") as arquivo:

        # Definimos a linha de cabeçalho do arquivo csv
        fieldnames = ["id", "nome", "quantidade", "valor_unitario"]

        # Quando instanciamos a classe DictWriter, indicamos o cabeçalho anterior em fieldnames
        arquivo_csv = csv.DictWriter(arquivo, delimiter=';', fieldnames=fieldnames)

        # O método writeheader() escreve no arquivo csv o cabeçalho, ou seja, os valores de fieldnames
        arquivo_csv.writeheader()

        # Escreve o conteúdo no arquivo recebendo a lista de dicionários
        arquivo_csv.writerows(carrinho_de_compras)
