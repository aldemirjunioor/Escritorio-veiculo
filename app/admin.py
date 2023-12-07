from django.contrib import admin
from .models import *


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ['num', 'num_escritorio', 'data', 'duracao']
    
@admin.register(Escritorio)
class EscritorioAdmin(admin.ModelAdmin):
    list_display = ['local', 'num_contrato']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['num_hab', 'stado_hab', 'nome_cliente', 'end_cliente', 'tel_cliente']

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['num_veiculo', 'data_prox_manut', 'placa']

@admin.register(TipoVeiculo)
class TipoVeiculoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome_veiculo', 'ar_cond']

@admin.register(Automovel)
class AutomovelAdmin(admin.ModelAdmin):
    list_display = ['num_portas', 'dir_hidraulica', 'cambio_auto']

@admin.register(Onibus)
class OnibusAdmin(admin.ModelAdmin):
    list_display = ['num_passag', 'leito', 'sanitario']

