from django.urls import path

from .views import GetAllOwners, OwnerDetailView, Login, GetAllKeepers, KeeperDetailView

urlpatterns = [
    path("", Login),
    path("getAll", GetAllOwners.as_view()),
    path("<int:pk>/detailUser", OwnerDetailView.as_view(), name="detalle_usuario"),
    path("keepers/getAll", GetAllKeepers.as_view()),
    path("<int:pk>/detailKeeper", KeeperDetailView.as_view(), name="detalle_keeper"),
]
