"""
Exercício 03

Escreva um programa que leia três números inteiros e exiba o maior e o menor deles.

"""

if __name__ == "__main__":
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    numero3 = int(input("Informe o terceiro número: "))

    lista_numeros = [numero1, numero2, numero3]
    lista_numeros.sort()

    print(f"O menor número informado é o {lista_numeros[0]}")
    print(f"O maior número informado é o {lista_numeros[-1]}")
