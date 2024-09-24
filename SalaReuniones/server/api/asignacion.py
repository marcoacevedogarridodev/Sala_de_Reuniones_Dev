from rest_framework import serializers
from rest_framework import viewsets
from server.models import Asignacion
from server.api.sala import SalaSerializer
from server.api.reuniones import ReunionesSerializer

class AsignacionSerializer(serializers.ModelSerializer):
    sala = SalaSerializer()
    reunion = ReunionesSerializer()

    class Meta:
        model = Asignacion
        fields = ['id', 'sala', 'reunion', 'fecha']


class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer