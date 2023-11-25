"""
Exercício 02

Escreva um programa que receba números pelo terminal. Se o usuário digitar o número 0, o programa para de receber números pelo terminal e retorna uma lista dos quadrados desses números.
"""

if __name__ == "__main__":
    lista_quadrados = []

    while True:

        numero = int(input("Informe um número (0 para encerrar): "))

        if numero == 0:
            break

        lista_quadrados.append(numero * numero)

    print(lista_quadrados) 