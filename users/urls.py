from django.urls import path

from .views import GetAllOwners

urlpatterns = [
    path("getAll", GetAllOwners.as_view()),
]
