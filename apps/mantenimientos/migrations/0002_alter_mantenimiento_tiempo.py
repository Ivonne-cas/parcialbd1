# Generated by Django 3.2.8 on 2021-10-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimientos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimiento',
            name='tiempo',
            field=models.IntegerField(verbose_name='tiempo'),
        ),
    ]
