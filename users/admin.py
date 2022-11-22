from django.contrib import admin

from .models import Owner, Keeper, Availability

# Register your models here.
admin.site.register(Owner)
admin.site.register(Keeper)
admin.site.register(Availability)