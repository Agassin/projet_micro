"""
Fixtures de données pour les tests.

Ce module contient des fixtures pytest pour les données communes des tests.
"""

import pytest
from django.contrib.auth.models import User
from django.test import Client


@pytest.fixture
def user_data():
    """
    Fixture fournissant des données d'utilisateur pour les tests.

    Returns:
        dict: Dictionnaire contenant les données d'un utilisateur
    """
    return {
        'username': 'fixtureuser',
        'email': 'fixture@example.com',
        'password': 'fixturepass123',
        'first_name': 'Test',
        'last_name': 'User'
    }


@pytest.fixture
def multiple_users(db):
    """
    Fixture créant plusieurs utilisateurs pour les tests.

    Args:
        db: Base de données de test

    Returns:
        list: Liste d'utilisateurs créés
    """
    users = []
    for i in range(3):
        user = User.objects.create_user(
            username=f'user{i}',
            email=f'user{i}@example.com',
            password=f'pass{i}123'
        )
        users.append(user)
    return users


@pytest.fixture
def admin_data():
    """
    Fixture fournissant des données d'administrateur pour les tests.

    Returns:
        dict: Dictionnaire contenant les données d'un administrateur
    """
    return {
        'username': 'adminuser',
        'email': 'admin@example.com',
        'password': 'adminpass123'
    }


@pytest.fixture
def test_client_factory():
    """
    Fixture fournissant une fabrique de clients pour les tests.

    Returns:
        callable: Fonction pour créer des clients de test
    """
    def create_client():
        return Client()
    return create_client


@pytest.fixture(params=['testuser1', 'testuser2', 'testuser3'])
def multiple_usernames(request):
    """
    Fixture paramétrée pour tester avec plusieurs noms d'utilisateurs.

    Args:
        request: Objet de requête pytest

    Returns:
        str: Nom d'utilisateur
    """
    return request.param


@pytest.fixture
def user_with_profile(db):
    """
    Fixture créant un utilisateur avec profil complet.

    Args:
        db: Base de données de test

    Returns:
        User: Utilisateur créé avec profil complet
    """
    user = User.objects.create_user(
        username='profileuser',
        email='profile@example.com',
        password='profilepass123',
        first_name='Jean',
        last_name='Dupont'
    )
    return user


@pytest.fixture
def inactive_user(db):
    """
    Fixture créant un utilisateur inactif.

    Args:
        db: Base de données de test

    Returns:
        User: Utilisateur inactif
    """
    user = User.objects.create_user(
        username='inactiveuser',
        email='inactive@example.com',
        password='inactivepass123',
        is_active=False
    )
    return user
