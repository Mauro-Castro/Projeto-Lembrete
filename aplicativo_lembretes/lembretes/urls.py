from django.urls import path
from . import views
from .views import LembreteListView

urlpatterns = [
    path('', views.index, name='index'),
    path('lembretes/', views.LembreteListView.as_view(), name='lista_lembretes'),
    path('lembretes/create/', views.create_lembrete, name='create_lembrete'),
    path('lembretes/edit/<int:id>/', views.edit_lembrete, name='edit_lembrete'),
    path('lembretes/delete/<int:id>/', views.delete_lembrete, name='delete_lembrete'),
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/create/', views.create_categoria, name='create_categoria'),
    path('categorias/edit/<int:id>/', views.edit_categoria, name='edit_categoria'),
    path('categorias/delete/<int:id>/', views.delete_categoria, name='delete_categoria'),
    path('anexos/create/<int:lembrete_id>/', views.create_anexo, name='create_anexo'),
    path('anexos/edit/<int:pk>/', views.edit_anexo, name='edit_anexo'),
    path('anexos/delete/<int:pk>/', views.delete_anexo, name='delete_anexo'),
    path('lembretes/<int:lembrete_id>/anexos/', views.lista_anexos, name='lista_anexos'),
]
