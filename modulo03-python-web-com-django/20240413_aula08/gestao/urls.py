from django.urls import path

from . import views

app_name = "gestao"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "inquilinos/<int:id_do_usuario>/perfil/",
        views.perfil_inquilino,
        name="perfil_inquilino"
    )
]
