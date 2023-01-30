from django.urls import path
from .views import OrderList, AlbumList

urlpatterns = [
    path("", OrderList.as_view(), name="order-list"),
    path("album", AlbumList.as_view(), name="order-list"),
]