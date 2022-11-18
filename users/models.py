from django.contrib.auth.models import User, AbstractUser
from django.db import models

from bookings.models import Booking


class Owner(User):
    phone = models.CharField(max_length=255)

    def get_all_bookings(self):
        return Booking.objects.filter(pet__owner_id=self.pk)

    class Meta:
        verbose_name = 'Owner'


class Keeper(Owner):
    pet_size = models.CharField(choices=(('sm', 'Small'),
                                         ('md', 'Medium'),
                                         ('lg', 'Large')),
                                max_length=2)
    keep_price = models.FloatField()

    class Meta:
        verbose_name = 'Keeper'


class Availability(models.Model):
    day = models.DateField()
    state = models.BooleanField(default=True)
    keeper = models.ForeignKey(Keeper, on_delete=models.CASCADE)