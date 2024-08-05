from django.db import models

# Create your models here.
class Prioridade(models.Model):
    nome = models.CharField(max_length=255)
    nivel = models.IntegerField()