"""
Laços de repetição em Python

Um laço de repetição é um comando que repete a execução de um bloco de código, enquanto uma determinada condição é verdadeira. Caso a condição não seja mais verdadeira, a execução do bloco de código é encerrada.

Em Python, temos 2 comandos de controle de repetição: for e while.

Utilizamos o laço for quando queremos iterar (acessar sequencialmente os itens) um container, que pode ser uma string, uma lista, etc. Enquanto houverem itens a serem lidos desse container, o bloco de código associado ao for será executado.
"""

from random import randint

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
    # lista_pecas = [["Parafuso 2mm", False], "Parafuso 5mm", False]

    # for peca in lista_pecas:
    #     print(peca)

    for tupla in lista_calculo:
        print(f"{tupla[0]}^{tupla[1]} = {pow(tupla[0], tupla[1])}.")

    # Comando break
    # O break interrompe automaticamente a execução do bloco de código. Ou seja, independentemente de existirem mais item a serem lidos, o laço for é interrompido.

    # Exemplo: Imagine uma lista com valores vindos de um sensor. Caso o valor vindo desse sensor seja negativo, paramos imediatamente o laço for

    # Criamos a lista de números randômicos utilizando um list comprehension
    # Basicamente, utilizamos apenas 1 linha para criar a lista e preenchê-la.
    lista_numeros = [randint(-2, 10) for _ in range(100)]

    # As instruções abaixo têm o mesmo efeito que o list comprehension acima
    # lista_numeros = []
    # for _ in range(100):
    #     lista_numeros.append(randint(-2, 10))

    print(lista_numeros)

    for numero in lista_numeros:

        if numero < 0:
            print(f"Valor do sensor negativo! {numero}. Cancelamento automático.")
            break

        print(f"Valor lido do sensor: {numero}.")

    # Comando continue
    # O comando continue interrompe a execução atual do laço, e volta para o início, para o próximo item do container ser processado.

    quantidade_negativos = 0

    for numero in lista_numeros:
        if numero < 0:
            print(f"Valor de sensor negativo! {numero}. Armazenando ao contador")
            quantidade_negativos += 1
            continue

        print(f"Valor lido do sensor: {numero}.")

    print(f"Quantidade de valores maiores ou iguais a 0: {len(lista_numeros)-quantidade_negativos}")
    print(f"Quantidade de valores menores do que 0: {quantidade_negativos}")

    # else
    # O else faz parte da sintaxe do laço for. Ele é executado logo após o laço for finalizar. Detalhe: Caso o comando break seja executado dentro do laço for, o bloco do else não será executado

    lista_valores = [True, True, False, True]

    for valor in lista_valores:
        print(valor)
        if not valor:
            # caso o break seja executado, o bloco de código do else não será.
            break

    else:
        print("Todos os valores foram lidos")