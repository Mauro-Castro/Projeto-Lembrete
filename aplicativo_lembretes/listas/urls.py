from django.urls import path
from . import views

urlpatterns = [
    path('listas/', views.lista_listas, name='lista_listas'),
    path('listas/create/', views.create_lista, name='create_lista'),
    path('listas/edit/<int:id>/', views.edit_lista, name='edit_lista'),
    path('listas/delete/<int:id>/', views.delete_lista, name='delete_lista'),
]
