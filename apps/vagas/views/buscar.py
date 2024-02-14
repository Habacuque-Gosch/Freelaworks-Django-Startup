from django.shortcuts import render, redirect
from apps.vagas.models import Vagas
from django.contrib import messages



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

