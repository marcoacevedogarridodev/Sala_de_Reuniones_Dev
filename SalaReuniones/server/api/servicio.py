from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from server.services import asignar_reuniones_a_salas
from server.models import Sala, Reunion
from .sala import SalaSerializer


@api_view(['POST'])  
def asignar_reuniones(request):
    salas = Sala.objects.all()
    reuniones = Reunion.objects.all() 
    
    asignaciones = asignar_reuniones_a_salas(salas, reuniones)

    salas_serialized = SalaSerializer(salas, many=True).data

    if asignaciones:
        return Response({"asignaciones": asignaciones, "salas": salas_serialized}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "no se pudo asignar ninguna reunion."}, status=status.HTTP_400_BAD_REQUEST)
