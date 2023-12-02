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
