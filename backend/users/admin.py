"""Admin registrations for users app."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'date_joined')
    search_fields = ('username', 'email')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'current_level', 'total_xp',
        'current_streak', 'best_streak', 'last_activity_date'
    )
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
