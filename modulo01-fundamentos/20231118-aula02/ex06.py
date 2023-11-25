"""
Exercicio 06

Escreva um programa que imprima o seguinte padrão no terminal:

#
##
###
####
#####
"""

if __name__ == "__main__":

    MAXIMO = 5
    contador = 1

    while contador <= MAXIMO:
        print('#'*contador)
        contador += 1