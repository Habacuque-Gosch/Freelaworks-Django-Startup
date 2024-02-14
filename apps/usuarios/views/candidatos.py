from django.shortcuts import render, redirect, get_list_or_404
from apps.usuarios.models import Resumo
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def candidatos(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    resumo = Resumo.objects.filter()

    paginator = Paginator(resumo, 20)
    page = request.GET.get('page')
    resumo_por_pagina = paginator.get_page(page)
    
    return render(request, 'partials/candidatos.html', {"resumo": resumo_por_pagina, "user": user})