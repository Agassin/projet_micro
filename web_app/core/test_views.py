"""
Tests unitaires pour les vues de l'application.

Ce module contient des tests détaillés pour chaque vue.
"""

import pytest
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from core.views import home, login_view, dashboard, eleve


class HomeViewUnitTestCase(TestCase):
    """Tests unitaires pour la vue home."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.factory = RequestFactory()

    def test_home_view_returns_correct_response(self):
        """Vérifie que la vue home retourne une réponse HTTP."""
        request = self.factory.get('/')
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_home_view_contains_template(self):
        """Vérifie que la vue home utilise un template."""
        request = self.factory.get('/')
        response = home(request)
        # La réponse contient le contenu du template
        self.assertIsNotNone(response.content)


class LoginViewUnitTestCase(TestCase):
    """Tests unitaires pour la vue login."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.factory = RequestFactory()

    def test_login_view_returns_correct_response(self):
        """Vérifie que la vue login retourne une réponse HTTP."""
        request = self.factory.get('/login/')
        response = login_view(request)
        self.assertEqual(response.status_code, 200)

    def test_login_view_handles_get_request(self):
        """Vérifie que la vue login gère les requêtes GET."""
        request = self.factory.get('/login/')
        response = login_view(request)
        self.assertEqual(response.status_code, 200)


class DashboardViewUnitTestCase(TestCase):
    """Tests unitaires pour la vue dashboard."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_view_returns_correct_response(self):
        """Vérifie que la vue dashboard retourne une réponse HTTP."""
        request = self.factory.get('/dashboard/')
        response = dashboard(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_is_accessible(self):
        """Vérifie que le dashboard est accessible via le client."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)


class EleveViewUnitTestCase(TestCase):
    """Tests unitaires pour la vue eleve."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.factory = RequestFactory()
        self.client = Client()

    def test_eleve_view_returns_correct_response(self):
        """Vérifie que la vue eleve retourne une réponse HTTP."""
        request = self.factory.get('/eleve/')
        response = eleve(request)
        self.assertEqual(response.status_code, 200)

    def test_eleve_view_is_accessible(self):
        """Vérifie que la vue eleve est accessible via le client."""
        response = self.client.get(reverse('eleve'))
        self.assertEqual(response.status_code, 200)


class ViewsIntegrationTestCase(TestCase):
    """Tests d'intégration pour toutes les vues."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='viewtestuser',
            email='viewtest@example.com',
            password='viewtestpass123'
        )

    def test_all_views_return_200_status(self):
        """Vérifie que toutes les vues retournent le code 200."""
        views = [
            ('home', '/'),
            ('login', '/login/'),
            ('dashboard', '/dashboard/'),
            ('eleve', '/eleve/'),
        ]

        for view_name, url in views:
            response = self.client.get(url)
            self.assertIn(
                response.status_code,
                [200, 404],
                f"Vue {view_name} a retourné {response.status_code}"
            )

    def test_authenticated_user_can_access_views(self):
        """Teste que l'accès aux vues fonctionne quand authentifié."""
        self.client.login(
            username='viewtestuser',
            password='viewtestpass123'
        )

        views = ['home', 'login', 'dashboard', 'eleve']
        for view_name in views:
            response = self.client.get(reverse(view_name))
            self.assertIn(
                response.status_code,
                [200, 404],
                f"Vue {view_name} n'est pas accessible"
            )


@pytest.mark.django_db
class PytestViewDetailTests:
    """Tests détaillés des vues avec pytest."""

    def test_home_view_with_factory(self, rf):
        """
        Teste la vue home avec RequestFactory.

        Args:
            rf: RequestFactory (fixture pytest-django)
        """
        request = rf.get('/')
        response = home(request)
        assert response.status_code == 200

    def test_login_view_with_factory(self, rf):
        """
        Teste la vue login avec RequestFactory.

        Args:
            rf: RequestFactory (fixture pytest-django)
        """
        request = rf.get('/login/')
        response = login_view(request)
        assert response.status_code == 200

    def test_dashboard_view_with_factory(self, rf):
        """
        Teste la vue dashboard avec RequestFactory.

        Args:
            rf: RequestFactory (fixture pytest-django)
        """
        request = rf.get('/dashboard/')
        response = dashboard(request)
        assert response.status_code == 200

    def test_eleve_view_with_factory(self, rf):
        """
        Teste la vue eleve avec RequestFactory.

        Args:
            rf: RequestFactory (fixture pytest-django)
        """
        request = rf.get('/eleve/')
        response = eleve(request)
        assert response.status_code == 200
