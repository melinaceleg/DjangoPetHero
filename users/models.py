from django.contrib.auth.models import User, AbstractUser
from django.db import models

from bookings.models import Booking
from pets.models import Pet


class Owner(User):
    phone = models.CharField(max_length=255)

    def get_all_bookings(self):
        return Booking.objects.filter(pet__owner_id=self.pk)

    def get_all_pets(self):
        return Pet.objects.filter(owner_id=self.pk)

    def get_class(self):
        return "Owner"

    class Meta:
        verbose_name = 'Owner'


class Keeper(Owner):
    pet_size = models.CharField(choices=(('Small', 'Small'),
                                         ('Medium', 'Medium'),
                                         ('Large', 'Large')),
                                max_length=10)
    keep_price = models.FloatField()


    def get_all_availability(self):
        return Availability.objects.filter(keeper_id=self.pk)


    def get_class(self):
        return "Keeper"

    class Meta:
        verbose_name = 'Keeper'


class Availability(models.Model):
    day = models.DateField()
    state = models.BooleanField(default=True)
    keeper = models.ForeignKey(Keeper, on_delete=models.CASCADE)
    # booking = models.ForeignKey("bookings.Booking", on_delete=models.CASCADE, related_name="bookings", null=True, blank=True)

