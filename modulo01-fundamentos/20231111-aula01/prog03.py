"""
Entrada e saída de dados pelo terminal
Variáveis e tipos de dados
Tipos numéricos
"""

if __name__ == "__main__":
    
    """
    O Python possui 3 tipos de dados numéricos

    int     = Tipo inteiro
    float   = Número com casas decimais
    complex = Números complexos (parte inteira e parte imaginária)
    """

    # Exemplo 1: Qual é o maior número
    # A função input() sempre vai retornar uma string, independentemente do que informarmos no terminal.
    # Portanto, precisamos converter o número após recebê-lo.
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))

    if numero1 > numero2:
        print(f"O número {numero1} é maior que {numero2}.")

    elif numero2 > numero1:
        print(f"O número {numero2} é maior que {numero1}.")

    else:
        print(f"Os números {numero1} e {numero2} são iguais.")

    # Exemplo 2
    # Receber 3 números pelo terminal, e calcular a média aritmética.
    # Detalhe: Os números poderão ter casas decimais.
    # No Python, indicamos casas decimais utilizando o . (8.5)
    # Precisamos utilizar a função float() para converter o valor recebido pelo terminal

    numero1 = float(input("Informe a primeira nota: "))
    numero2 = float(input("Informe a segunda nota: "))
    numero3 = float(input("Informe a terceira nota: "))

    soma = numero1 + numero2 + numero3
    media = soma / 3

    # Formatamos o valor para mostrar apenas 1 casa decimal após o ponto
    print(f"A média é igual a {media:.2f}.")