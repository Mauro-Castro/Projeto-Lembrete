from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from lembretes.models import Lembrete

# Create your models here.
class Notificacao(models.Model):
    lembrete = models.ForeignKey(Lembrete, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=255)
    data_notificacao = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.mensagem
    
def criar_notificacao(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Notificacao.objects.create(
            lembrete=instance,
            mensagem="Novo lembrete criado",
            user=instance.user  
        )