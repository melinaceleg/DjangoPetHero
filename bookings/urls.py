from django.urls import path

from .views import GetAllBookings, NewBookingView

urlpatterns = [
    path("getAll", GetAllBookings.as_view()),
    path("<int:pet_pk>/<int:keeper_pk>/<int:availability_pk>/newbooking", NewBookingView.as_view(), name="nuevo_booking"),
]
