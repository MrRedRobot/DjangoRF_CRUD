# Generated by Django 4.1.3 on 2022-12-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=2000)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(max_length=50)),
                ('prioridad', models.CharField(max_length=6)),
                ('fecha_entrega', models.DateTimeField()),
                ('comentario', models.TextField()),
            ],
        ),
    ]