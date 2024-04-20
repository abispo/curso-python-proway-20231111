import uuid

from django.db import models

class Imovel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    tipo_logradouro = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    descricao = models.TextField(null=True, blank=True)
    disponivel = models.BooleanField(default=True)
    
    class Meta:
        db_table = "tb_imoveis"


class TipoContrato(models.Model):

    tipo_contrato = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "tb_tipos_contrato"