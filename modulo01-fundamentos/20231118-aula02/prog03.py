"""
Laços de repetição em Python

Um laço de repetição é um comando que repete a execução de um bloco de código, enquanto uma determinada condição é verdadeira. Caso a condição não seja mais verdadeira, a execução do bloco de código é encerrada.

Em Python, temos 2 comandos de controle de repetição: for e while.

Utilizamos o laço while quando precisamos repetir a execução de um bloco de código enquanto uma determinada condição é verdadeira. Caso a condição não seja mais verdadeira, o bloco de código não é mais executado.
"""

from random import randint

if __name__ == "__main__":
    
    # Exemplo1: Sorteio de números utilizando o laço while

    cartela = [3, 7, 2, 1, 9]
    contador = 0
    numero_acertos = 0

    while contador < 5:

        numero_sorteado = randint(1, 10)
        print(f"Número sorteado: {numero_sorteado}")

        if numero_sorteado in cartela:
            numero_acertos += 1

        contador += 1

    print(f"Números da sua cartela: {cartela}")
    print(f"Quantidade de acertos: {numero_acertos}")


    # Assim como no laço while, também podemos utilizar o comando break dentro de bloco de código, que irá interromper o laço imediatamente.

    # Exemplo 2: Criar um algoritmo que simule uma batalha entre 2 personagens de um jogo

    # Abaixo, criamos 2 dicionários: Um para o personagem e outro para o monstro, no caso, um orc.
    # Dicionário é um dos tipos de dados em Python, ele se caracteriza por ter uma estrutura chave-valor: Para cada chave, apenas 1 valor está associado a essa chave, e vice-versa. Como valores, podemos ter quaisquer tipos de dados em Python, como strings, numeros, listas, e até mesmo outro dicionário. Como chave, apenas podemos utilizar strings, tipos numéricos ou tipos booleanos.
    personagem = {
        "HP": 13,
        "Ataque": 4,
        "Defesa": 4
    }

    orc = {
        "HP": 19,
        "Ataque": 3,
        "Defesa": 5
    }

    while True:
        
        print("Personagem atacando orc!")
        dado_personagem = randint(1, 6)
        dado_orc = randint(1, 6)

        ataque_personagem = personagem.get("Ataque") + dado_personagem
        defesa_orc = orc.get("Defesa") + dado_orc

        if ataque_personagem > defesa_orc:
            dano = ataque_personagem - defesa_orc
            print(f"Personagem desferiu {dano} de dano ao orc")
            orc["HP"] -= dano

        else:
            print("O orc defendeu o ataque!")

        if orc["HP"] <= 0:
            print("O personagem derrotou o orc!")
            break

        print("Orc atacando personagem")
        dado_personagem = randint(1, 6)
        dado_orc = randint(1, 6)

        ataque_orc = orc["Ataque"] + dado_orc
        defesa_personagem = personagem["Defesa"] + dado_personagem

        if ataque_orc > defesa_personagem:
            dano = ataque_orc - defesa_personagem
            print(f"Orc desferiu {dano} de dano ao personagem")
            personagem["HP"] -= dano

        else:
            print("O personagem defendeu o ataque.")

        if personagem["HP"] <= 0:
            print("O orc derrotou o personagem")
            break

        print('-'*50)

    # Também podemos utilizar o continue dentro de um laço while

    lista_valores = [1, 5, 5.2, 5.8, "Python", [2, 3], (1, 3, 7), {"nome": "José"}]

    indice = 0
    soma = 0

    while indice < len(lista_valores):

        if not isinstance(lista_valores[indice], int):
            print("O valor não é um número inteiro")
            indice += 1
            continue

        soma += lista_valores[indice]
        indice += 1

    else:
        print("Todos os valores foram lidos")

    print(f"Soma: {soma}")