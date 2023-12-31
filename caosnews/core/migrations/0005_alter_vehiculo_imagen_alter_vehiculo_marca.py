# Generated by Django 4.2.2 on 2023-07-11 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_vehiculo_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='vehiculos/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(max_length=15, verbose_name='Titulo'),
        ),
    ]
