"""
Configuration pytest pour le projet.

Ce fichier configure les fixtures et les paramètres de test pour le projet.
"""

import pytest
from django.contrib.auth.models import User
from django.test import Client


@pytest.fixture
def client():
    """
    Fixture pour le client Django.

    Returns:
        Client: Client Django pour tester les requêtes HTTP
    """
    return Client()


@pytest.fixture
def user(db):
    """
    Fixture pour créer un utilisateur de test.

    Args:
        db: Base de données de test

    Returns:
        User: Utilisateur Django créé pour les tests
    """
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )


@pytest.fixture
def admin_user(db):
    """
    Fixture pour créer un utilisateur administrateur.

    Args:
        db: Base de données de test

    Returns:
        User: Utilisateur administrateur créé pour les tests
    """
    return User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpass123'
    )


@pytest.fixture
def authenticated_client(client, user):
    """
    Fixture pour un client authentifié.

    Args:
        client: Client Django
        user: Utilisateur de test

    Returns:
        Client: Client Django authentifié
    """
    client.login(username='testuser', password='testpass123')
    return client


@pytest.fixture
def admin_client(client, admin_user):
    """
    Fixture pour un client administrateur authentifié.

    Args:
        client: Client Django
        admin_user: Utilisateur administrateur

    Returns:
        Client: Client Django avec les droits admin
    """
    client.login(username='admin', password='adminpass123')
    return client
