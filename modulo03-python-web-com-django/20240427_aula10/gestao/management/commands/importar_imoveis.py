import csv      # Módulo para se trabalhar com arquivos .csv
import os       # Módulo com funções para trabalhar com o siste de arquivos, dentre outras coisas

from typing import Any

from django.core.management.base import BaseCommand, CommandParser

import requests

from gestao.models import Imovel

class Command(BaseCommand):
    help = "Importa um arquivo .csv com dados de imóveis"

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
                    id = linha.get("id")
                    tipo_logradouro = linha.get("tipo_logradouro")
                    logradouro = linha.get("logradouro")
                    numero = linha.get("numero")
                    complemento = linha.get("complemento")
                    bairro = linha.get("bairro")
                    cidade = linha.get("cidade")
                    estado = linha.get("estado")
                    descricao = linha.get("descricao")
                    disponivel = bool(int(linha.get("disponivel")))

                    Imovel(
                        id=id,
                        tipo_logradouro=tipo_logradouro,
                        logradouro=logradouro,
                        numero=numero,
                        complemento=complemento,
                        bairro=bairro,
                        cidade=cidade,
                        estado=estado,
                        descricao=descricao,
                        disponivel=disponivel
                    ).save()

                    self.stdout.write(f"Imovel de id '{id}' salvo com sucesso.")

        except Exception as exc:
            self.stdout.write(str(exc))