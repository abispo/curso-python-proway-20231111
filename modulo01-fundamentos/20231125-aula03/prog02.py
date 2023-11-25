"""
Funções (Procedures)

Também podemos passar valores que serão acessíveis dentro das funções. Ou seja, podemos criar funções com parâmetros (ou argumentos) que irão receber os valores
"""

def calculo_imc(altura, peso):
    return peso / (altura * altura)

if __name__ == "__main__":
    
    print(f"Cálculo de IMC: Altura: 1.81. Peso: 101.4: {calculo_imc(1.81, 101.4):.2f}.")

    # A chamada do calculo_imc abaixo irá gerar uma exceção, pois estamos passando apenas 1 argumento para a função que espera receber 2. Quando não definimos valores padrão para os parâmetros da função, esses parâmetros são obrigários ou posicionais, ou seja, precisamos passar valores a eles
    try:
        print(f"Cálculo de IMC: Altura: 1.81. Peso: 101.4: {calculo_imc(101.4):.2f}.")

    except Exception as exc:
        print(exc)

    # Além de passar os valores por posição, podemos também indicar qual parâmetro receberá qual valor. Chamamos isso de passagem de valores por nome de parâmetro (keyword)
    print(f"Cálculo de IMC: Altura: 1.71. Peso: 81.7: {calculo_imc(peso=81.7, altura=1.71):.2f}.")

    print('-'*50)
    lista_calculo_imc = [[1.68, 100], [1.87, 88], [1.76, 91]]

    # Caso queiramos, podemos desempacotas os valores dos parâmetros na chamada da função. Para isso, precisamos utilizar a sintaxe do asterisco (*sequencia)
    for valor in lista_calculo_imc:
        # A função calculo_imc está sendo chamada passando os parâmetros de maneira posicional
        # A chamada nesse caso, é assim: calculo_imc(1.68, 100)
        print(f"Cálculo de IMC: Altura: {valor[0]}. Peso: {valor[1]}: {calculo_imc(*valor):.2f}.")

    print('-'*50)
    # Também é possível desempacotar os valores dos parâmetros informando o nome do parâmetro. Nesse caso, precisamos trabalhar com dicionários
    lista_calculo_imc = [
        {"altura": 1.67, "peso": 58},
        {"altura": 1.99, "peso": 99.1},
        {"altura": 1.74, "peso": 97.5},
        {"altura": 2.09, "peso": 109.9},
        {"altura": 1.80, "peso": 80.7},
    ]

    for valor in lista_calculo_imc:
        # A função calculo_imc está sendo chamada passando os valores para os parâmetros por nome
        # A chamada abaixo nesse caso ficaria assim: calculo_imc(altura=1.67, peso=58)
        print(f"Cálculo de IMC: Altura: {valor.get('altura')}. Peso: {valor.get('peso')}: {calculo_imc(**valor):.2f}.")
