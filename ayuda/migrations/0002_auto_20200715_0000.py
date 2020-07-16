# Generated by Django 3.0.8 on 2020-07-15 06:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidad', '0001_initial'),
        ('beneficiario', '0001_initial'),
        ('ayuda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayuda',
            name='beneficiario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beneficiarios', to='beneficiario.beneficiario'),
        ),
        migrations.AddField(
            model_name='ayuda',
            name='entidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entidades', to='entidad.entidad'),
        ),
        migrations.AddField(
            model_name='ayuda',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
