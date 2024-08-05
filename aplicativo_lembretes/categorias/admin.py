from django.contrib import admin
from django.contrib.auth.models import User
from .models import Categoria
# Register your models here.
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user',)

def save_user_profile(sender, instance, **kwargs):
    from .models import Perfil  
    if not hasattr(instance, 'perfil'):
        Perfil.objects.create(user=instance)          

admin.site.register(Categoria)