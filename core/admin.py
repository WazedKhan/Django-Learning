from django.contrib import admin

from .models import Product, Order, Customer, Album, Track, QR


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(QR)