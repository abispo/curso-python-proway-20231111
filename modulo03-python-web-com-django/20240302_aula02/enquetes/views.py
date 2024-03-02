
# A classe HttpResponse é utilizada quando queremos retornar uma resposta HTTP válida
from django.http.response import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from enquetes.models import Pergunta, Opcao

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
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(
        request,
        "enquetes/resultados.html",
        {"pergunta": pergunta}
    )

def votar(request, pergunta_id):
    
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    try:
        opcao_escolhida = pergunta.opcao_set.get(pk=request.POST["opcao"])
        
    except (KeyError, Opcao.DoesNotExist):
        return render(
            request,
            "enquetes/detalhe.html",
            {
                "mensagem_erro": "Você não escolheu uma opção.",
                "pergunta": pergunta
            }
        )
    
    else:
        opcao_escolhida.votos += 1
        opcao_escolhida.save()

        return redirect(
            reverse("enquetes:resultados", args=(pergunta.id,))
        )