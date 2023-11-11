"""
Entrada e saída de dados pelo terminal
Variáveis e tipos de dados
Strings
"""

"""
Apesar de não ser obrigatório, é considerada uma boa prática indicarmos quando o arquivo será executado diretamente pelo interpretador python. Verificamos se o valor da variável __name__ é igual a __main__. Se sim, o código será executado.
"""

if __name__ == "__main__":
    
    """
    print(valor) - Imprime no terminal o valor passado como parâmetro
    input() - Captura um valor digitado pelo terminal.

    Exemplo: Mensagem de boas vindas
    """

    nome = input("Informe o seu nome: ")
    curso = input("Informe o seu curso: ")

    # Concatenando as strings com +
    print("Olá " + nome + ". Bem vindo(a) ao curso " + curso + ".")

    # Utilizando o método .format()
    print("Olá {}. Bem vindo(a) ao curso {}.".format(nome, curso))

    # Utilizando f-strings
    print(f"Olá {nome}. Bem vindo(a) ao curso {curso}.")
