from django.conf import settings
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone

from registro.forms import PreRegistroForm
from registro.models import PreRegistro
from registro.utils import enviar_email
from registro.validadores import (
    senhas_sao_iguais,
    todos_dados_preenchidos,
    username_nao_existe
)

def pre_registro(request: HttpRequest):

    if request.method == "GET":
        form = PreRegistroForm()

        return render(
            request,
            "registro/pre_registro.html",
            {"form": form}
        )

    elif request.method == "POST":
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

def registro(request: HttpRequest):

    try:
        if request.method == "GET":
            # Verificação no cadastro
            # 1. Verificar se o pre registro ainda é válido
                # 1.1 O código foi encontrado e a coluna valido é True

            token = request.GET.get("id")

            pre_registro_valido = PreRegistro.objects.filter(
                token=token, valido=True
            ).first()

            if not pre_registro_valido:
                return redirect(reverse("registro:pre_registro_invalido"))
            
            data_pre_registro = pre_registro_valido.criado_em

            pre_registro_expirado = (timezone.now() - data_pre_registro).total_seconds() > settings.TEMPO_LIMITE_PRE_REGISTRO

            if pre_registro_expirado:
                pre_registro_valido.valido = False
                pre_registro_valido.save()

                return redirect(reverse("registro:pre_registro_expirado"))
            
            return render(
                request,
                "registro/registro.html",
                {"pre_registro": pre_registro_valido}
            )
        elif request.method == "POST":

            nome = request.POST.get("nome")
            sobrenome = request.POST.get("sobrenome")
            nome_de_usuario = request.POST.get("nome_de_usuario")
            senha = request.POST.get("senha")
            confirmacao_senha = request.POST.get("confirmacao_senha")

            id_pre_registro = request.POST.get("id_pre_registro")
            email = request.POST.get("email")

            erros = []

            if not todos_dados_preenchidos(
                nome, sobrenome, nome_de_usuario, senha, confirmacao_senha
            ):
                erros.append("Você deve preencher todos os campos no formulário.")

            if not username_nao_existe(nome_de_usuario):
                erros.append(f"O nome de usuário '{nome_de_usuario}' já existe! Escolha outro.")

            if not senhas_sao_iguais(senha, confirmacao_senha):
                erros.append("O valor do campo 'Senha' é diferente do valor do campo 'Confirmação da Senha.")

            if erros:
                return render(
                    request,
                    "registro/registro.html",
                    {"erros": erros}
                )
            
            User.objects.create_user(
                first_name=nome,
                last_name=sobrenome,
                username=nome_de_usuario,
                email=email,
                password=senha
            )

            pre_registro = PreRegistro.objects.get(token=id_pre_registro)
            pre_registro.valido = False
            pre_registro.save()

            return redirect(reverse("registro:confirmacao_cadastro"))

    except ValidationError:
        return redirect(reverse("registro:pre_registro_invalido"))
    
def pre_registro_invalido(request: HttpRequest):
    return render(
        request,
        "registro/pre_registro_invalido.html"
    )

def pre_registro_expirado(request: HttpRequest):
    return render(
        request,
        "registro/pre_registro_expirado.html"
    )

def confirmacao_cadastro(request: HttpRequest):
    return render(
        request,
        "registro/confirmacao_cadastro.html"
    )