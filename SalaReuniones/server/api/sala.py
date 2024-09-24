from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import status
from server.models import Sala
from rest_framework.decorators import api_view
from rest_framework.response import Response
from server.models import Asignacion


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['id', 'nombre', 'horario_disponibilidad', 'capacidad_maxima']


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


@api_view(['GET'])
def calendario_sala(request, sala_id):
    try:
        sala = Sala.objects.get(pk=sala_id)
    except Sala.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    asignaciones = Asignacion.objects.filter(sala=sala).order_by('fecha')
    calendario = {
        'sala': sala.nombre,
        'asignaciones': []
    }

    for asignacion in asignaciones:
        calendario['asignaciones'].append({
            'reunion': asignacion.reunion.descripcion,
            'fecha': asignacion.fecha,
            'duracion': asignacion.reunion.duracion,
            'cantidad_asistentes': asignacion.reunion.cantidad_asistentes
        })

    return Response(calendario, status=status.HTTP_200_OK)