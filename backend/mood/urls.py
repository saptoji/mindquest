"""URLs for mood app."""
from django.urls import path
from .views import MoodCreateView, MoodHistoryView

app_name = 'mood'

urlpatterns = [
    path('', MoodCreateView.as_view(), name='create'),
    path('history/', MoodHistoryView.as_view(), name='history'),
]
