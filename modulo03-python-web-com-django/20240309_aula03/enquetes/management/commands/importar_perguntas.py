import csv      # Módulo para se trabalhar com arquivos .csv
import os       # Módulo com funções para trabalhar com o siste de arquivos, dentre outras coisas

from typing import Any

from django.utils import timezone
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
                    pergunta = Pergunta(
                        texto=linha.get("pergunta"),
                        data_de_publicacao=timezone.now()
                    )
                    pergunta.save()

                    Opcao(texto=linha.get("opcao1"), pergunta=pergunta).save() if linha.get("opcao1") else None
                    Opcao(texto=linha.get("opcao2"), pergunta=pergunta).save() if linha.get("opcao2") else None
                    Opcao(texto=linha.get("opcao3"), pergunta=pergunta).save() if linha.get("opcao3") else None
                    Opcao(texto=linha.get("opcao4"), pergunta=pergunta).save() if linha.get("opcao4") else None
                    Opcao(texto=linha.get("opcao5"), pergunta=pergunta).save() if linha.get("opcao5") else None


        except Exception as exc:
            self.stdout.write(str(exc))