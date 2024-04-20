from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from registro.models import Perfil

def index(request):
    return render(
        request,
        "gestao/index.html"
    )

@login_required
def meu_perfil(request: HttpRequest):

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