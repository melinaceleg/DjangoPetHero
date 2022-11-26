from django.urls import path

from .views import GetAllOwners, OwnerDetailView, Login, GetAllKeepers, KeeperDetailView

urlpatterns = [
    path("", Login),
    path("getAll", GetAllOwners.as_view()),
    path("<int:pk>/detailUser", OwnerDetailView.as_view(), name="detalle_usuario"),
    path("keepers/<str:pet_size>/getAll", GetAllKeepers.as_view(), name="keepers_size"),
    path("<int:pk>/detailKeeper", KeeperDetailView.as_view(), name="detalle_keeper"),
]
