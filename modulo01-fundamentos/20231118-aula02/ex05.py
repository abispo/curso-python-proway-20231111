"""
Exercicio 05

Escreva um programa que gere números randômicos de 0 até 50. Salve esse números em uma lista. Em seguida, informe quais são o maior e o menor número dessa lista. Dica: Utilize as funções built-in max() e min().
"""

from random import randint

if __name__ == "__main__":

    lista_randomicos = [randint(1, 50) for _ in range(50)]

    print(lista_randomicos)
    print(f"Maior número: {max(lista_randomicos)}")
    print(f"Menor número: {min(lista_randomicos)}")