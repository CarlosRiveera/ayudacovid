# Generated by Django 3.0.8 on 2020-07-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayuda', '0002_auto_20200715_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayuda',
            name='nombreAyuda',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
