# Generated by Django 5.1.2 on 2024-10-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0002_rename_fecha_resena_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrador'), ('user', 'Usuario')], default='user', max_length=10),
        ),
    ]
