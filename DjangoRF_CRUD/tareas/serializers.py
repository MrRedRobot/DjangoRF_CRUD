from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('id', 'nombre', 'descripcion', 'estado', 'prioridad', 'fecha_entrega', 'comentario')
        read_only_fields = ('fecha_entrega',)