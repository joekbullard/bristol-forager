# Generated by Django 4.1 on 2022-12-30 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forager', '0006_rename_forage_end_species_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerecord',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_images', to='forager.record'),
        ),
        migrations.AlterField(
            model_name='imagespecies',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species_images', to='forager.species'),
        ),
    ]
