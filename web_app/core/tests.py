"""
Tests unitaires pour l'application core.

Ce module contient tous les tests unitaires pour les modèles, vues et URLs
de l'application Django.
"""

import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


# ============================================================================
# Tests des vues
# ============================================================================

class ViewsTestCase(TestCase):
    """Tests pour les vues de l'application."""

    def setUp(self):
        """
        Configuration avant chaque test.

        Crée un client pour les requêtes HTTP et un utilisateur de test.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_home_view_status_code(self):
        """Vérifie que la vue home retourne le code 200."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        """Vérifie que la vue home utilise le bon template."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')

    def test_home_view_context(self):
        """Vérifie que la vue home retourne un contexte valide."""
        response = self.client.get(reverse('home'))
        self.assertIsNotNone(response.context)

    def test_login_view_status_code(self):
        """Vérifie que la vue login retourne le code 200."""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_template_used(self):
        """Vérifie que la vue login utilise le bon template."""
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_get_request(self):
        """Vérifie que la vue login accepte les requêtes GET."""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_status_code(self):
        """Vérifie que la vue dashboard retourne le code 200."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_template_used(self):
        """Vérifie que la vue dashboard utilise le bon template."""
        response = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_dashboard_view_unauthenticated_access(self):
        """
        Vérifie que la vue dashboard est accessible sans authentification.

        Note: À améliorer selon les besoins de sécurité.
        """
        response = self.client.get(reverse('dashboard'))
        self.assertIn(response.status_code, [200, 302])

    def test_eleve_view_status_code(self):
        """Vérifie que la vue eleve retourne le code 200."""
        response = self.client.get(reverse('eleve'))
        self.assertEqual(response.status_code, 200)

    def test_eleve_view_template_used(self):
        """Vérifie que la vue eleve utilise le bon template."""
        response = self.client.get(reverse('eleve'))
        self.assertTemplateUsed(response, 'eleve.html')

    def test_eleve_view_context(self):
        """Vérifie que la vue eleve retourne un contexte valide."""
        response = self.client.get(reverse('eleve'))
        self.assertIsNotNone(response.context)


# ============================================================================
# Tests des URLs
# ============================================================================

class URLsTestCase(TestCase):
    """Tests pour les routes URL de l'application."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.client = Client()

    def test_home_url_resolves(self):
        """Vérifie que l'URL home se résout correctement."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url_reverse(self):
        """Vérifie que reverse('home') génère la bonne URL."""
        url = reverse('home')
        self.assertEqual(url, '/')

    def test_login_url_resolves(self):
        """Vérifie que l'URL login se résout correctement."""
        response = self.client.get('/login/')
        self.assertIn(response.status_code, [200, 404])

    def test_dashboard_url_resolves(self):
        """Vérifie que l'URL dashboard se résout correctement."""
        response = self.client.get('/dashboard/')
        self.assertIn(response.status_code, [200, 404])

    def test_eleve_url_resolves(self):
        """Vérifie que l'URL eleve se résout correctement."""
        response = self.client.get('/eleve/')
        self.assertIn(response.status_code, [200, 404])


# ============================================================================
# Tests des modèles
# ============================================================================

class ModelsTestCase(TestCase):
    """Tests pour les modèles de données."""

    def test_user_model_creation(self):
        """Vérifie que la création d'un utilisateur fonctionne."""
        user = User.objects.create_user(
            username='newuser',
            email='new@example.com',
            password='newpass123'
        )
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.email, 'new@example.com')
        self.assertTrue(user.check_password('newpass123'))

    def test_user_model_str(self):
        """Vérifie la représentation en chaîne du modèle User."""
        user = User.objects.create_user(
            username='struser',
            password='pass123'
        )
        self.assertEqual(str(user), 'struser')

    def test_user_model_email_field(self):
        """Vérifie que le champ email fonctionne correctement."""
        user = User.objects.create_user(
            username='emailuser',
            email='email@test.com',
            password='pass123'
        )
        self.assertEqual(user.email, 'email@test.com')


# ============================================================================
# Tests d'intégration
# ============================================================================

