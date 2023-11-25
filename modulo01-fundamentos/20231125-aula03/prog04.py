"""
Funções (Procedures)

No Python, também é possível criarmos funções que recebem uma quantidade arbitrária (qualquer) de parâmetros. Ou seja, funções que não sabem exatamente quantos parâmetros serão passados.

1   3   funcao_01
2   8   funcao_02
3   5   funcao_03
"""

def calculo_gas_metano(*args):
    return sum(args) / len(args)


def mostrar_info_usuario(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave.title()}: {valor}")
    print('-'*50)

if __name__ == "__main__":
    
    # Aqui, podemos considerar que os valores passados para os parâmetros estão sendo 'empacotados' da tupla args
    media_sensor_1 = calculo_gas_metano(0.2, 0.0, 0.1)
    media_sensor_2 = calculo_gas_metano(0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.0)
    media_sensor_3 = calculo_gas_metano(0.0, 0.2, 0.4, 0.0, 0.1)

    print(f"Média calculada pelo sensor 1: {media_sensor_1}.")
    print(f"Média calculada pelo sensor 2: {media_sensor_2}.")
    print(f"Média calculada pelo sensor 3: {media_sensor_3}.")

    print('-'*100)

    mostrar_info_usuario(nome="João", idade=30, cidade="Blumenau")
    mostrar_info_usuario(nome="José", endereco="Rua XV de Novembro, 100, Centro")
    mostrar_info_usuario(
        nome="Maria",
        endereco="Rua XV de Novembro, 100, Centro",
        cidade="Blumenau",
        estaco="SC"
    )
    mostrar_info_usuario(nome="Barbara", idade=30)
