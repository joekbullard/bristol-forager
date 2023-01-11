# Generated by Django 4.1 on 2022-12-29 14:54

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import forager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageAlbum",
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
            ],
        ),
        migrations.CreateModel(
            name="Species",
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
                ("common_name", models.CharField(max_length=200)),
                ("scientific_name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("forage_start", models.DateField(null=True)),
                ("forage_end", models.DateField(null=True)),
                (
                    "album",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_album",
                        to="forager.imagealbum",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "species",
                "ordering": ["common_name"],
            },
        ),
        migrations.CreateModel(
            name="Record",
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
                ("record_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
                ("notes", models.TextField(blank=True, null=True)),
                ("location", django.contrib.gis.db.models.fields.PointField(srid=4326)),
                (
                    "album",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_album",
                        to="forager.imagealbum",
                    ),
                ),
                (
                    "species",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="forager.species",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "record",
                "ordering": ["-record_date"],
            },
        ),
        migrations.CreateModel(
            name="Image",
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
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to=forager.models.get_upload_path)),
                ("default", models.BooleanField(default=False)),
                ("width", models.FloatField(default=100)),
                ("length", models.FloatField(default=100)),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="forager.imagealbum",
                    ),
                ),
            ],
        ),
    ]
