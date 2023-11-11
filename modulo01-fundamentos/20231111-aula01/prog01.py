
# Isso é um comentário
# Comentários não são executados pelo interpretador

# A função print mostra uma mensagem no terminal.
# No caso abaixo, estamos imprimindo no terminal o texto "Olá Mundo"
# Em Python, tudo que está entre aspas simples ou aspas duplas é uma string (texto)
# A função print() aceita como argumento qualquer expressão válida em Python
print("Olá mundo!")
print(2 + 2)

# Algumas regras da linguagem

# Python é uma linguagem case-sensitive, ou seja, a variável Nome é diferente da variável nome

Nome = "José"
nome = "Maria"

print(Nome)
print(nome)

# No Python, não temos caracteres que representam um comentário de várias linhas
"""
Para isso, utilizamos o formato de string multilinha. Uma string multilinha sempre começa com 3 aspas simples (ou duplas) e termina com 3 aspas simples (ou duplas)
"""

"""
A principal característica da sintaxe do Python, é que o espaçamento depois da criação de um bloco de código é checado como regra de sintaxe.
"""

idade = 20

"""
Sempre que temos 2 pontos (:), significa que estamos criando um novo bloco de código. Quando um novo bloco de código é criado, deve ser respeitado o espaçamento para a linha anterior. Por padrão, o espaçamento é de 4 espaços.
"""
if nome == "Maria":
    print("ok")
    
    if idade == 20:
        print("Ok")

print("fora")