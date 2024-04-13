from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

class PreRegistro(models.Model):
    email = models.EmailField("E-mail", max_length=300)
    token = models.UUIDField(default=uuid4)
    criado_em = models.DateTimeField(auto_now_add=True)
    valido = models.BooleanField(default=True)

    class Meta:
        db_table = "tb_pre_registro"

class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    documento = models.CharField(max_length=20, null=True, blank=True)
    genero = models.CharField(max_length=1, null=True, blank=True)
    data_de_nascimento = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "tb_perfis"