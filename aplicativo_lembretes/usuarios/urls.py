from django.urls import path
from .views import views

urlpatterns = [
    path('register/', views.register, name='register'),
]
