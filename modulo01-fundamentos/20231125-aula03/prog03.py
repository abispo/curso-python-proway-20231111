"""
Funções (Procedures)

Parâmetros (parte 2)

Também podemos criar parâmetros que não são obrigatórios em uma função. Nesse caso, precisamos definir um valor padrão para esses parâmetro
"""

def calculo_salario_funcionario(nome, setor=1, valor_hora=0, qtd_horas=0):
    
    if setor == 1:
        return (nome, 2000,)

    else:
        return (nome, valor_hora * qtd_horas)


if __name__ == "__main__":

    print(f"O funcionário Roberto irá receber {calculo_salario_funcionario('Roberto')[1]}")
    print(f"O funcionário Rui irá receber {calculo_salario_funcionario('Rui', 2, 80, 17)[1]}")