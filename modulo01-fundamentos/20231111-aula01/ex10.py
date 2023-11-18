"""
Exercício 10

Escreva um programa que leia o salário de um funcionário e exiba o valor do salário líquido, descontando o INSS. As faixas de desconto são as seguintes:

Até R$ 1.320,00 7,5%
De R$ 1.320,01 a R$ 2.571,29 9%
De R$ 2.571,30 até R$ 3.856,94 12%
Acima de R$ 3.856,95 14%
"""

FAIXA_DESCONTO1 = 0.075
FAIXA_DESCONTO2 = 0.09
FAIXA_DESCONTO3 = 0.12
FAIXA_DESCONTO4 = 0.14

if __name__ == "__main__":
    
    salario_bruto = float(input("Informe o seu salário bruto: "))
    salario_liquido = 0
    faixa_de_desconto = ""

    if salario_bruto <= 1320:
        faixa_de_desconto = f"Primeira faixa de desconto: {FAIXA_DESCONTO1 * 100:.2f}%"
        salario_liquido = salario_bruto - (salario_bruto * FAIXA_DESCONTO1)

    elif salario_bruto >= 1320.01 and salario_bruto <= 2751.29:
        faixa_de_desconto = f"Segunda faixa de desconto: {FAIXA_DESCONTO2 * 100:.2f}%"
        salario_liquido = salario_bruto - (salario_bruto * FAIXA_DESCONTO2)

    elif salario_bruto >= 2571.30 and salario_bruto <= 3856.94:
        faixa_de_desconto = f"Terceira faixa de desconto: {FAIXA_DESCONTO3 * 100:.2f}%"
        salario_liquido = salario_bruto - (salario_bruto * FAIXA_DESCONTO3)

    else:
        faixa_de_desconto = f"Quarta faixa de desconto: {FAIXA_DESCONTO4 * 100:.2f}%"
        salario_liquido = salario_bruto - (salario_bruto * FAIXA_DESCONTO4)

    print(f"Seu salário Bruto é de {salario_bruto}.")
    print(f"Você caiu na {faixa_de_desconto}.")
    print(f"Seu salário líquido é de {salario_liquido}.")
