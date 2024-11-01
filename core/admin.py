from django.contrib import admin
from .models import Servico, Cargo, Funcionario


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('icone', 'servico', 'ativo', 'modificado')


@admin.register(Funcionario)
class FucionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')
