# Generated by Django 5.1.2 on 2024-10-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resena',
            old_name='fecha',
            new_name='fecha_creacion',
        ),
        migrations.AlterField(
            model_name='resena',
            name='puntuacion',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='resena',
            unique_together={('usuario', 'juego')},
        ),
    ]