"""
Programação Orientada a Objetos em Python

Herança
Herança acontece quando uma classe(classe filha ou subclasse) herda atributos e métodos de uma outra classe(classe mãe ou superclasse). 

"""

from excecoes import ContaBloqueada, ValorDeDepositoInvalido, ValorDeSaqueInvalido

class ContaFinanceira:

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
    
    def sacar(self, valor):
        raise NotImplementedError

    def depositar(self, valor):
        raise NotImplementedError


class ContaInvestimento(ContaFinanceira):

    def __init__(self, nome, saldo=0, taxa=0.01) -> None:
        self._taxa = taxa
        super().__init__(nome, saldo)


    def render(self):
        self._saldo = self._saldo + (self._saldo * self._taxa)


class ContaCorrente(ContaFinanceira):
    pass


if __name__ == "__main__":
    conta_cdb_inter = ContaInvestimento(
        nome="Conta CDB Inter", taxa=0.063
    )
    print(conta_cdb_inter)
    conta_cdb_inter.depositar(1)
