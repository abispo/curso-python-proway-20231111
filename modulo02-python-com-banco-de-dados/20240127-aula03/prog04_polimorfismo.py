"""
Programação Orientada a Objetos em Python

Polimorfismo
Polimorfismo signafica "muitas formas", ou seja, uma função ou método que pode ser chamado de diferentes maneiras, e também que pode retornar de maneiras diferentes (direfentes comportamentos)
"""

class Funcionario:
    
    def __init__(self, nome) -> None:
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    def calcular_salario(self):
        raise NotImplementedError
    

class FuncionarioCLT(Funcionario):
    
    def __init__(self, nome, salario) -> None:
        self._salario = salario
        super().__init__(nome)

    def calcular_salario(self):
        return self._salario
    

class FuncionarioTerceirizado(Funcionario):

    def __init__(self, nome, valor_hora, total_horas) -> None:
        self._valor_hora = valor_hora
        self._total_horas = total_horas
        super().__init__(nome)

    def calcular_salario(self):
        return self._valor_hora * self._total_horas
    

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, qtd_vendas, comissao) -> None:
        self._qtd_vendas = qtd_vendas
        self._comissao = comissao
        super().__init__(nome)

    def calcular_salario(self):
        return self._qtd_vendas * (self._comissao / 100)


class FolhaDePagamento:
    def __init__(self, lista_funcionarios) -> None:
        self._funcionarios = lista_funcionarios


    def calcular(self):
        pass