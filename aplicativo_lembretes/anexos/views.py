from django.shortcuts import render, get_object_or_404, redirect
from .models import Anexo
from .forms import AnexoForm
from django.contrib.auth.decorators import login_required
from lembretes.models import Lembrete

# Create your views here.
@login_required
def lista_anexos(request, lembrete_id):
    lembrete = get_object_or_404(Lembrete, id=lembrete_id)
    anexos = lembrete.anexos.all()
    return render(request, 'anexos/lista_anexos.html', {'lembrete': lembrete, 'anexos': anexos})

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
        form = AnexoForm()
    return render(request, 'anexos/create_anexo.html', {'form': form, 'lembrete': lembrete})

@login_required
def edit_anexo(request, id):
    anexo = get_object_or_404(Anexo, id=id)
    if request.method == 'POST':
        form = AnexoForm(request.POST, request.FILES, instance=anexo)
        if form.is_valid():
            form.save()
            return redirect('lista_anexos', lembrete_id=anexo.lembrete.id)
    else:
        form = AnexoForm(instance=anexo)
    return render(request, 'anexos/edit_anexo.html', {'form': form, 'anexo': anexo})

@login_required
def delete_anexo(request, id):
    anexo = get_object_or_404(Anexo, id=id)
    lembrete_id = anexo.lembrete_id
    if request.method == 'POST':
        anexo.delete()
        return redirect('lista_anexos', lembrete_id=lembrete_id)
    return render(request, 'anexos/delete_anexo.html', {'anexo': anexo})