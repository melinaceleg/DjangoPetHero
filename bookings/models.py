import this
from datetime import date

from django.db import models

import users.models as users_models


class Booking(models.Model):
    # owner = models.ForeignKey("users.Owner", on_delete=models.CASCADE, related_name="owners")
    keeper = models.ForeignKey("users.Keeper", on_delete=models.CASCADE, related_name="keepers")
    pet = models.ForeignKey("pets.Pet", on_delete=models.CASCADE, related_name="pets")
    price = models.FloatField()
    status = models.CharField(choices=(('r', 'Reserved'), ('p', 'In Progress'), ('f', 'Finalized')),
                              max_length=1,
                              default='r')

    def get_total_days(self):
        delta = self.end_date - self.start_date
        return delta.days

    def calculate_price(self):
        price = self.get_total_days() * self.keeper.keep_price
        return price

    def get_dates(self):
        return [
            aval.day
            for aval in users_models.Availability.objects.filter(booking_id=self.pk).order_by('day')
        ]


class Review(models.Model):
    date = models.DateField()
    review = models.CharField(max_length=1000)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)


class Payment(models.Model):
    advancement = models.FloatField()
    paid_out = models.BooleanField(default=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)