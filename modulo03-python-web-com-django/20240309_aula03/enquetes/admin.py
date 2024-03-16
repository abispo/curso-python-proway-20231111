from django.contrib import admin

from enquetes.models import Pergunta, Opcao, OpiniaoPergunta

admin.site.register(Pergunta)
admin.site.register(Opcao)
admin.site.register(OpiniaoPergunta)