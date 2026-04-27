import os
from datetime import datetime, timezone
from django.http import JsonResponse


def healthz(_request):
    return JsonResponse({
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


def data(_request):
    return JsonResponse({
        "message": "Hello from the Django backend",
        "environment": os.getenv("APP_ENV", "unknown"),
        "version": os.getenv("APP_VERSION", "0.0.0"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })