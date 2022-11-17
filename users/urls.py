from django.urls import path

from .views import GetAllOwners, OwnerDetailView, Login, GetAllKeepers, KeeperDaysView

urlpatterns = [
    path("", Login),
    path("getAll", GetAllOwners.as_view()),
    path("keeper/getAll", GetAllKeepers.as_view()),
    path("<int:pk>/detailUser", OwnerDetailView.as_view(), name="detalle_usuario"),
    path("<int:pk>/detailKeeper", OwnerDetailView.as_view(), name="detalle_keeper"),
    path("<int:pk>/detailKeeper/days", KeeperDaysView.as_view(), name="detalle_keeper"),
]
