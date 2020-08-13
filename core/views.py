from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.models import Evento


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos}
    return render(request, 'agenda.html', dados)


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário e/ou senha inválidos!")
    return redirect('/')


def login_user(request):
    return render(request, 'login.html')


@login_required(login_url='/login/')
def add_evento(request):
    return render(request, 'add_evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user

        if titulo is "" or data_evento is "":
            messages.error(request, "Título e data não podem estar em branco!")
            return redirect('/')

        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)

        messages.info(request, "Evento '" + titulo + "' criado com sucesso!")

    return redirect('/')
