from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mood/home.html')

    def test_dashboard_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mood/dashboard.html')

    def test_log_mood_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('log_mood'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mood/log_mood.html')