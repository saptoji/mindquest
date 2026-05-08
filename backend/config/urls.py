"""
MindQuest URL configuration.
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
)
from .views import health_check, debug_info, test_db


urlpatterns = [
    path('', health_check, name='health-check'),
    path('debug/', debug_info, name='debug-info'),
    path('debug/db/', test_db, name='test-db'),
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
