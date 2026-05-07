"""URLs for quests app."""
from django.urls import path
from .views import (
    TodayQuestListView, CompleteQuestView,
    QuestHistoryView, TodayCompletionStatsView
)

app_name = 'quests'

urlpatterns = [
    path('today/', TodayQuestListView.as_view(), name='today'),
    path('today-stats/', TodayCompletionStatsView.as_view(), name='today-stats'),
    path('history/', QuestHistoryView.as_view(), name='history'),
    path('<int:quest_id>/complete/', CompleteQuestView.as_view(), name='complete'),
]
