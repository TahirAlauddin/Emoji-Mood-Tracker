from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

EMOJI_CHOICES = [
    ("😄", "Very Happy"),
    ("🙂", "Happy"),
    ("😐", "Neutral"),
    ("🙁", "Sad"),
    ("😢", "Very Sad"),
]

class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="moods")
    emoji = models.CharField(max_length=2, choices=EMOJI_CHOICES)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    intensity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Intensity of the mood (1-5)",
    )

    @classmethod
    def get_weekly_trend(cls, user):
        end_date = timezone.now().date()
        start_date = end_date - timezone.timedelta(days=7)
        return (
            cls.objects.filter(user=user, date__range=[start_date, end_date])
            .values("date")
            .annotate(avg_intensity=Avg("intensity"))
            .order_by("date")
        )

    @classmethod
    def get_monthly_trend(cls, user):
        end_date = timezone.now().date()
        start_date = end_date - timezone.timedelta(days=30)
        return (
            cls.objects.filter(user=user, date__range=[start_date, end_date])
            .values("date")
            .annotate(avg_intensity=Avg("intensity"))
            .order_by("date")
        )

    class Meta:
        unique_together = ["user", "date"]
        permissions = [
            ("view_own_mood", "Can view own mood"),
            ("edit_own_mood", "Can edit own mood"),
        ]

    def __str__(self):
        return f"{self.user.username}'s mood on {self.date}: {self.emoji}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    notification_preferences = models.JSONField(default=dict)
    preferred_emoji = models.CharField(max_length=2, default='😊')

    def __str__(self):
        return f"{self.user.username}'s profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()