from django.contrib import admin
from apps.vagas.models import Vagas

class ListandoVagas(admin.ModelAdmin):
    list_display = ("id", "nome", "tipo_de_vaga", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("tipo_de_vaga", "usuario")
    list_editable = ("publicada",)
    list_per_page = 20

admin.site.register(Vagas, ListandoVagas)