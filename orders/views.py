from rest_framework import generics

from core.models import Order, Album
from .serializer import OrderSerializer, AlbumSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all() \
        .select_related('customer', 'customer__user')
    serializer_class = OrderSerializer


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all().prefetch_related("tracks")
    serializer_class = AlbumSerializer

