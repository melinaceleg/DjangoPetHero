from django.urls import path

from .views import GetAllOwners, OwnerDetailView, Login, GetAllKeepers, KeeperDaysView, KeeperDetailView

urlpatterns = [
    path("", Login),
    path("getAll", GetAllOwners.as_view()),
    path("keepers/getAll", GetAllKeepers.as_view()),
    path("<int:pk>/detailUser", OwnerDetailView.as_view(), name="detalle_usuario"),
    path("<int:pk>/detailKeeper", KeeperDetailView.as_view(), name="detalle_keeper"),
    path("<int:pk>/detailKeeper/days", KeeperDaysView.as_view(), name="detalle_keeper"),
]
