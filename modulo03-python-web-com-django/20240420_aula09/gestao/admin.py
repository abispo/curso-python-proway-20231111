from django.contrib import admin

from gestao.models import (
    Imovel, TipoContrato, Contrato, InformacaoAluguelTipoContratoImovel
)

admin.site.register(Imovel)
admin.site.register(TipoContrato)
admin.site.register(Contrato)
admin.site.register(InformacaoAluguelTipoContratoImovel)
