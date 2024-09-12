from django.contrib import admin

from .models import UserProfile, Mood


@admin.site.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    pass


@admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
