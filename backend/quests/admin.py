"""Admin for quests app."""
from django.contrib import admin
from .models import Quest, UserQuestLog


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'xp_reward', 'is_active')
    list_filter = ('category', 'difficulty', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)


@admin.register(UserQuestLog)
class UserQuestLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'quest', 'completed_date', 'xp_earned', 'created_at')
    list_filter = ('completed_date',)
    search_fields = ('user__username', 'quest__title')
    readonly_fields = ('created_at',)
