from django.urls import path
from .views import *


urlpatterns = [
    path('', loader, name = 'loader'),
    path('home/', home, name = 'home'),
    path('index/', index, name = 'index'),
    path("buscar", buscar, name="buscar"),
    path("filtrar", filtrar, name="filtrar"),
    path("nova-vaga", nova_vaga, name="nova_vaga"),
    path("editar-vaga/<int:vaga_id>", editar_vaga, name="editar_vaga"),
    path("deletar-vaga/<int:vaga_id>", deletar_vaga, name="deletar_vaga"),
]
