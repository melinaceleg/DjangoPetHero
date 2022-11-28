from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from bookings.models import Booking
from pets.models import Pet
from users.models import Keeper, Availability


class GetAllBookings(ListView):
    model = Booking
    queryset = Booking.objects.all()
    template_name = "bookings/getall.html"


class NewBookingView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "bookings/newBooking.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["pet_pk"] = self.kwargs["pet_pk"]
        context["keeper_pk"] = self.kwargs["keeper_pk"]
        context["availability_pk"] = self.kwargs["availability_pk"]
        self.create_booking(context["availability_pk"], context["pet_pk"], context["keeper_pk"])
        # Add in a QuerySet of all the books
        context['date'] = datetime.now()
        return context

    def create_booking(self, id_availability, id_pet, id_keeper):
        pet = Pet.objects.get(pk=id_pet)
        keeper = Keeper.objects.get(pk=id_keeper)
        # price = keeper.keep_price
        availability = Availability.objects.get(pk=id_availability)
        booking = Booking()
        booking.pet = pet
        availability.state = False
        availability.save()
        booking.availability = availability
        booking.save()
        # return redirect('/user/friends-add/')