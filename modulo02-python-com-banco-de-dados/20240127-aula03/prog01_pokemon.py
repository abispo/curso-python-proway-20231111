"""
Programação Orientada a Objetos

Classes, atributos e métodos
"""

# Utilizamos a palavra reservada 'class' para criar uma classe
class Pokemon:
    
    # O método especial __init__ é o método inicializador da classe, ou seja, é o método chamado quando instanciamos a classe. É semelhante aos métodos construtores em linguagens como Java e C#.
    # Métodos que começam e terminam com duplo underscore '__', também são chamados de métodos mágicos.
    def __init__(self, nome, tipo, vitalidade):
        # self é uma referência ao próprio objeto que está sendo instanciado. É semelhante a palavra reservada 'this' em linguagens como Java e C#
        # Estamos criando os atributos '_nome', '_tipo' e '_vitalidade'. Como o python não possui palavras reservadas para definir se tal objeto é público ou privado, utilizamos a convenção do underscore antes do nome, para definir que esse atributo ou método deve ser tratado como se fosse privado.
        self._nome = nome
        self._tipo = tipo
        self._vitalidade = vitalidade

    # Utilizando getters e setters
    def get_nome(self):
        return self._nome
    
    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self, novo_tipo):
        self._tipo = novo_tipo

    # Utilizando o decorator property
    @property
    def vitalidade(self):
        return self._vitalidade
    
    @vitalidade.setter
    def vitalidade(self, novo_valor):
        self._vitalidade = novo_valor


    # Obrigatoriamente, precisamos passar self como primeiro argumento do método
    def atacar(self):
        # Como o self é referência ao próprio objeto, o utilizamos para acessar os atributos e o métodos do objeto
        print(f"O {self._nome} atacou!")

    def desviar(self):
        print(f"O {self._nome} desviou!")

    def evoluir(self):
        print(f"O {self._nome} evoluiu!")

if __name__ == "__main__":
    # Instanciando a classe Pokemon
    pikachu = Pokemon("Pikachu", "Elétrico", 80)

    # Apesar de ser plenamento possível, não é recomendável acessar diretamente atributos definidos para serem tratados como privados no Python. Para isso, podemos usar 2 estratérias: Utilizar getters e setters, ou o decorador @property
    print(pikachu._nome)

    # Utilizando o getter de nome
    print(pikachu.get_nome())

    # Utilizando getter e setter de tipo
    pikachu.set_tipo("Trovão")
    print(pikachu.get_tipo())

    print(pikachu.vitalidade)
    pikachu.vitalidade = 71
    print(pikachu.vitalidade)