import uuid

from django.db import models

from registro.models import Perfil

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

    def __str__(self) -> str:
        return "{} localizada em {}-{}".format(
            self.descricao,
            self.cidade,
            self.estado
        )
    
    class Meta:
        db_table = "tb_imoveis"


class TipoContrato(models.Model):

    tipo_contrato = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return "{} ({})".format(
            self.tipo_contrato.title(),
            self.descricao
        )

    class Meta:
        db_table = "tb_tipos_contrato"


class Contrato(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    tipo_contrato = models.ForeignKey(
        TipoContrato, null=True, on_delete=models.SET_NULL
    )

    locatario = models.ForeignKey(
        Perfil, null=True, on_delete=models.SET_NULL
    )

    imovel = models.ForeignKey(
        Imovel, null=True, on_delete=models.SET_NULL
    )

    data_de_inicio = models.DateField()
    data_de_fim = models.DateField()
    esta_ativo = models.BooleanField(default=True)
    valor_total = models.FloatField()
    valor_parcela = models.FloatField()
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "tb_contratos"

class InformacaoAluguelTipoContratoImovel(models.Model):
    
    imovel = models.ForeignKey(
        Imovel,
        null=True,
        on_delete=models.SET_NULL
    )
    tipo_contrato = models.ForeignKey(
        TipoContrato,
        null=True,
        on_delete=models.SET_NULL
    )
    valor = models.FloatField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return "Contrato {} para o imóvel '{}'. Valor: R$ {:.2f}".format(
            self.tipo_contrato.tipo_contrato,
            self.imovel,
            self.valor
        )

    class Meta:
        db_table = "informacoes_aluguel_tipo_contrato_imovel"

class Parcelamento(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contrato = models.ForeignKey(
        Contrato,
        null=True,
        on_delete=models.SET_NULL
    )
    numero_parcela = models.IntegerField()
    valor_parcela = models.FloatField()
    data_vencimento = models.DateField()
    paga = models.BooleanField(default=False)
    data_pagamento = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "tb_parcelamentos"