from django.shortcuts import render, redirect, get_list_or_404
from apps.usuarios.models import Resumo
from apps.vagas.models import Vagas
from django.contrib.auth.models import User
from django.contrib import auth, messages
from apps.usuarios.forms import LoginForms, CadastroForms, ResumoForms, ResumoFormsSave



def login(request):
    ''' Realiza o login do usuario na aplicação '''
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
                return redirect('index')
            else:
                messages.error(request, "usuário ou senha inválido")
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    ''' Realiza o cadastro de um novo usuario no sistema '''
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha_cadastro"].value() != form["senha_confirma"].value():
                messages.error(request, "senhas não são iguais")
                return redirect('cadastro')

            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_cadastro"].value()
        if  User.objects.filter(username=nome).exists():
            messages.error(request, "Usuário já existente")
            return redirect('cadastro')
        
        usuario =  User.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )
        usuario.save()
        # messages.success(request, "Cadastro efetuado com sucesso")
        return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    ''' Realiza o logout do usuario na aplicação '''
    # messages.success(request, "Logout efetuado com sucesso")
    auth.logout(request)
    return redirect('login')

def perfil(request, user):
    user = request.user
    if not user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('login')
    try:
        resumo = get_list_or_404(Resumo, usuario_edit=user)
    except:
        return render(request, 'usuarios/perfil.html')
    
    return render(request, 'usuarios/perfil.html', {"resumo": resumo, "user": user})

def novo_resumo(request):
    user = request.user
    if not user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')

    form = ResumoForms()
    if request.method == 'POST':
        form = ResumoForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil salvo com sucesso")
            return redirect('perfil', user)
        
    return render(request, 'usuarios/novo_resumo.html', {"form": form})

def editar_perfil(request, resumo_id):
    user = request.user
    if not user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    resumo = Resumo.objects.get(id=resumo_id)
    form = ResumoFormsSave(instance=resumo)

    if request.method == 'POST':
        form = ResumoFormsSave(request.POST, instance=resumo)
        if form.is_valid():
            form.save()
            messages.success(request, "Resumo editado com sucesso")
            return redirect('perfil', user)

    return render(request, 'usuarios/editar_resumo.html', {"form": form, "resumo_id": resumo_id})

def candidatar(request, vaga_id):
    user = request.user
    try:
        candidato = get_list_or_404(Resumo, usuario_edit=user)
    except:
        messages.error(request, "Preencha seu perfil")
        return redirect('perfil', user)

    if not user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    try:
        vagas = get_list_or_404(Vagas, pk=vaga_id)
    except:
        return render(request, 'vagas/vaga.html', {"vagas": vagas})
    
    return render(request, 'vagas/vaga.html', {"vagas": vagas, "candidato": candidato})

# def notificacao(request):
    # user = request.user
    # if not user.is_authenticated:
    #     return redirect('login')
    
    # vagas = Vagas.objects.order_by("data_publicada").filter(publicada=True)

    # return render(request, 'partials/notificacao.html', {"vagas": vagas, "user": user})

# def upload_curriculo(request): 
#     form = CurriculoForms
#     if request.method == 'POST':
#         form = CurriculoForms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, "Nova fotografia cadastrada")

#     return render(request, 'usuarios/upload_curriculo.html', {"form": form})
