from django.urls import path
from .views import Homepage

urlpatterns = [
    path("", Homepage), # localhost:8000 -> Homepage
]