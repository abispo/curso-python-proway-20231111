"""
Exercício 05

Escreva um programa que solicite o nome, a idade e o sexo do usuário. Em seguida, exiba uma mensagem personalizada informando se o usuário é homem ou mulher e se é maior ou menor de idade.

"""

if __name__ == "__main__":

    nome = input("Informe o seu nome: ")
    idade = int(input("Informe a sua idade: "))
    sexo = input("Informe o seu sexo: ")

    mensagem = """
Bem-vindo(a) {}.
Você informou seu sexo como {}.
E você é {} de idade.
"""

    if sexo == "M":
        sexo = "Masculino"
    else:
        sexo = "Feminino"

    if idade >= 18:
        idade = "maior"

    else:
        idade = "menor"

    print(mensagem.format(nome, sexo, idade))