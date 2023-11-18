"""
Laços de repetição em Python

Um laço de repetição é um comando que repete a execução de um bloco de código, enquanto uma determinada condição é verdadeira. Caso a condição não seja mais verdadeira, a execução do bloco de código é encerrada.

Em Python, temos 2 comandos de controle de repetição: for e while.

Utilizamos o laço for quando queremos iterar (acessar sequencialmente os itens) um container, que pode ser uma string, uma lista, etc. Enquanto houverem itens a serem lidos desse container, o bloco de código associado ao for será executado.
"""

if __name__ == "__main__":

    # Dada uma lista de números, gerar uma nova lista com os quadrados desses números
    lista_numeros = [1, 2, 3, 4, 5]
    lista_quadrados = []

    # Utilizando o laço for para ler os itens da lista
    # A cada iteração, o item atual da lista é salvo na variável numero
    for numero in lista_numeros:

        # O método append() adiciona um novo item no final da lista
        lista_quadrados.append(numero * numero)

    print(lista_quadrados)

    # No laço for, podemos receber mais de 1 valor ao mesmo tempo, assim como recebemos mais de um valor quando "desempacotamos" mais de um valor em variáveis.
    # Por exemplo, uma lista de tuplas, com valores de base e expoente, a serem calculados

    lista_calculo = [(3, 2,), (1, 4,), (4, 7,), (5, 2,), (3, 5,)]

    competidores = ["Mário", "João", "José", "Carlos", "Tiago"]
    lista_pecas = [["Parafuso 2mm", False], "Parafuso 5mm", False]

    for peca in lista_pecas:
        print(peca)

    for tupla in lista_calculo:
        print(f"{tupla[0]}^{tupla[1]} = {pow(tupla[0], tupla[1])}.")