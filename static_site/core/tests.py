# core/tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class CoreViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )

    def test_home_view(self):
        """Tester la page d'accueil"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_view(self):
        """Tester la page À propos"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_login_view(self):
        """Tester la page de connexion"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/login.html')

    def test_register_view(self):
        """Tester la page d'inscription"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/register.html')

    def test_profile_view_requires_login(self):
        """Tester que la page profil nécessite une connexion"""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirection vers login
