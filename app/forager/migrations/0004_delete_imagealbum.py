# Generated by Django 4.1 on 2022-12-29 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forager', '0003_remove_record_album_remove_species_album'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageAlbum',
        ),
    ]