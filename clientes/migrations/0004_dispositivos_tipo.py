# Generated by Django 4.2.5 on 2023-09-06 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_dispositivos_icone'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivos',
            name='tipo',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
