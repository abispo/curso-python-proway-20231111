"""
Programação Orientada a Objetos

Composição
Ocorre quando uma classe compõe ou é composta de uma ou mais classes
"""

from random import shuffle

class Carta:
    
    def __init__(self, naipe, valor):
        self._naipe = naipe
        self._valor = valor

    def __repr__(self) -> str:
        return f"{self._valor}{self._naipe}"
    
    def __str__(self) -> str:
        return f"{self._valor}{self._naipe}"

class Baralho:
    
    def __init__(self) -> None:
        self._cartas = []

        self._valores = [
            '2', '3', '4', '5',
            '6', '7', '8', '9',
            '10', 'J', 'Q', 'K',
            'A' 
        ]

        self._naipes = [
            "\u2660", "\u2665", "\u2666", "\u2663"
        ]

        self._construir()
        shuffle(self._cartas)

    def pegar_carta(self):
        return self._cartas.pop()

    def __repr__(self) -> str:
        return ", ".join([str(carta) for carta in self._cartas])

    def _construir(self):
        for valor in self._valores:
            for naipe in self._naipes:
                self._cartas.append(Carta(naipe, valor))

if __name__ == "__main__":
    
    baralho = Baralho()
    cartas = [baralho.pegar_carta(), baralho.pegar_carta()]

    print(f"Sua mão é: {cartas}")

    flop = [baralho.pegar_carta(), baralho.pegar_carta(), baralho.pegar_carta()]
    print(f"O flop é: {flop}")