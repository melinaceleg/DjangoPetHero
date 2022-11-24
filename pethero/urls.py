
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("users.urls")),
    # path("users/", include("users.urls")),
    path("bookings/", include("bookings.urls")),
    path("pets/", include("pets.urls")),
    path("admin/", admin.site.urls),
]
