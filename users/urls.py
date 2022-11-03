from django.urls import path

from .views import GetAllOwners, OwnerDetailView

urlpatterns = [
    path("getAll", GetAllOwners.as_view()),
    path("<int:pk>/detailUser", OwnerDetailView.as_view(), name="detalle_usuario"),
]
