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

        form = PreRegistroForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            pre_registro = PreRegistro(email=email)

            pre_registro.save()

        return redirect(reverse("registro:pre_registro"))
