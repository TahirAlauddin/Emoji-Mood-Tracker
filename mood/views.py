# mood/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mood
from .forms import MoodForm, UserProfileForm


def home(request):
    return render(request, "mood/home.html")


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


@login_required
def mood_trends(request):
    weekly_trend = Mood.get_weekly_trend(request.user)
    print(weekly_trend)
    monthly_trend = Mood.get_monthly_trend(request.user)
    print(monthly_trend)

    from django.utils.dateformat import DateFormat

    # Assuming weekly_trend and monthly_trend are lists of dictionaries containing 'date' and 'avg_intensity'

    # Convert datetime.date objects to strings in 'YYYY-MM-DD' format
    weekly_trend = [
        {"date": trend['date'].strftime('%Y-%m-%d'), "avg_intensity": trend['avg_intensity']}
        for trend in weekly_trend
    ]

    monthly_trend = [
        {"date": trend['date'].strftime('%Y-%m-%d'), "avg_intensity": trend['avg_intensity']}
        for trend in monthly_trend
    ]

    # Now, pass this converted data into the context
    context = {
        "weekly_trend": list(weekly_trend),
        "monthly_trend": list(monthly_trend),
    }

    return render(request, "mood/mood_trends.html", context)


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    return render(request, 'mood/user_profile.html', {'form': form})
