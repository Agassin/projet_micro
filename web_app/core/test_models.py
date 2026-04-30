"""
Tests unitaires pour les modèles de l'application.

Ce module contient les tests pour les modèles Django.
"""

import pytest
from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTestCase(TestCase):
    """Tests pour le modèle User."""

    def setUp(self):
        """Configuration avant chaque test."""
        pass

    def test_create_user_successfully(self):
        """Teste la création réussie d'un utilisateur."""
        user = User.objects.create_user(
            username='testuser1',
            email='testuser1@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser1')
        self.assertEqual(user.email, 'testuser1@example.com')
        self.assertTrue(user.check_password('testpass123'))

    def test_user_password_is_hashed(self):
        """Vérifie que le mot de passe est bien haché."""
        user = User.objects.create_user(
            username='hashuser',
            password='plainpassword'
        )
        self.assertNotEqual(user.password, 'plainpassword')
        self.assertTrue(user.check_password('plainpassword'))

    def test_user_authentication_with_correct_password(self):
        """Teste l'authentification avec le bon mot de passe."""
        user = User.objects.create_user(
            username='authuser',
            password='correctpass123'
        )
        self.assertTrue(user.check_password('correctpass123'))

    def test_user_authentication_with_wrong_password(self):
        """Teste l'authentification avec un mauvais mot de passe."""
        user = User.objects.create_user(
            username='authuser2',
            password='correctpass123'
        )
        self.assertFalse(user.check_password('wrongpass123'))

    def test_user_string_representation(self):
        """Teste la représentation en chaîne de l'utilisateur."""
        user = User.objects.create_user(username='stringuser')
        self.assertEqual(str(user), 'stringuser')

    def test_user_email_is_optional(self):
        """Teste que l'email est optionnel."""
        user = User.objects.create_user(
            username='noemailuser',
            password='pass123'
        )
        self.assertEqual(user.email, '')

    def test_user_email_can_be_updated(self):
        """Teste que l'email peut être modifié."""
        user = User.objects.create_user(
            username='emailupdate',
            email='old@example.com',
            password='pass123'
        )
        user.email = 'new@example.com'
        user.save()
        updated_user = User.objects.get(username='emailupdate')
        self.assertEqual(updated_user.email, 'new@example.com')

    def test_user_is_active_by_default(self):
        """Vérifie que les utilisateurs sont actifs par défaut."""
        user = User.objects.create_user(
            username='activeuser',
            password='pass123'
        )
        self.assertTrue(user.is_active)

    def test_user_is_not_staff_by_default(self):
        """Vérifie que les utilisateurs ne sont pas staff par défaut."""
        user = User.objects.create_user(
            username='nonstaffuser',
            password='pass123'
        )
        self.assertFalse(user.is_staff)

    def test_user_is_not_superuser_by_default(self):
        """Vérifie que les utilisateurs ne sont pas superuser par défaut."""
        user = User.objects.create_user(
            username='nonsuperuser',
            password='pass123'
        )
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Teste la création d'un superuser."""
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_user_queryset_count(self):
        """Teste le comptage des utilisateurs."""
        User.objects.create_user(username='user1', password='pass1')
        User.objects.create_user(username='user2', password='pass2')
        User.objects.create_user(username='user3', password='pass3')

        count = User.objects.count()
        self.assertEqual(count, 3)

    def test_user_filtering(self):
        """Teste le filtrage des utilisateurs."""
        User.objects.create_user(
            username='filteruser',
            email='filter@example.com',
            password='pass123'
        )
        user = User.objects.get(username='filteruser')
        self.assertEqual(user.email, 'filter@example.com')


@pytest.mark.django_db
class PytestUserModelTests:
    """Tests des modèles avec pytest."""

    def test_create_user_with_pytest(self):
        """Teste la création d'un utilisateur avec pytest."""
        user = User.objects.create_user(
            username='pytestuser',
            email='pytest@example.com',
            password='pytestpass123'
        )
        assert user.username == 'pytestuser'
        assert user.email == 'pytest@example.com'
        assert user.check_password('pytestpass123')

    def test_user_count_with_pytest(self):
        """Teste le comptage avec pytest."""
        User.objects.create_user(username='user1', password='pass1')
        User.objects.create_user(username='user2', password='pass2')

        count = User.objects.count()
        assert count == 2

    def test_superuser_creation_with_pytest(self):
        """Teste la création de superuser avec pytest."""
        admin = User.objects.create_superuser(
            username='pytestadmin',
            email='pytestadmin@example.com',
            password='adminpass123'
        )
        assert admin.is_staff
        assert admin.is_superuser

    def test_user_retrieval_with_pytest(self):
        """Teste la récupération d'utilisateur avec pytest."""
        User.objects.create_user(
            username='retrieveuser',
            password='pass123'
        )
        user = User.objects.get(username='retrieveuser')
        assert user.username == 'retrieveuser'
