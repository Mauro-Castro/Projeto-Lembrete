from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lembrete, Lista
from .forms import LembreteForm
from django.shortcuts import get_object_or_404
from .models import Categoria
from .forms import CategoriaForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from notificacoes.models import Notificacao
from .models import Anexo
from .forms import AnexoForm
from django.http import HttpResponseBadRequest
import logging

# Create your views here.
def index(request):
    lembretes = Lembrete.objects.all()
    return render(request, 'lembretes/lista_lembretes.html', {'lembretes': lembretes})

@login_required
def edit_lembrete(request, id):
    lembrete = get_object_or_404(Lembrete, id=id)
    listas = Lista.objects.filter(usuario=request.user)
    lembrete_listas_ids = list(lembrete.listas.values_list('id', flat=True))
    
    if request.method == 'POST':
        form = LembreteForm(request.POST, instance=lembrete)
        if form.is_valid():
            lembrete = form.save(commit=False)
            lembrete.user = request.user
            lembrete.save()
            
            listas_ids = request.POST.getlist('listas')
            lembrete.listas.set(listas_ids)
            
            for file in request.FILES.getlist('anexos'):
                Anexo.objects.create(lembrete=lembrete, arquivo=file, descricao=file.name)
            
            return redirect('lista_lembretes')
    else:
        form = LembreteForm(instance=lembrete)
    
    return render(request, 'lembretes/edit_lembrete.html', {
        'form': form,
        'listas': listas,
        'lembrete_listas_ids': lembrete_listas_ids,
        'lembrete': lembrete
    })

@login_required
def delete_lembrete(request, id):
    lembrete = get_object_or_404(Lembrete, id=id, user=request.user)
    if request.method == 'POST':
        lembrete.delete()
        return redirect('lista_lembretes')
    return render(request, 'lembretes/delete_lembrete.html', {'lembrete': lembrete})

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'lembretes/categoria_list.html', {'categorias': categorias})

def create_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'lembretes/create_categoria.html', {'form': form})

def edit_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'lembretes/edit_categoria.html', {'form': form})

def delete_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'lembretes/delete_categoria.html', {'categoria': categoria})

@login_required
def lista_lembretes(request, categoria_id=None):
    lembretes = Lembrete.objects.filter(user=request.user)
    
    if categoria_id:
        lembretes = lembretes.filter(categoria_id=categoria_id)
    
    categorias = Categoria.objects.all()
    
    return render(request, 'lembretes/lista_lembretes.html', {
        'lembretes': lembretes, 
        'categorias': categorias
    })
    
class LembreteListView(LoginRequiredMixin, ListView):
    model = Lembrete
    template_name = 'lembretes/lista_lembretes.html'
    context_object_name = 'lembretes'

    def get_queryset(self):
        return Lembrete.objects.filter(user=self.request.user)

@login_required
def create_lembrete(request):
    if request.method == 'POST':
        form = LembreteForm(request.POST)
        if form.is_valid():
            lembrete = form.save(commit=False)
            lembrete.user = request.user
            lembrete.save()
            
            listas_ids = request.POST.getlist('listas')
            lembrete.listas.set(listas_ids)
            
            for file in request.FILES.getlist('anexos'):
                Anexo.objects.create(lembrete=lembrete, arquivo=file, descricao=file.name)
            
            return redirect('lista_lembretes')
    else:
        form = LembreteForm()
        listas = Lista.objects.filter(usuario=request.user)
    
    return render(request, 'lembretes/create_lembrete.html', {
        'form': form,
        'listas': listas
    })
def lista_notificacoes(request):
    notificacoes = Notificacao.objects.filter(user=request.user)
    return render(request, 'lembretes/notificacoes.html', {'notificacoes': notificacoes})

@login_required
def lista_anexos(request, lembrete_id):
    lembrete = get_object_or_404(Lembrete, id=lembrete_id)
    anexos = Anexo.objects.filter(lembrete=lembrete)
    return render(request, 'anexos/lista_anexos.html', {'anexos': anexos, 'lembrete': lembrete})


logger = logging.getLogger(__name__)

@login_required
def create_anexo(request, lembrete_id):
    lembrete = get_object_or_404(Lembrete, id=lembrete_id)

    if request.method == 'POST':
        form = AnexoForm(request.POST, request.FILES)
        if form.is_valid():
            anexo = form.save(commit=False)
            anexo.lembrete = lembrete
            anexo.save()
            return redirect('lista_anexos', lembrete_id=lembrete.id)
        else:
            print("Form Errors:", form.errors)
    else:
        form = AnexoForm()

    return render(request, 'anexos/create_anexo.html', {'form': form, 'lembrete': lembrete})


def delete_anexo(request, pk):
    anexo = get_object_or_404(Anexo, pk=pk)
    if request.method == 'POST':
        lembrete_id = anexo.lembrete.id
        anexo.delete()
        return redirect('lista_anexos', lembrete_id=lembrete_id)
    return render(request, 'anexos/delete_anexo.html', {'anexo': anexo})

logger = logging.getLogger(__name__)

@login_required
def edit_anexo(request, pk):
    logger.debug(f"Received pk: {pk}")
    anexo = get_object_or_404(Anexo, pk=pk)

    if request.method == 'POST':
        form = AnexoForm(request.POST, request.FILES, instance=anexo)
        if form.is_valid():
            form.save()
            return redirect('lista_anexos', lembrete_id=anexo.lembrete.id)
    else:
        form = AnexoForm(instance=anexo)

    return render(request, 'anexos/edit_anexo.html', {'form': form, 'anexo': anexo})