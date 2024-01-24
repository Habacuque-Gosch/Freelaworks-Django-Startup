from django.urls import path
from apps.vagas.views import \
    home, index, buscar, filtrar, candidatar, minhas_vagas, nova_vaga, editar_vaga, deletar_vaga


urlpatterns = [
    path('', home, name = 'home'),
    path('index/', index, name = 'index'),
    path("buscar", buscar, name="buscar"),
    path("filtrar", filtrar, name="filtrar"),
    path("candidatar", candidatar, name="candidatar"),
    path("minhas-vagas", minhas_vagas, name="minhas_vagas"),
    path("nova-vaga", nova_vaga, name="nova_vaga"),
    path("editar-vaga/<int:vaga_id>", editar_vaga, name="editar_vaga"),
    path("deletar-vaga/<int:vaga_id>", deletar_vaga, name="deletar_vaga"),
]
