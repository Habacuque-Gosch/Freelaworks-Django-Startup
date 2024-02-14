from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from apps.vagas.models import Vagas
from django.contrib import auth, messages
from apps.empresas.forms import LoginForms, CadastroForms



def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha_login"].value()
                
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                # messages.success(request, f"{nome} logado com sucesso")
                return redirect('candidatos')
            else:
                messages.error(request, "usuário ou senha inválido")
                return redirect('login_empresa')

    return render(request, 'empresas/login_empresas.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha_cadastro"].value() != form["senha_confirma"].value():
                messages.error(request, "senhas não são iguais")
                return redirect('cadastro_empresa')

            nome = form["nome_cadastro"].value()
            # numero_funcionarios = form["numero_funcionarios"].value()
            # telefone = form["telefone"].value()
            email = form["email"].value()
            senha = form["senha_cadastro"].value()

        if  User.objects.filter(username=nome).exists():
            messages.error(request, "Usuário já existente")
            return redirect('cadastro_empresa')
        
        usuario =  User.objects.create_user(
            username=nome,
            email=email,
            password=senha,
        )
        usuario.save()
        return redirect('login_empresa')

    return render(request, 'empresas/cadastro_empresas.html', {"form": form})

def logout(request):
    # messages.success(request, "Logout efetuado com sucesso")
    auth.logout(request)
    return redirect('login_empresa')

def perfil(request, user):
    if not request.user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('login_empresa')
    
    user = request.user

    return render(request, 'empresas/perfil_empresas.html', {"user": user})

def dashboard(request):
    user = request.user
    if not user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('login_empresa')
    try:
        vagas = get_list_or_404(Vagas, usuario=user)
        return render(request, 'empresas/dashboard.html', {"vagas": vagas})
    except:
        return render(request, 'empresas/dashboard.html')
# def novo_resumo(request):
#     user = request.user
#     if not user.is_authenticated:
#         messages.error(request, "Usuário não logado")
#         return redirect('login')

#     form = ResumoForms()
#     if request.method == 'POST':
#         form = ResumoForms(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Perfil salvo com sucesso")
#             return redirect('perfil', user)
        
#     return render(request, 'usuarios/novo_resumo.html', {"form": form})

# def editar_perfil(request, resumo_id):
#     user = request.user
#     if not user.is_authenticated:
#         messages.error(request, "Usuário não logado")
#         return redirect('login')
    
#     resumo = Resumo.objects.get(id=resumo_id)
#     form = ResumoForms(instance=resumo)

#     if request.method == 'POST':
#         form = ResumoForms(request.POST, instance=resumo)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Resumo editado com sucesso")
#             return redirect('perfil', user)

#     return render(request, 'usuarios/editar_resumo.html', {"form": form, "resumo_id": resumo_id})



