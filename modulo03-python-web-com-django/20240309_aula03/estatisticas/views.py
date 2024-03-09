from django.db.models import Count, Sum, Avg
from django.shortcuts import render

from enquetes.models import Pergunta, Opcao

def index(request):

    quantidade_perguntas_cadastradas = Pergunta.objects.count()
    quantidade_opcoes_cadastradas = Opcao.objects.count()
    lista_perguntas_ordenada_quantidade_votos = Pergunta.objects.annotate(
        num_votos=Sum("opcao__votos")
    ).order_by('-num_votos')[:10]
    media_opcoes_por_pergunta = Pergunta.objects.annotate(
        num_opcoes=Count('opcao')
    ).aggregate(media_opcoes=Avg("num_opcoes"))

    contexto = {
        "quantidade_perguntas_cadastradas": quantidade_perguntas_cadastradas,
        "quantidade_opcoes_cadastradas": quantidade_opcoes_cadastradas,
        "lista_perguntas_ordenada_quantidade_votos": lista_perguntas_ordenada_quantidade_votos,
        "media_opcoes_por_pergunta": media_opcoes_por_pergunta["media_opcoes"]
    }

    return render(
        request,
        "estatisticas/index.html",
        context=contexto
    )