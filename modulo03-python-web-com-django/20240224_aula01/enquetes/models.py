from django.db import models


class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    data_de_publicacao = models.DateTimeField("Data de publicação")

    class Meta:
        db_table = "tb_perguntas"


class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)

    class Meta:
        db_table = "tb_opcoes"