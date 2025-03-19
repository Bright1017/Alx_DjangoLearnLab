from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class AuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    # def test_login_view(self):
    #     response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass123'})
    #     self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_profile_access_unauthorized(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/login/?next=/profile/')

    def test_csrf_token_present(self):
        response = self.client.get(reverse('register'))
        self.assertContains(response, 'csrfmiddlewaretoken')