"""
Funções (Procedures)

Funções são blocos de código que podem ser chamadas em qualquer lugar de um programa. As funções podem receber valores a partir de parâmetros, e também retornar valores.

Em Python, utilizamos a palavra reservada 'def' para criar funções.
"""

from datetime import datetime
from time import sleep
from random import randint

# Após o def, precisamos dar um nome para a função
# A função abaixo, não recebe nenhum parâmetro, e imprime a mensagem "Olá"
def ola():
    print("Olá!")

if __name__ == "__main__":

    # Função que retorna a data e hora atuais
    def hora_agora():
        return datetime.now()
    
    # Abaixo chamamos a função ola
    ola()

    # A linha abaixo imprimirá a mensagem, e pois None, pois a função ola não retorna valor algum
    print(ola())

    # Imprimir a data e hora atuais no terminal
    hora_atual = hora_agora()
    sleep(randint(1, 5))
    nova_hora = hora_agora()

    print(hora_atual)
    print(nova_hora)
    diferenca = nova_hora - hora_atual

    print(f"Segundos passados: {diferenca.seconds}s")