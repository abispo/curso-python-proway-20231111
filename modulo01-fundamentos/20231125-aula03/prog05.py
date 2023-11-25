"""
Funções (Procedures)

Funções recursivas.

Uma função recursiva, basicamente é uma função que chama a si mesma. Temos que tomar cuidado ao implementar esse tipo de função, pois existe um limite de chamadas que uma função pode fazer a ela mesma, antes que uma exceção seja gerada. Funções recursivas pode ser problemáticas também pela possibilidade de consumir uma grande quantidade de memória.

Exemplo: implementação da função fatorial

5! = 5 * 4 * 3 * 2 * 1      = 120
3! = 3 * 2 * 1              = 6

"""

def fatorial_nao_recursivo(numero):
    contador = numero
    total = numero

    while contador > 1:
        total = total * (contador - 1)
        contador = contador - 1

    return total


def fatorial_recursivo(numero):
    if numero == 1:
        return numero

    return numero * fatorial_recursivo(numero - 1)

if __name__ == "__main__":

    print(fatorial_nao_recursivo(5))
    print(fatorial_nao_recursivo(3))

    print(fatorial_recursivo(5))
