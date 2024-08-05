from django import forms
from .models import Lista

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['nome', 'descricao']
