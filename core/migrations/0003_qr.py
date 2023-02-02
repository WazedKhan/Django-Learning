# Generated by Django 4.1.4 on 2023-02-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_album_alter_order_product_track"),
    ]

    operations = [
        migrations.CreateModel(
            name="QR",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("qr_code", models.ImageField(blank=True, upload_to="QR_codes")),
            ],
        ),
    ]
