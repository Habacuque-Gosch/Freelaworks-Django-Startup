from django.contrib import admin
from apps.usuarios.models import Resumo

class ListandoResumos(admin.ModelAdmin):
    list_display = ("id", "nome_completo", "titulo_profissional")
    list_display_links = ("id", "nome_completo")
    search_fields = ("nome_completo",)
    list_filter = ("titulo_profissional", "usuario_edit")
    list_per_page = 20

admin.site.register(Resumo, ListandoResumos)
