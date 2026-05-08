"""
MindQuest URL configuration.
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
)
from .views import health_check, run_migrations, seed_quests


urlpatterns = [
    path('', health_check, name='health-check'),
    path('migrate/', run_migrations, name='run-migrations'),
    path('seed/', seed_quests, name='seed-quests'),
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/auth/', include('users.urls')),
    path('api/quests/', include('quests.urls')),
    path('api/mood/', include('mood.urls')),

    # API documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
