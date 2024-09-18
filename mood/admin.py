from django.contrib import admin

from .models import UserProfile, Mood


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