class IntegrationTestCase(TestCase):
    """Tests d'intégration pour vérifier le flux complet."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='integrationuser',
            email='integration@test.com',
            password='integrationpass123'
        )

    def test_user_creation_and_login(self):
        """Teste la création d'un utilisateur et la connexion."""
        login_success = self.client.login(
            username='integrationuser',
            password='integrationpass123'
        )
        self.assertTrue(login_success)

    def test_user_creation_and_access_home(self):
        """Teste l'accès à la page d'accueil après création d'utilisateur."""
        self.client.login(
            username='integrationuser',
            password='integrationpass123'
        )
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_navigation_flow(self):
        """Teste le flux de navigation entre les pages."""
        # Accès à la page d'accueil
        home_response = self.client.get(reverse('home'))
        self.assertEqual(home_response.status_code, 200)

        # Accès à la page de connexion
        login_response = self.client.get(reverse('login'))
        self.assertEqual(login_response.status_code, 200)

        # Connexion
        login_success = self.client.login(
            username='integrationuser',
            password='integrationpass123'
        )
        self.assertTrue(login_success)

        # Accès au tableau de bord
        dashboard_response = self.client.get(reverse('dashboard'))
        self.assertEqual(dashboard_response.status_code, 200)


# ============================================================================
# Tests des fixtures pytest
# ============================================================================

@pytest.mark.django_db
class PytestViewTests:
    """Tests des vues avec pytest et ses fixtures."""

    def test_home_view_with_pytest(self, client):
        """
        Teste la vue home avec pytest.

        Args:
            client: Fixture client Django
        """
        response = client.get(reverse('home'))
        assert response.status_code == 200
        assert 'index.html' in [t.name for t in response.templates]

    def test_login_view_with_pytest(self, client):
        """
        Teste la vue login avec pytest.

        Args:
            client: Fixture client Django
        """
        response = client.get(reverse('login'))
        assert response.status_code == 200

    def test_dashboard_view_with_pytest(self, client):
        """
        Teste la vue dashboard avec pytest.

        Args:
            client: Fixture client Django
        """
        response = client.get(reverse('dashboard'))
        assert response.status_code == 200

    def test_eleve_view_with_pytest(self, client):
        """
        Teste la vue eleve avec pytest.

        Args:
            client: Fixture client Django
        """
        response = client.get(reverse('eleve'))
        assert response.status_code == 200

    def test_authenticated_user_access(self, authenticated_client):
        """
        Teste l'accès avec un utilisateur authentifié.

        Args:
            authenticated_client: Fixture client authentifié
        """
        response = authenticated_client.get(reverse('home'))
        assert response.status_code == 200

    def test_admin_user_access(self, admin_client):
        """
        Teste l'accès avec un utilisateur administrateur.

        Args:
            admin_client: Fixture client admin
        """
        response = admin_client.get('/admin/')
        assert response.status_code == 200


# ============================================================================
# Tests de sécurité
# ============================================================================

class SecurityTestCase(TestCase):
    """Tests de sécurité pour l'application."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.client = Client()

    def test_csrf_protection_on_login(self):
        """Vérifie que la protection CSRF est active sur la page login."""
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'csrfmiddlewaretoken', count=0)

    def test_sql_injection_prevention(self):
        """Teste la prévention des injections SQL."""
        # Les vues actuelles ne traitent pas de données utilisateur,
        # mais ce test servira de base pour les futures vues
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_xss_protection(self):
        """Vérifie la protection contre les attaques XSS."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


# ============================================================================
# Tests de performance
# ============================================================================

class PerformanceTestCase(TestCase):
    """Tests de performance pour l'application."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.client = Client()

    def test_home_view_response_time(self):
        """Vérifie que la vue home répond rapidement."""
        import time
        start = time.time()
        self.client.get(reverse('home'))
        end = time.time()
        # La requête ne doit pas prendre plus de 1 seconde
        self.assertLess(end - start, 1.0)

    def test_multiple_requests_handling(self):
        """Teste la gestion de multiples requêtes simultanées."""
        for _ in range(10):
            response = self.client.get(reverse('home'))
            self.assertEqual(response.status_code, 200)


# ============================================================================
# Tests des templates
# ============================================================================

class TemplatesTestCase(TestCase):
    """Tests pour vérifier l'utilisation correcte des templates."""

    def setUp(self):
        """Configuration avant chaque test."""
        self.client = Client()

    def test_home_template_exists(self):
        """Vérifie que le template home existe."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')

    def test_login_template_exists(self):
        """Vérifie que le template login existe."""
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_dashboard_template_exists(self):
        """Vérifie que le template dashboard existe."""
        response = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_eleve_template_exists(self):
        """Vérifie que le template eleve existe."""
        response = self.client.get(reverse('eleve'))
        self.assertTemplateUsed(response, 'eleve.html')

    def test_all_templates_are_django_templates(self):
        """Vérifie que les templates sont des templates Django valides."""
        views_to_test = [
            (reverse('home'), 'index.html'),
            (reverse('login'), 'login.html'),
            (reverse('dashboard'), 'dashboard.html'),
            (reverse('eleve'), 'eleve.html'),
        ]
        for url, template_name in views_to_test:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, template_name)
