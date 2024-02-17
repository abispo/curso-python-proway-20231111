
import unittest

from unittest.mock import patch

from frases_anime import pegar_frase_anime


class TestFrasesAnime(unittest.TestCase):

    @patch("frases_anime.requests")
    def test_pegar_frase_anime_deve_retornar_info_da_frase(self, requests_mock):
        
        # Arrange
        entrada = "naruto"

        # Aqui estamos definindo como o método json() do objeto retornado pela chamada get() do pacote requests irá se comportar
        requests_mock.get.return_value.json.return_value = {
            "id": 2732,
            "quote": "Once you question your own belief, it's over.",
            "anime": "Naruto",
            "character": "Naruto Uzumaki"
        }

        esperado = {
            "id": 2732,
            "quote": "Once you question your own belief, it's over.",
            "anime": "Naruto",
            "character": "Naruto Uzumaki"
        }

        # Act
        resultado = pegar_frase_anime(entrada)

        # Assert
        self.assertDictEqual(resultado, esperado)

        requests_mock.get.assert_called_once_with(url="https://animechan.xyz/api/random/anime?title=naruto")
        

