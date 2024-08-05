from django.db import models
from prioridades.models import Prioridade
from categorias.models import Categoria
from django.contrib.auth.models import User

class Lembrete(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_lembrete = models.DateTimeField()
    prioridade = models.IntegerField(choices=[(1, 'Alta'), (2, 'Média'), (3, 'Baixa')])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='lembretes', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listas = models.ManyToManyField('Lista', blank=True)

    def __str__(self):
        return self.titulo

class Lista(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Anexo(models.Model):
    arquivo = models.FileField(upload_to='anexos/')
    descricao = models.TextField(blank=True, null=True)
    lembrete = models.ForeignKey('Lembrete', related_name='anexos', on_delete=models.CASCADE)