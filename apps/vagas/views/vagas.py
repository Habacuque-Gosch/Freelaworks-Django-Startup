from django.shortcuts import render, redirect
from apps.vagas.models import Vagas
from apps.vagas.forms import VagasForms, VagasFormsSave
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import stripe




# def loader(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     return render(request, 'partials/loader.html')

# def home(request):
#     if request.user.is_authenticated:
#         return redirect('index')

#     return render(request, 'partials/home.html')

def index(request):
    user = request.user
    if not request.user.is_authenticated:
        return redirect('login')
    
    vagas = Vagas.objects.order_by("data_publicada").filter(publicada=True)

    paginator = Paginator(vagas, 20)
    page = request.GET.get('page')
    vagas_por_pagina = paginator.get_page(page)

    return render(request, 'vagas/index.html', {"vagas": vagas_por_pagina, "user": user, "vagas_notificacao": vagas_por_pagina })

def nova_vaga(request):
    current_user = request.user
    if not current_user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    form = VagasFormsSave
    if request.method == 'POST':
        form = VagasFormsSave(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = current_user
            form.save()
            messages.success(request, "Vaga cadastrada com sucesso")
            return redirect('dashboard')
            

    return render(request, 'vagas/nova_vaga.html', {"form": form})

def editar_vaga(request, vaga_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    vagas = Vagas.objects.get(id=vaga_id)
    form = VagasForms(instance=vagas)

    if request.method == 'POST':
        form = VagasForms(request.POST, instance=vagas)
        if form.is_valid():
            form.save()
            messages.success(request, "Vaga editada com sucesso")
            return redirect('dashboard')

    return render(request, 'vagas/editar_vaga.html', {"form": form, "vaga_id": vaga_id})

def deletar_vaga(request, vaga_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    vagas = Vagas.objects.get(id=vaga_id)
    vagas.delete()
    messages.success(request, "vaga deletada com sucesso")
    return redirect('dashboard')

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='partials/home.html',
            cancel_url='partials/home.html',
        )
    except Exception as e:
        return str(e)

    return render(request, 'partials/home.html')