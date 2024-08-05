from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lembrete
from notificacoes.models import Notificacao
from django.utils import timezone

@receiver(post_save, sender=Lembrete)
def criar_notificacao(sender, instance, created, **kwargs):
    if created and instance.user:
        Notificacao.objects.create(
            lembrete=instance,
            mensagem="Novo lembrete criado",
            data_notificacao=timezone.now(),
            user=instance.user
        )
