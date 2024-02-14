from django.urls import path
from apps.empresas.views import login, cadastro, logout, perfil, dashboard

urlpatterns = [
    path('login-empresa/', login, name = 'login_empresa'),
    path('cadastro-empresa/', cadastro, name = 'cadastro_empresa'),
    path('logout-empresa/', logout, name = 'logout_empresa'),
    path('perfil-empresa/<str:user>', perfil, name = 'perfil_empresa'),
    path("dashboard", dashboard, name="dashboard"),
    
    # path('novo-resumo-empresa', novo_resumo, name = 'novo_resumo'),
    # path("editar-perfil-empresa/<int:resumo_id>", editar_perfil, name="editar_perfil"),
]
