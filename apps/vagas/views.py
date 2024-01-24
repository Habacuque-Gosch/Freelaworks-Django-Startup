from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from apps.vagas.models import Vagas
from apps.vagas.forms import VagasForms, VagasFormsSave
from django.contrib import messages
import stripe
from django.conf import settings


def home(request):
    if request.user.is_authenticated:
        vagas = Vagas.objects.order_by("data_publicada").filter(publicada=True)
        return render(request, 'vagas/index.html', {"vagas": vagas})

    return render(request, 'partials/home.html')

def index(request):
    user = request.user
    if not request.user.is_authenticated:
        return redirect('login')
    
    vagas = Vagas.objects.order_by("data_publicada").filter(publicada=True)

    return render(request, 'vagas/index.html', {"vagas": vagas, "user": user})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    vagas = Vagas.objects.order_by("data_publicada").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            vagas = vagas.filter(nome__icontains=nome_a_buscar)

    return render(request, 'vagas/index.html', {"vagas": vagas, "palavra": nome_a_buscar})

def filtrar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    vagas = Vagas.objects.order_by("data_publicada").filter(publicada=True)
        
    if "tipo" in request.GET:
        key_a_buscar = request.GET['tipo']
        if key_a_buscar:
            vagas = vagas.filter(tipo_de_vaga__icontains=key_a_buscar)

    if "local" in request.GET:
        key_a_buscar = request.GET['local']
        if key_a_buscar:
            vagas = vagas.filter(local__icontains=key_a_buscar)

    return render(request, 'vagas/index.html', {"vagas": vagas})


def candidatar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    return render(request, 'vagas/index.html')

def minhas_vagas(request):
    user = request.user
    if not user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('login_empresa')
    try:
        vagas = get_list_or_404(Vagas, usuario=user)
        return render(request, 'vagas/minhas_vagas.html', {"vagas": vagas})
    except:
        return render(request, 'vagas/minhas_vagas.html')

def nova_vaga(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    form = VagasFormsSave
    if request.method == 'POST':
        form = VagasFormsSave(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vaga cadastrada com sucesso")
            return redirect('minhas_vagas')

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
            return redirect('minhas_vagas')

    return render(request, 'vagas/editar_vaga.html', {"form": form, "vaga_id": vaga_id})

def deletar_vaga(request, vaga_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    vagas = Vagas.objects.get(id=vaga_id)
    vagas.delete()
    messages.success(request, "vaga deletada com sucesso")
    return redirect('minhas_vagas')


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