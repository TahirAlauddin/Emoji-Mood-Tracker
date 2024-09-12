# mood/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mood
from .forms import MoodForm


@login_required
def log_mood(request):
    if request.method == "POST":
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.save(commit=False)
            mood.user = request.user
            mood.save()
            return redirect("dashboard")
    else:
        form = MoodForm()
    return render(request, "mood/log_mood.html", {"form": form})


@login_required
def dashboard(request):
    recent_moods = Mood.objects.filter(user=request.user).order_by("-date")[:7]
    return render(request, "mood/dashboard.html", {"recent_moods": recent_moods})


def home(request):
    return render(request, "mood/home.html")
