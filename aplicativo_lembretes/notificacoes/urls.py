from django.urls import path
from . import views

urlpatterns = [
    path('notificacoes/', views.lista_notificacoes, name='lista_notificacoes'),
    path('notificacoes/lida/<int:notificacao_id>/', views.marcar_como_lida, name='marcar_como_lida'),
]
