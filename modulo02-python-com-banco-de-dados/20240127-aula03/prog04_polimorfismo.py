"""
Programação Orientada a Objetos em Python

Polimorfismo
Polimorfismo signafica "muitas formas", ou seja, uma função ou método que pode ser chamado de diferentes maneiras, e também que pode retornar de maneiras diferentes (diferentes comportamentos)
"""

from mensagens import mensagem_calculo_folha

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
        print("=== CÁLCULO DE FOLHA DE PAGAMENTO ===")
        print("-------------------------------------\n")

        for funcionario in self._funcionarios:
            saida = mensagem_calculo_folha.format(
                funcionario.nome,
                funcionario.__class__.__name__,
                funcionario.calcular_salario()
            )
            print(saida)

if __name__ == "__main__":
    lista_funcionarios = [
        FuncionarioCLT("João da Silva", 1850),
        FuncionarioTerceirizado("Maria das Dores", 75, 112),
        FuncionarioTerceirizado("José dos Reis", 83.50, 43),
        FuncionarioComissionado("Amanda Ribeiro", 84561.98, 10),
        FuncionarioComissionado("Bruna Almeida", 124932.53, 8.5)
    ]

    FolhaDePagamento(lista_funcionarios).calcular()