
# A classe HttpResponse é utilizada quando queremos retornar uma resposta HTTP válida
from django.http.response import HttpResponse

from django.shortcuts import render

"""
As funções criadas dentro do módulo views, devem ser consideradas views que serão ligadas a uma url, criando uma rota
"""

# Obrigatoriamente, todas as funções view devem receber o parâmetro request, mesmo se esse parâmetro não for utilizado
def index(request):
    return HttpResponse("Você está na página principal do módulo de enquetes.")

def detalhe(request, pergunta_id):
    return HttpResponse(f"Você está nos detalhes da pergunta {pergunta_id}")

def resultados(request, pergunta_id):
    return HttpResponse(f"Você está nos resultados da pergunta {pergunta_id}")

def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando na pergunta {pergunta_id}")