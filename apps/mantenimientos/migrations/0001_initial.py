# Generated by Django 3.2.8 on 2021-10-22 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='fecha')),
                ('solicitud', models.IntegerField(verbose_name='solicitud')),
                ('tiempo', models.DurationField(verbose_name='tiempo')),
            ],
            options={
                'verbose_name': 'mantenimiento',
                'verbose_name_plural': 'mantenimientos',
            },
        ),
        migrations.CreateModel(
            name='MantenimientoEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, verbose_name='descripcion')),
                ('resultado', models.BooleanField(verbose_name='resultado')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.equipo', verbose_name='equipo')),
                ('mantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimientos.mantenimiento', verbose_name='mantenimiento')),
            ],
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='equipo',
            field=models.ManyToManyField(through='mantenimientos.MantenimientoEquipo', to='equipos.Equipo'),
        ),
    ]
