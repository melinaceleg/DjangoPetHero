from django.urls import path

from .views import GetAllBookings

urlpatterns = [
    path("getAll", GetAllBookings.as_view()),
]
