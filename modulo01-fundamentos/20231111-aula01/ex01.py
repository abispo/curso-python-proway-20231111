"""
Exercício 01

Crie um programa que peça ao usuário para digitar um número inteiro e exiba se ele é positivo, negativo ou zero.

"""

if __name__ == "__main__":
    
    numero = int(input("Informe um número: "))

    if numero > 0:
        print(f"O número {numero} é maior do que 0.")

    elif numero < 0:
        print(f"O número {numero} é menor do que 0.")

    else:
        print(f"O número {numero} é igual a 0.")
