from django.urls import path
from apps.empresas.views import login, cadastro, logout, perfil

urlpatterns = [
    path('login-empresa/', login, name = 'login_empresa'),
    path('cadastro-empresa/', cadastro, name = 'cadastro_empresa'),
    path('logout-empresa/', logout, name = 'logout_empresa'),
    path('perfil-empresa/', perfil, name = 'perfil_empresa')
]
