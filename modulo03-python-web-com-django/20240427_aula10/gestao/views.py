from datetime import datetime

from django.contrib.auth.decorators import (
    login_required,
    permission_required
)
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from gestao.models import Imovel
from registro.models import Perfil

def index(request):
    return render(
        request,
        "gestao/index.html"
    )

@login_required
def meu_perfil(request: HttpRequest):

    if request.user.has_perm("registro.perfil_bloqueado"):
        return render(
            request,
            "gestao/nao_autorizado.html"
        )

    if request.method == "GET":

        atualizado_com_sucesso = int(request.GET.get("atualizado_com_sucesso", "0"))

        return render(
            request,
            "gestao/meu_perfil.html",
            {"atualizado_com_sucesso": bool(atualizado_com_sucesso)}
        )
    
    if request.method == "POST":
        usuario = request.user

        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        email = request.POST.get("email")
        documento = request.POST.get("documento")
        genero = request.POST.get("genero")
        data_de_nascimento = request.POST.get("data_de_nascimento")

        usuario.first_name = nome
        usuario.last_name = sobrenome
        usuario.email = email

        perfil_usuario = Perfil.objects.get(pk=usuario.id)
        
        perfil_usuario.documento = documento
        perfil_usuario.genero = genero

        data_de_nascimento = datetime.strptime(
            data_de_nascimento, "%Y-%m-%d"
        ).date()

        perfil_usuario.data_de_nascimento = data_de_nascimento

        usuario.save()
        perfil_usuario.save()
        
        return redirect(
            f"{reverse('gestao:meu_perfil')}?atualizado_com_sucesso=1"
        )
    
@login_required
def nao_autorizado(request: HttpRequest):
    return render(
        request,
        "gestao/nao_autorizado.html"
    )

@login_required
def lista_imoveis(request: HttpRequest):

    lista_imoveis = Imovel.objects.filter(disponivel=True)
    imoveis = []

    for imovel in lista_imoveis:

        imovel_id = imovel.id
        descricao = imovel.descricao
        preco_diaria = imovel.informacaoalugueltipocontratoimovel_set.filter(tipo_contrato=1).first()
        preco_mensal = imovel.informacaoalugueltipocontratoimovel_set.filter(tipo_contrato=2).first()

        dados_imovel = {
            "id": imovel_id,
            "descricao": descricao,
            "preco_diaria": None if not preco_diaria else preco_diaria.valor,
            "preco_mensal": None if not preco_mensal else preco_mensal.valor
        }

        imoveis.append(dados_imovel)
    
    return render(
        request,
        "gestao/lista_imoveis.html",
        {
            "imoveis": imoveis
        }
    )

@login_required
def detalhe_imovel(request: HttpRequest, imovel_id: str):

    imovel = get_object_or_404(Imovel, pk=imovel_id)

    preco_diaria = imovel.informacaoalugueltipocontratoimovel_set.get(tipo_contrato=1).first()
    preco_mensal = imovel.informacaoalugueltipocontratoimovel_set.get(tipo_contrato=2).first()

    detalhes_precos = {
        "preco_diaria": None if not preco_diaria else preco_diaria,
        "preco_mensal": None if not preco_mensal else preco_mensal
    }

    return render(
        request,
        "gestao/detalhe_imovel.html",
        {
            "imovel": imovel,
            "detalhes_precos": detalhes_precos
        }
    )