"""
Exercício 03

Escreva um programa que gere 100 números randômicos de 1 a 100. Em seguida, crie 2 listas: Uma que irá salvar apenas os números pares, e outra que irá salvar apenas os números ímpares. Em seguida, mostre na tela a quantidade de itens de cada lista e quais são os seus valores. Exemplo:
"""

from random import randint

if __name__ == "__main__":
    
    # Criar a lista usando list comprehension
    lista_randomicos = [randint(1, 100) for _ in range(100)]

    lista_pares = []
    lista_impares = []

    for numero in lista_randomicos:
        
        if numero % 2 == 0:
            lista_pares.append(numero)

        else:
            lista_impares.append(numero)

    print(f"Quantidade de itens na lista de pares: {len(lista_pares)}")
    print(f"Itens da lista de pares: {lista_pares}")

    print(f"Quantidade de itens na lista de ímpares: {len(lista_impares)}")
    print(f"Itens da lista de pares: {lista_impares}")