from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

#def index(request):     #Para redirecionar o index para uma pagina
    #return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user   #para visualizar os eventos do usuario logado
    evento = Evento.objects.filter(usuario=usuario)   #para visualizar os eventos do usuario logado
    #evento = Evento.objects.all()  ---- para visualizar os eventos de todos os usuarios
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)