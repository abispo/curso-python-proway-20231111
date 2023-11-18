"""
Exercício 07

Faça um programa que receba uma temperatura em graus Celsius e exiba a temperatura equivalente em graus Fahrenheit. A fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32.
"""

if __name__ == "__main__":

    graus_celsius = float(input("Informe a temperatura em graus Celsius: "))
    graus_fahrenheit = (graus_celsius * (9/5)) + 32

    print(f"{graus_celsius} convertidos para Fahrenheit é igual a {graus_fahrenheit}.")