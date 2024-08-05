from django.shortcuts import render, get_object_or_404, redirect
from .models import Notificacao

# Create your views here.
def lista_notificacoes(request):
    notificacoes = Notificacao.objects.filter(user=request.user).order_by('data_notificacao')
    return render(request, 'notificacoes/lista_notificacoes.html', {'notificacoes': notificacoes})

def marcar_como_lida(request, notificacao_id):
    notificacao = get_object_or_404(Notificacao, id=notificacao_id, user=request.user)
    notificacao.lida = True
    notificacao.save()
    return redirect('lista_notificacoes')
