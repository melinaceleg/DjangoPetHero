from django.contrib import admin

from .models import Owner, Keeper

# Register your models here.
admin.site.register(Owner)
admin.site.register(Keeper)