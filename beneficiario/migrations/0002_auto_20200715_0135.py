# Generated by Django 3.0.8 on 2020-07-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiario',
            name='nombreBeneficiario',
            field=models.CharField(max_length=140),
        ),
    ]