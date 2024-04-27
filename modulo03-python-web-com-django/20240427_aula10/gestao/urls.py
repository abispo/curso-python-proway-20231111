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
    ),
    path(
        "alugar-imovel/",
        views.lista_imoveis,
        name="lista_imoveis"
    ),
    path(
        "imoveis/<imovel_id>/",
        views.detalhe_imovel,
        name="detalhe_imovel"
    ),
    path(
        "imoveis/<imovel_id>/alugar/",
        views.alugar_imovel,
        name="alugar_imovel"
    )
]
