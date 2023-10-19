from django.contrib import admin
from base.models import Cadastro

# Register your models here.

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email','data'] #colunas
    search_fields = ['nome','email'] #filtros/buscas
    list_filter = ['data']

    

