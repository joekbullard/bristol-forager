# Generated by Django 4.1 on 2022-12-30 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forager', '0005_alter_imagespecies_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='species',
            old_name='forage_end',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='species',
            old_name='forage_start',
            new_name='start',
        ),
    ]
