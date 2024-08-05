from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_lembretes')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
