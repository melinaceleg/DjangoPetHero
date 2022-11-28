from django.urls import path

from .views import GetAllOwners, OwnerDetailView, Login, GetAllKeepers, KeeperDetailView

urlpatterns = [
    path("", Login),
    path("getAll", GetAllOwners.as_view()),
    path("<int:pk>/detailUser", OwnerDetailView.as_view(), name="detalle_usuario"),
    path("keepers/<int:pet_pk>/<str:pet_size>/getAll", GetAllKeepers.as_view(), name="keepers_size"),
    path("<int:pet_id>/<int:pk>/detailKeeper", KeeperDetailView.as_view(), name="detalle_keeper"),
]
