"""
Programação Orientada a Objetos em Python

Encapsulamento
É o processo onde "protegemos" informações internas do objeto, e definimos as "interfaces" públicas que darão acesso aos atributos e/ou métodos privados do objeto, sendo possível assim alterar o estado do objeto.
"""

from random import randint

from excecoes import ContaBloqueada, ValorDeDepositoInvalido, ValorDeSaqueInvalido

class ContaBancaria:

    def __init__(self, nome, saldo=0) -> None:
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValorDeDepositoInvalido
        
        self._saldo = self._saldo + valor

    def sacar(self, valor):
        if bool(randint(0, 1)):
            raise ContaBloqueada
        
        if valor > self._saldo:
            raise ValorDeSaqueInvalido
        
        self._saldo = self._saldo - valor

if __name__ == "__main__":

    saida = """
INFORME A OPÇÃO DESEJADA
0 - SAIR
1 - VER SALDO
2 - DEPOSITAR
3 - SACAR
"""

    try:
        conta_viacredi = ContaBancaria("Conta Corrente Viacredi")

        while True:
            opcao = int(input("Informe a opção desejada: "))

            match opcao:
                case 0:
                    print("Finalizando...")
                    break

                case 1:
                    print(f"O seu saldo é de {conta_viacredi.saldo}.")

                case 2:
                    valor = float(input("Informe um valor para depósito: "))
                    conta_viacredi.depositar(valor)

                case 3:
                    valor = float(input("Informe o valor para saque: "))
                    conta_viacredi.sacar(valor)

            
    except Exception as exc_info:
        print(exc_info)
