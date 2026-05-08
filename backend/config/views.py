import sys
import traceback
from io import StringIO
from django.http import JsonResponse
from django.core.management import call_command

def health_check(request):
    return JsonResponse({"status": "ok", "app": "MindQuest API"})

def run_migrations(request):
    output = StringIO()
    errors = StringIO()
    try:
        call_command('migrate', stdout=output, stderr=errors)
        return JsonResponse({
            "migrate": output.getvalue(),
            "errors": errors.getvalue(),
        })
    except Exception as e:
        return JsonResponse({
            "error": str(e),
            "traceback": traceback.format_exc(),
        })

def seed_quests(request):
    output = StringIO()
    errors = StringIO()
    try:
        call_command('seed_quests', stdout=output, stderr=errors)
        return JsonResponse({
            "seed": output.getvalue(),
            "errors": errors.getvalue(),
        })
    except Exception as e:
        return JsonResponse({
            "error": str(e),
            "traceback": traceback.format_exc(),
        })
