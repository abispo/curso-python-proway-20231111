"""
Exercicio 09

Escreva um programa em Python que gere uma lista randômica de 50 números de 1 até 50. Em seguida, retire os valores repetidos dessa lista (utilize a função randint() do pacote random)
"""

from random import randint

if __name__ == "__main__":

    lista = [randint(1, 50) for _ in range(50)]

    print(f"Lista inicial: {lista}")
    print(f"Lista final: {list(set(lista))}")