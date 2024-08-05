from django.urls import path
from . import views

urlpatterns = [
    path('lembrete/<int:lembrete_id>/', views.lista_anexos, name='lista_anexos'),
    path('lembrete/<int:lembrete_id>/create/', views.create_anexo, name='create_anexo'),
    path('edit/<int:id>/', views.edit_anexo, name='edit_anexo'),
    path('delete/<int:id>/', views.delete_anexo, name='delete_anexo'),
]
