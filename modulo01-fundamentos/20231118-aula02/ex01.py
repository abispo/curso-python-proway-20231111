"""
Exercício 01

Escreva um programa que receba um número maior do que 1 pelo terminal. Em seguida, o programa retorna a soma de 1 até esse número.
"""

if __name__ == "__main__":

    numero_entrada = int(input("Informe um número maior do que 1: "))
    soma = 0

    for numero in range(1, numero_entrada + 1):
        soma = soma + numero

    print(soma)
