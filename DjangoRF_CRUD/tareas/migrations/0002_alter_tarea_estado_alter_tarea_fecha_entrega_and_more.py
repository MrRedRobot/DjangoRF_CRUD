# Generated by Django 4.1.3 on 2022-12-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_entrega',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
