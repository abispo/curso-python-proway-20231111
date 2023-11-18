"""
Exercício 08

Crie um programa que receba um número inteiro e exiba se ele é par ou ímpar.
"""

if __name__ == "__main__":

    numero = int(input("Informe um número inteiro: "))

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")