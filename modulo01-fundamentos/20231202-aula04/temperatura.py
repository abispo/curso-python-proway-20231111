"""
Script que busca os dados de temperatura de uma cidade qualquer via API.

Esse script deve salvar os dados em um arquivo csv com o nome da cidade. Por exemplo: blumenau.csv. Esse arquivo deve ter as seguintes colunas
cidade              -> Nome informado da cidade
temperatura         -> chave 'temperature'
vento               -> chave 'wind'
descricao           -> chave 'description'
temperatura_d1      -> chave 'temperature' do primeiro item da lista 'forecast'
temperatura_d2      -> chave 'temperature' do segundo item da lista 'forecast'
temperatura_d3      -> chave 'temperature' do terceiro item da lista 'forecast'
ultima_atualizacao  -> retorno do método datetime.now() formatado em dd/mm/yyyy hh:mm:ss

Detalhe: O arquivo deve ser atualizado a cada chamada, portanto utilize o modo de abertura 'a' para o conteúdo não ser sobrescrito.

Exemplo de chamada da API, pegando os dados de temperatura de Blumenau
https://goweather.herokuapp.com/weather/blumenau

"""

import os
from datetime import datetime

import requests

# https://goweather.herokuapp.com/weather/blumenau
