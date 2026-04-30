"""
Tests de factories pour la création de données de test.

Ce module contient des factories pour simplifier la création de données de test.
"""

import pytest
from django.contrib.auth.models import User


class UserFactory:
    """Factory pour créer des utilisateurs de test."""

    @staticmethod
    def create(username='testuser', email='test@example.com',
               password='testpass123', **kwargs):
        """
        Crée un utilisateur avec les paramètres donnés.

        Args:
            username (str): Nom d'utilisateur
            email (str): Email de l'utilisateur
            password (str): Mot de passe de l'utilisateur
            **kwargs: Paramètres supplémentaires

        Returns:
            User: Utilisateur créé
        """
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            **kwargs
        )
        return user

    @staticmethod
    def create_superuser(username='admin',
                         email='admin@example.com',
                         password='adminpass123', **kwargs):
        """
        Crée un superutilisateur.

        Args:
            username (str): Nom d'utilisateur
            email (str): Email de l'utilisateur
            password (str): Mot de passe de l'utilisateur
            **kwargs: Paramètres supplémentaires

        Returns:
            User: Superutilisateur créé
        """
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            **kwargs
        )
        return user

    @staticmethod
    def create_batch(count=5, **kwargs):
        """
        Crée plusieurs utilisateurs.

        Args:
            count (int): Nombre d'utilisateurs à créer
            **kwargs: Paramètres supplémentaires

        Returns:
            list: Liste d'utilisateurs créés
        """
        users = []
        for i in range(count):
            username = f"user{i}" if 'username' not in kwargs else kwargs['username']
            email = f"user{i}@example.com" if 'email' not in kwargs else kwargs['email']
            user = UserFactory.create(
                username=username,
                email=email,
                **{k: v for k, v in kwargs.items() if k not in ['username', 'email']}
            )
            users.append(user)
        return users


@pytest.mark.django_db
class TestUserFactory:
    """Tests pour la UserFactory."""

    def test_create_single_user(self):
        """Teste la création d'un utilisateur unique."""
        user = UserFactory.create()
        assert user.username == 'testuser'
        assert user.email == 'test@example.com'

    def test_create_user_with_custom_data(self):
        """Teste la création d'un utilisateur avec données personnalisées."""
        user = UserFactory.create(
            username='customuser',
            email='custom@example.com'
        )
        assert user.username == 'customuser'
        assert user.email == 'custom@example.com'

    def test_create_superuser(self):
        """Teste la création d'un superutilisateur."""
        admin = UserFactory.create_superuser()
        assert admin.is_superuser
        assert admin.is_staff

    def test_create_batch_of_users(self):
        """Teste la création d'un lot d'utilisateurs."""
        users = UserFactory.create_batch(5)
        assert len(users) == 5
        assert User.objects.count() == 5

    def test_factory_users_are_distinct(self):
        """Teste que les utilisateurs créés sont distincts."""
        users = UserFactory.create_batch(3)
        usernames = [u.username for u in users]
        assert len(set(usernames)) == 3
