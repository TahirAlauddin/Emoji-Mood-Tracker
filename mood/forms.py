from django import forms
from .models import Mood, UserProfile, EMOJI_CHOICES


class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ["emoji", "intensity", "notes"]
        widgets = {
            "emoji": forms.Select(attrs={"class": "form-select"}),
            "intensity": forms.NumberInput(attrs={"class": "form-input"}),
            "notes": forms.Textarea(attrs={"class": "form-textarea", "rows": 3}),
        }


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["bio", "birth_date", "preferred_emoji"]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }
