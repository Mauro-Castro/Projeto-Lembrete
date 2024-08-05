from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from prioridades.models import Prioridade
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Lembrete(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_lembrete = models.DateTimeField()
    prioridade = models.CharField(max_length=50)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)