"""Vues de l'application core.

Ce module contient toutes les vues principales de l'application Django.
"""

from django.shortcuts import render


def home(request):
    """Affiche la page d'accueil de l'application.

    Args:
        request: Objet HttpRequest

    Returns:
        HttpResponse: Page d'accueil rendue
    """
    return render(request, 'index.html')


def login_view(request):
    """Affiche la page de connexion.

    Args:
        request: Objet HttpRequest

    Returns:
        HttpResponse: Page de connexion rendue
    """
    return render(request, 'login.html')


def dashboard(request):
    """Affiche le tableau de bord de l'application.

    Args:
        request: Objet HttpRequest

    Returns:
        HttpResponse: Tableau de bord rendu
    """
    return render(request, 'dashboard.html')


def eleve(request):
    """Affiche la page des élèves.

    Args:
        request: Objet HttpRequest

    Returns:
        HttpResponse: Page des élèves rendue
    """
    return render(request, 'eleve.html')
