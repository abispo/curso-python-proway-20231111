from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from registro.forms import PreRegistroForm
from registro.models import PreRegistro
from registro.utils import enviar_email

def pre_registro(request: HttpRequest):

    if request.method == "GET":
        form = PreRegistroForm()

        return render(
            request,
            "registro/pre_registro.html",
            {"form": form}
        )

    elif request.method == "POST":
        # Verificação no cadastro
        # 1. Verificar se o pre registro ainda é válido
        # 2. Verificar se o pre registro não está expirado

        form = PreRegistroForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]

            # Implementar as seguintes validações antes de salvar o registro
            # 1. Verificar se o e-mail do usuário já não está salvo na tabela de usuários (auth_user)
            email_ja_cadastrado = User.objects.filter(email=email)
        
            # 2. Verificar se o e-mail informado já não está salvo na tabela de pre registro
            # e ainda é válido
            email_existe_no_pre_registro = PreRegistro.objects.filter(
                email=email, valido=True
            )

            if email_ja_cadastrado or email_existe_no_pre_registro:
                form.add_error(
                    None, "O e-mail informado não é válido. Verifique se já possui cadastro ou se ainda não confirmou um pré-registro anterior."
                )

                return render(
                    request,
                    "registro/pre_registro.html",
                    {"form": form}
                )

            pre_registro = PreRegistro(email=email)
            pre_registro.save()

            enviar_email(request, pre_registro)

            return redirect("registro:envio_email_pre_registro")

        return redirect(reverse("registro:pre_registro"))
    

def envio_email_pre_registro(request):
    return render(
        request,
        "registro/envio_email_pre_registro.html"
    )

def registro(request):
    return render(
        request,
        "registro/registro.html"
    )