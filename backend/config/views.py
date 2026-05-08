import os
import sys
import traceback
from django.http import JsonResponse
from django.conf import settings

def health_check(request):
    return JsonResponse({"status": "ok", "app": "MindQuest API"})

def debug_info(request):
    info = {
        "debug": settings.DEBUG,
        "allowed_hosts": settings.ALLOWED_HOSTS,
        "database": str(settings.DATABASES['default']),
        "python_version": sys.version,
        "env_keys": [k for k in os.environ.keys() if not 'TOKEN' in k and not 'SECRET' in k and not 'PASSWORD' in k],
    }
    return JsonResponse(info)

def test_db(request):
    from django.db import connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
        return JsonResponse({"db_ok": True, "result": row})
    except Exception as e:
        return JsonResponse({"db_ok": False, "error": str(e), "traceback": traceback.format_exc()})

def test_register(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    try:
        user = User.objects.create_user(
            username=f"debug_{os.urandom(4).hex()}",
            password="TestPass123!",
            email="debug@example.com"
        )
        # Try to access profile
        profile = user.profile
        return JsonResponse({"created": True, "user_id": user.id, "profile_level": profile.current_level})
    except Exception as e:
        return JsonResponse({"created": False, "error": str(e), "traceback": traceback.format_exc()})
