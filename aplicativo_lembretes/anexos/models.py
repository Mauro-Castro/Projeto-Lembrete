from django.db import models
from lembretes.models import Lembrete
# Create your models here.
class Anexo(models.Model):
    lembrete = models.ForeignKey(Lembrete, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='anexos/')
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao