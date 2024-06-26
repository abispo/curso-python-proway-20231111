from django.urls import path

from . import views

app_name = "gestao"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "meu-perfil/",
        views.meu_perfil,
        name="meu_perfil"
    ),
    path(
        "nao-autorizado/",
        views.nao_autorizado,
        name="nao_autorizado"
    )
]
