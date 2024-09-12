from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Mood


class MoodLoggerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

    def test_log_mood(self):
        response = self.client.post(
            reverse("log_mood"),
            {"emoji": "😄", "intensity": 5, "notes": "Feeling great today!"},
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful post
        self.assertEqual(Mood.objects.count(), 1)
        mood = Mood.objects.first()
        self.assertEqual(mood.user, self.user)
        self.assertEqual(mood.emoji, "😄")

    def test_dashboard(self):
        Mood.objects.create(user=self.user, emoji="🙂", intensity=4)
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "🙂")
