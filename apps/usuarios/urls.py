from django.urls import path
from .views import *
from django.views.generic import TemplateView



urlpatterns = [
    path('login/', login, name = 'login'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('logout/', logout, name = 'logout'),
    path('perfil/<str:user>', perfil, name = 'perfil'),
    path('novo-resumo', novo_resumo, name = 'novo_resumo'),
    path("editar-perfil/<int:resumo_id>QKJBN?", editar_perfil, name="editar_perfil"),
    # path('upload-curriculo/', upload_curriculo, name = 'upload_curriculo')
    path("candidatar/<int:vaga_id>", candidatar, name="candidatar"),
    path('candidatos', candidatos, name = 'candidatos'),
    path('buscar-candidatos', buscar_candidatos, name = 'buscar_candidatos'),
    path('filtrar-candidatos', filtrar_candidatos, name = 'filtrar_candidatos'),
    # path('notificacao', notificacao, name = 'notificacao'),
]
