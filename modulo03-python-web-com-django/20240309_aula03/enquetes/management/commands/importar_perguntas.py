import csv      # Módulo para se trabalhar com arquivos .csv
import os       # Módulo com funções para trabalhar com o siste de arquivos, dentre outras coisas
from typing import Any
from django.core.management.base import BaseCommand, CommandParser

import requests

from enquetes.models import Pergunta, Opcao

class Command(BaseCommand):
    help = "Importa um arquivo .csv com perguntas e opções."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("arquivo", type=str)

    def handle(self, *args: Any, **options: Any) -> str | None:
        
        try:
            caminho = options.get('arquivo')
            resposta = requests.get(caminho)

            pasta_arquivos = os.path.join(os.getcwd(), "arquivos")

            if not os.path.exists(pasta_arquivos):
                os.mkdir(pasta_arquivos)

            caminho_arquivo = os.path.join(pasta_arquivos, "dados.csv")

            with open(caminho_arquivo, "w", encoding='utf-8') as arquivo:
                arquivo.write(resposta.text)

            with open(caminho_arquivo, "r", encoding='utf-8') as arquivo:
                arquivo_csv = csv.DictReader(arquivo, delimiter=';')

                for linha in arquivo_csv:
                    pergunta = Pergunta(texto=linha.get("pergunta"))
                    Opcao(texto=linha.get("opcao")) if linha.get("opcao") else None

        except Exception as exc:
            self.stdout.write(str(exc))