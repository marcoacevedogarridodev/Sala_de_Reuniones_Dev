from rest_framework import serializers
from rest_framework import viewsets
from server.models import Reunion
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from server.api.sala import SalaSerializer


class ReunionesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reunion
        fields = [ 'id', 'descripcion', 'duracion', 'cantidad_asistentes', 'horario_deseado']

    def validate(self, data):
        if 'duracion' not in data:
            raise serializers.ValidationError({"duracion": "Este campo es obligatorio."})
        return data


class ReunionesViewSet(viewsets.ModelViewSet):
    queryset = Reunion.objects.all()
    serializer_class = ReunionesSerializer


@api_view(['POST'])
def crear_reunion(request):
    serializer = ReunionesSerializer(data=request.data)
    if serializer.is_valid():
        reunion = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_reunion(request, pk):
    try:
        reunion = Reunion.objects.get(pk=pk)
    except Reunion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    reunion.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

