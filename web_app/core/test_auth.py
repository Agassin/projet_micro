"""
Tests d'authentification et d'autorisation.

Ce module contient les tests pour l'authentification et l'autorisation.
"""

import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class AuthenticationTestCase(TestCase):
    """Tests pour l'authentification."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='authuser',
            email='auth@example.com',
            password='authpass123'
        )

    def test_user_login_success(self):
        """Teste une connexion réussie."""
        login_success = self.client.login(
            username='authuser',
            password='authpass123'
        )
        self.assertTrue(login_success)

    def test_user_login_failure_wrong_password(self):
        """Teste une connexion échouée avec mauvais mot de passe."""
        login_success = self.client.login(
            username='authuser',
            password='wrongpassword'
        )
        self.assertFalse(login_success)

    def test_user_login_failure_nonexistent_user(self):
        """Teste une connexion échouée avec utilisateur inexistant."""
        login_success = self.client.login(
            username='nonexistent',
            password='password123'
        )
        self.assertFalse(login_success)

    def test_logged_in_user_session(self):
        """Teste que la session est créée après connexion."""
        self.client.login(username='authuser', password='authpass123')
        self.assertIn('_auth_user_id', self.client.session)

    def test_user_logout(self):
        """Teste la déconnexion d'un utilisateur."""
        self.client.login(username='authuser', password='authpass123')
        self.assertIn('_auth_user_id', self.client.session)

        self.client.logout()
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_auth_api_login_success(self):
        """Teste l'API d'authentification avec des identifiants codés en dur."""
        response = self.client.post(
            reverse('api_auth_login'),
            data={
                'username': 'maman',
                'password': 'test123'
            },
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('redirect_url'), '/dashboard/')

    def test_auth_api_login_failure(self):
        """Teste l'API d'authentification avec de mauvais identifiants."""
        response = self.client.post(
            reverse('api_auth_login'),
            data={
                'username': 'maman',
                'password': 'wrong'
            },
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 401)
        self.assertFalse(response.json().get('success'))

    def test_multiple_user_login(self):
        """Teste la connexion de plusieurs utilisateurs différents."""
        user2 = User.objects.create_user(
            username='authuser2',
            password='authpass123'
        )
        self.assertIsNotNone(user2)

        # Connexion du premier utilisateur
        login1 = self.client.login(username='authuser', password='authpass123')
        self.assertTrue(login1)

        # Déconnexion
        self.client.logout()

        # Connexion du deuxième utilisateur
        login2 = self.client.login(username='authuser2', password='authpass123')
        self.assertTrue(login2)


class AuthorizationTestCase(TestCase):
    """Tests pour l'autorisation."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.client = Client()
        self.regular_user = User.objects.create_user(
            username='regularuser',
            password='regularpass123'
        )
        self.admin_user = User.objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='adminpass123'
        )

    def test_regular_user_is_not_staff(self):
        """Vérifie qu'un utilisateur régulier n'est pas staff."""
        self.assertFalse(self.regular_user.is_staff)

    def test_admin_user_is_staff(self):
        """Vérifie qu'un administrateur est staff."""
        self.assertTrue(self.admin_user.is_staff)

    def test_regular_user_is_not_superuser(self):
        """Vérifie qu'un utilisateur régulier n'est pas superuser."""
        self.assertFalse(self.regular_user.is_superuser)

    def test_admin_user_is_superuser(self):
        """Vérifie qu'un administrateur est superuser."""
        self.assertTrue(self.admin_user.is_superuser)

    def test_user_permissions(self):
        """Teste les permissions des utilisateurs."""
        # Un utilisateur régulier n'a pas de permissions spéciales
        self.assertEqual(self.regular_user.user_permissions.count(), 0)


@pytest.mark.django_db
class PytestAuthenticationTests:
    """Tests d'authentification avec pytest."""

    def test_user_login_with_pytest(self, client, user):
        """
        Teste la connexion avec pytest.

        Args:
            client: Client Django
            user: Utilisateur fixture
        """
        login_success = client.login(
            username='testuser',
            password='testpass123'
        )
        assert login_success

    def test_user_authentication_check(self, user):
        """
        Teste la vérification d'authentification.

        Args:
            user: Utilisateur fixture
        """
        assert user.check_password('testpass123')
        assert not user.check_password('wrongpassword')

    def test_admin_user_privileges(self, admin_user):
        """
        Teste les privilèges d'admin.

        Args:
            admin_user: Utilisateur admin fixture
        """
        assert admin_user.is_staff
        assert admin_user.is_superuser

    def test_authenticated_client_has_user(self, authenticated_client, user):
        """
        Teste que le client authentifié a les bonnes données.

        Args:
            authenticated_client: Client authentifié fixture
            user: Utilisateur fixture
        """
        # Le client est maintenant authentifié
        response = authenticated_client.get('/')
        assert response.status_code == 200
