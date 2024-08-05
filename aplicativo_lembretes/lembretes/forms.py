from django import forms
from .models import Lembrete, Categoria, Anexo

class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = ['titulo', 'descricao', 'data_lembrete', 'prioridade', 'categoria']
        widgets = {
            'listas': forms.CheckboxSelectMultiple(),
            'data_lembrete': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']


class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = ['lembrete', 'arquivo', 'descricao']