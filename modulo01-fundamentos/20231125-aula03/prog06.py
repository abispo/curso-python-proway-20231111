"""
Funções (Procedures)

Funções lambda

No Python, existe a possibilidade de criarmos funções anônimas, ou seja, funções que não possuem nome. Chamamos essas funções de funções lambda.
"""

# Exemplo: Função que verifica se um usuario possui uma característica especial
# Essa função será útil em apenas 1 lugar, não sendo necessária no resto da aplicação

from random import randint

if __name__ == "__main__":
    
    usuario = {
        "nome": "João",
        "e_herdeiro": True
    }

    # lambda: Palavra reservada que indica que estamos criando uma função anônima
    # Podemos indicar que essa função anônima recebe parâmetros. No caso abaixo, ela receberá um parâmetro de nome x. Caso quiséssemos passar mais parâmetros, utilizamos a vírgula para separá-los. Exemplo: lambda x, y, z: x * y * z
    # Em uma função anônima não precisamos utilizar a palavra reservada return para retornar um valor, o que estiver após os 2 pontos (:) será retornado
    herdeiro = lambda x: x.get('e_herdeiro')

    # A linha abaixo imprime no terminal o objeto função lambda. Para executar a função anônima, precisamos utilizar a sintaxe normal de funções
    print(herdeiro)

    print(herdeiro(usuario))

    # Exemplo 2: Filtrar uma lista de usuários apenas com os usuários permitidos

    lista_usuarios = []
    for usuario in ["João", "José", "Maria", "Célia", "Ricardo", "Ronaldo", "Clara", "Barbara"]:
        lista_usuarios.append({
            "nome": usuario,
            "permitido": bool(randint(0, 1))
        })

    print(lista_usuarios)

    lista_usuarios_permitidos = filter(lambda usuario: usuario.get("permitido"), lista_usuarios)
    print(list(lista_usuarios_permitidos))

    print('-'*50)

    carrinho_de_compras = [
        {
            "nome": "Fone de ouvido",
            "quantidade": 4,
            "preco": 9.90,
        },
        {
            "nome": "Teclado Gamer",
            "quantidade": 1,
            "preco": 99
        },
        {
            "nome": "Mouse Gamer",
            "quantidade": 1,
            "preco": 49.90
        }
    ]

    update = lambda x: x.update({"total": x["quantidade"] * x["preco"]})
    update(carrinho_de_compras[0])
    print(update)

    carrinho_final = map(
        lambda x: {"total": x["quantidade"] * x["preco"]},
        carrinho_de_compras
    )

    



    print(list(carrinho_final))