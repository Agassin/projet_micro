# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home_view(request):
    """Vue pour la page d'accueil"""
    return render(request, 'home.html')

def about_view(request):
    """Vue pour la page À propos"""
    return render(request, 'about.html')

def login_view(request):
    """Vue personnalisée pour la connexion"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenue {username}!')
            return redirect('profile')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    
    return render(request, 'auth/login.html')

def register_view(request):
    """Vue pour l'inscription"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Compte créé avec succès!')
            return redirect('profile')
        else:
            # Afficher les erreurs du formulaire
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/register.html', {'form': form})

@login_required
def profile_view(request):
    """Vue pour la page profil (nécessite une connexion)"""
    return render(request, 'auth/profile.html', {'user': request.user})