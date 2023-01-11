# Generated by Django 4.1 on 2023-01-10 08:56

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forager', '0009_auto_20230109_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='import_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='record_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]