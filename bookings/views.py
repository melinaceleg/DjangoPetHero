from django.shortcuts import render
from django.views.generic import ListView

from bookings.models import Booking


class GetAllBookings(ListView):
    model = Booking
    queryset = Booking.objects.all()
    template_name = "bookings/getall.html"