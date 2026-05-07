from django.contrib import admin
from .models import MoodLog


@admin.register(MoodLog)
class MoodLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'log_date', 'mood_score', 'energy_score')
    list_filter = ('log_date', 'mood_score')
    search_fields = ('user__username',)
