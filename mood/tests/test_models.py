from mood.models import Mood, UserProfile
from django.test import TestCase
from django.contrib.auth.models import User

class MoodModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.mood = Mood.objects.create(user=self.user, emoji='😊', intensity=5)

    def test_mood_creation(self):
        self.assertTrue(isinstance(self.mood, Mood))
        self.assertEqual(self.mood.__str__(), f"testuser's mood on {self.mood.date}: 😊")

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_profile_creation(self):
        profile = UserProfile.objects.get(user=self.user)
        self.assertTrue(isinstance(profile, UserProfile))
        self.assertEqual(profile.__str__(), "testuser's profile")

