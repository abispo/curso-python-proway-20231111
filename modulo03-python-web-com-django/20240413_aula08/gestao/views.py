from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return render(
        request,
        "gestao/index.html"
    )

def perfil_inquilino(request: HttpRequest, id_do_usuario: int):

    if request.method == "GET":
        return render(
            request, "inquilinos/perfil_inquilino.html"
        )
