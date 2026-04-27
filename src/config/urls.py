from django.urls import path
from api.views import data, healthz

urlpatterns = [
    path("healthz", healthz),
    path("api/data", data),
]