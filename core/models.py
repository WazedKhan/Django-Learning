import qrcode
from io import BytesIO
from PIL import Image, ImageDraw

from django.db import models
from django.core.files import File
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    address_line_1 = models.CharField(max_length=100, null=True)
    address_line_2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state=models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    county = models.CharField(max_length=100, null=True)


    class Meta:
        db_table="customer"
        ordering= ["-user__date_joined", "user__username"]

    def __str__(self):
        return str(self.user.username)


class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)

    class Meta:
        db_table="product"

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.SET_NULL
    )
    product = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order"
        ordering = ["-date_created"]

    def __str__(self):
        return self.customer


    # ---------------------------------------------------------

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return '%s: %s' % (self.album_name, self.artist)


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)

class QR(models.Model):
    name = models.CharField(max_length=250)
    qr_code = models.ImageField(upload_to="QR_codes", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)