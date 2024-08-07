from django.shortcuts import render, redirect
from .models import Lista
from .forms import ListaForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def create_lista(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            lista = form.save(commit=False)
            lista.usuario = request.user
            lista.save()
            return redirect('nome_da_view_que_lista_as_listas')  
        form = ListaForm()
    return render(request, 'nome_do_template.html', {'form': form})  

@login_required
def lista_listas(request):
    listas = Lista.objects.filter(usuario=request.user)
    return render(request, 'listas/lista_listas.html', {'listas': listas})

@login_required
def edit_lista(request, id):
    lista = get_object_or_404(Lista, id=id, usuario=request.user)
    if request.method == 'POST':
        form = ListaForm(request.POST, instance=lista)
        if form.is_valid():
            form.save()
            return redirect('lista_listas')
    else:
        form = ListaForm(instance=lista)
    return render(request, 'listas/edit_lista.html', {'form': form})

@login_required
def delete_lista(request, id):
    lista = get_object_or_404(Lista, id=id, usuario=request.user)
    if request.method == 'POST':
        lista.delete()
        return redirect('lista_listas')
    return render(request, 'listas/delete_lista.html', {'lista': lista})
