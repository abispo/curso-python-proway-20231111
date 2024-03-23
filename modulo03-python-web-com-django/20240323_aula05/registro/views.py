from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from registro.forms import PreRegistroForm
from registro.models import PreRegistro

def pre_registro(request: HttpRequest):

    if request.method == "GET":
        form = PreRegistroForm()

        return render(
            request,
            "registro/pre_registro.html",
            {"form": form}
        )
    
    elif request.method == "POST":
        # Implementar as seguintes validações antes de salvar o registro
        # 1. Verificar se o e-mail do usuário já não está salvo na tabela de usuários (auth_user)
        # 2. Verificar se o e-mail informado já não está salvo na tabela de pre registro
        # 3. Verificar se o pre registro ainda é válido
        # 4. Verificar se o pre registro não está expirado

        form = PreRegistroForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            pre_registro = PreRegistro(email=email)

            pre_registro.save()

        return redirect(reverse("registro:pre_registro"))
