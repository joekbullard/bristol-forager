# Generated by Django 4.1 on 2022-12-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forager', '0004_delete_imagealbum'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagespecies',
            options={'verbose_name_plural': 'image species'},
        ),
        migrations.RenameField(
            model_name='imagerecord',
            old_name='product',
            new_name='record',
        ),
        migrations.RenameField(
            model_name='imagespecies',
            old_name='product',
            new_name='species',
        ),
        migrations.RemoveField(
            model_name='imagerecord',
            name='name',
        ),
        migrations.RemoveField(
            model_name='imagespecies',
            name='name',
        ),
        migrations.AddField(
            model_name='imagespecies',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
