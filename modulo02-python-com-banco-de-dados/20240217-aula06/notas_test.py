from typing import List
import unittest

from notas import processar_texto

class TestNotas(unittest.TestCase):

    def test_processar_texto_deve_retornar_uma_lista_de_floats(self):
        
        # Arrange (Preparação)
        # É onde preparamos os dados do nosso teste
        entrada: str = "João;8.5;8.0;9.0"
        esperado: List[float] = [8.5, 8.0, 9.0]

        # Act (Ação)
        # É onde chamamos as funções que serão testadas
        resultado: List[float] = processar_texto(entrada)

        # Assert (Verificação)
        # É onde verificamos se as saídas estão de acordo com o resultado esperado
        self.assertEqual(resultado, esperado)

        entrada: str = "Maria;9.5;10.0;10.0"
        esperado: List[float] = [9.5, 10.0, 10.0]

        resultado: List[float] = processar_texto(entrada)

        self.assertEqual(resultado, esperado)

        entrada: str = "José;7.0;6.0;8.5"
        esperado: List[float] = [7.0, 6.0, 8.5]

        resultado: List[float] = processar_texto(entrada)

        self.assertEqual(resultado, esperado)

if __name__ == "__main__":
    unittest.main()
