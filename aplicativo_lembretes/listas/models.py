from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Lista(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='listas')

    def __str__(self):
        return self.nome