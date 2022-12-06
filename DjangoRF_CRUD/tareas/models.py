from django.db import models

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=7)
    prioridad = models.CharField(max_length=6)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()