"""
Exercício 04

Escreva um programa que converta uma lista de inteiros em apenas 1 inteiro.
"""

if __name__ == "__main__":

    lista = [5, 9, 13, 14, 70]

    numero_final = ""

    for numero in lista:
        numero_final = f"{numero_final}{numero}"

    print(int(numero_final))

    # Existe outra maneira de se fazer isso, que é usando o método join() de strings
    # print("".join([str(numero) for numero in lista]))