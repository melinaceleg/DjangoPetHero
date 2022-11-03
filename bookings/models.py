import this

from django.db import models


class Booking(models.Model):
    owner = models.ForeignKey("users.Owner", on_delete=models.CASCADE, related_name="owners")
    keeper = models.ForeignKey("users.Keeper", on_delete=models.CASCADE, related_name="keepers")
    # pet = models.ForeignKey(pets.Pet, on_delete=models.CASCADE)
    price = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    # duration = models.IntegerField()
    status = models.CharField(choices=(('r', 'Reserved'), ('p', 'In Progress'), ('f', 'Finalized')),
                              max_length=1,
                              default='r')

    def get_total_days(self):
        delta = self.end_date - self.start_date
        return delta.days

    def calculate_price(self):
        price = self.get_total_days() * self.keeper.keep_price
        return price


class Review(models.Model):
    date = models.DateField()
    review = models.CharField(max_length=1000)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)