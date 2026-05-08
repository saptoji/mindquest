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
