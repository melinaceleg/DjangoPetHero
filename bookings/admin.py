from django.contrib import admin

from bookings.models import Booking, Payment, Review

admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)