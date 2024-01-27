class ValorDeDepositoInvalido(Exception):

    def __init__(self) -> None:
        super().__init__("O valor de deposito deve ser maior do que 0.")


class ValorDeSaqueInvalido(Exception):

    def __init__(self) -> None:
        super().__init__("O valor de saque deve ser igual ou menor que o saldo.")


class ContaBloqueada(Exception):
    def __init__(self) -> None:
        super().__init__("Sua conta está bloqueada para saque. Entre em contato com o seu gerente.")
    