"""
Exercicio 08

Escreva um programa em Python que inverta uma lista de números. Exemplo:
"""

if __name__ == "__main__":
    lista = [4, 8, 5, 9, 0]

    print(f"Lista inicial: {lista}")
    # Aqui utilizamos o slicing (fatiamento de listas)
    # Passamos o step como -1 para inverter a lista
    print(f"Lista final: {lista[::-1]}")
