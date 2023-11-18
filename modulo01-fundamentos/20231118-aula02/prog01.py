"""
Estruturas de condição

match case

O match case é a segunda estrutura de controle de condição no Python. Foi introduzida a partir da versão 3.10 da linguagem. Basicamente é o correspondente em Python do switch case, de linguagens como C# e Java.

É recomendado utilizar o match case em comparações mais simples, onde sabemos exatamente a quantidade de opções que podemos processar. Já o if utilizamos em comparações mais complexas.
"""

if __name__ == "__main__":

    nivel_de_acesso = int(input("Informe o nivel de acesso: "))

    match nivel_de_acesso:
        case 1:
            print("Seu nível de acesso é de administrador.")

        case 2:
            print("Seu nível de acesso é de moderador.")

        case 3:
            print("Seu nível de acesso é de usuário.")

        # Caso nenhuma das verificações anteriores resulte em True, chama o caso padrão
        case _:
            print("Nível de acesso desconhecido.")
