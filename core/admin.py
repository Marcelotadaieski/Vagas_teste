from django.contrib import admin
from .models import Vaga, Candidato   

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display      = ('titulo', 'setor', 'status', 'data_criacao')
    list_filter       = ('status', 'setor')
    search_fields     = ('titulo',)

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display      = ('nome', 'email', 'idade')
    search_fields     = ('nome', 'email')
    filter_horizontal = ('vagas',)
    readonly_fields   = ('idade',)
