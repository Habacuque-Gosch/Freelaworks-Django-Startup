from django.shortcuts import render, redirect
from apps.usuarios.models import Resumo


def buscar_candidatos(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    resumo = Resumo.objects.filter()

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            resumo = resumo.filter(titulo_profissional__icontains=nome_a_buscar)

    return render(request, 'partials/candidatos.html', {"resumo": resumo})

def filtrar_candidatos(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    resumo = Resumo.objects.filter()
        
    if "tipo" in request.GET:
        key_a_buscar = request.GET['tipo']
        if key_a_buscar:
            resumo = resumo.filter(tipo_de_vaga__icontains=key_a_buscar)

    if "local" in request.GET:
        key_a_buscar = request.GET['local']
        if key_a_buscar:
            resumo = resumo.filter(local__icontains=key_a_buscar)

    return render(request, 'partials/candidatos.html', {"resumo": resumo, "user": user})