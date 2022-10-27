from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Owner(User):
    phone = models.CharField(max_length=255)


class Keeper(Owner):
    pet_size = models.CharField(choices=(('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')), max_length=2)
    keep_price = models.FloatField()

