# Generated by Django 3.0.8 on 2020-07-16 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ayuda', '0003_ayuda_nombreayuda'),
        ('tipo_ayuda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_ayuda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=150)),
                ('cantidad', models.FloatField(max_length=150)),
                ('ayuda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ayuda', to='ayuda.ayuda')),
                ('tipo_ayuda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_ayuda', to='tipo_ayuda.Tipo_ayuda')),
            ],
        ),
    ]
