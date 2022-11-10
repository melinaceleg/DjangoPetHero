from django.urls import path

from pets.views import GetAllPets

urlpatterns = [
    path("getAll", GetAllPets.as_view()),
]
