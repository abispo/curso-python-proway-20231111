from django.contrib.auth.models import User, AnonymousUser
from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    data_de_publicacao = models.DateTimeField("Data de publicação")

    def __str__(self):
        return self.texto

    class Meta:
        db_table = "tb_perguntas"


class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.texto} ({self.pergunta.texto})"

    class Meta:
        db_table = "tb_opcoes"


class OpiniaoPergunta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nota = models.IntegerField()
    comentario = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pergunta.texto} ({self.nota})"
    
    class Meta:
        db_table = "tb_opinioes_perguntas"