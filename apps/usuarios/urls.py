from django.urls import path
from apps.usuarios.views import login, cadastro, logout, perfil, upload_curriculo


urlpatterns = [
    path('login/', login, name = 'login'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('logout/', logout, name = 'logout'),
    path('perfil/', perfil, name = 'perfil'),
    path('upload-curriculo/', upload_curriculo, name = 'upload_curriculo')
]
