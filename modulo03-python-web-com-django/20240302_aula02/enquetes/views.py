
# A classe HttpResponse é utilizada quando queremos retornar uma resposta HTTP válida
from django.http.response import HttpResponse

from django.shortcuts import render, get_object_or_404

from enquetes.models import Pergunta

"""
As funções criadas dentro do módulo views, devem ser consideradas views que serão ligadas a uma url, criando uma rota
"""

# Obrigatoriamente, todas as funções view devem receber o parâmetro request, mesmo se esse parâmetro não for utilizado
def index(request):
    
    perguntas = Pergunta.objects.order_by('-data_de_publicacao')
    contexto = {
        "perguntas": perguntas
    }

    # Utilizamos a função render para renderizar os templates como respostas HTTP
    return render(
        request,                # O argumento request é obrigatório
        "enquetes/index.html",  # O caminho completo até o template
        context=contexto        # O parâmetro opcional context. Indica as variáveis de contexto que serão passadas para o template
    )
    
def detalhe(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(
        request,
        "enquetes/detalhe.html",
        {"pergunta": pergunta}
    )

def resultados(request, pergunta_id):
    return HttpResponse(f"Você está nos resultados da pergunta {pergunta_id}")

def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando na pergunta {pergunta_id}")