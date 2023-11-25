"""
Exercicio 07

Escreva um programa que receba nome, idade e sexo de 5 usuários. Em seguida, mostre quantos usuários são do sexo masculino, quantos são do sexo feminino e qual é a média de idade. Exemplo:
Nome: João
Idade: 32
Sexo: M

Nome: Maria
Idade: 17
Sexo: F

Nome: Vanessa
Idade: 28
Sexo: F

Quantidade de usuários do sexo masculino: 1
Quantidade de usuários do sexo feminino: 2
Média de idade: 25.67
"""

if __name__ == "__main__":
    MAXIMO = 5
    contador = 0

    qtd_sexo_masculino = 0
    qtd_sexo_feminino = 0
    soma_idade = 0

    lista_usuarios = []

    while contador < MAXIMO:

        nome = input("Informe o nome do usuário: ")
        idade = int(input("Informe a idade do usuário: "))
        sexo = input("Informe o sexo do usuário: ")

        lista_usuarios.append(
            {
                "nome": nome,
                "idade": idade,
                "sexo": sexo
            }
        )

        print(f"Usuário '{nome}' inserido com sucesso!")
        contador += 1

    for usuario in lista_usuarios:
        if usuario.get("sexo") == "M":
            qtd_sexo_masculino += 1

        else:
            qtd_sexo_feminino += 1

        soma_idade += usuario.get("idade")

    print(f"Quantidade de usuários do sexo masculino: {qtd_sexo_masculino}.")
    print(f"Quantidade de usuários do sexo feminino: {qtd_sexo_feminino}.")
    print(f"Média de idade: {soma_idade / MAXIMO}")