from django import forms
from .models import Mood


class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ["emoji", "intensity", "notes"]
        widgets = {
            "emoji": forms.Select(attrs={"class": "form-select"}),
            "intensity": forms.NumberInput(attrs={"class": "form-input"}),
            "notes": forms.Textarea(attrs={"class": "form-textarea", "rows": 3}),
        }
