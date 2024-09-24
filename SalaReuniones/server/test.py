import unittest
from datetime import datetime, timedelta
import logging
import os
import django
import unittest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SalaReuniones.settings')
django.setup()

from server.services import (
    asignar_reuniones_a_salas,
    capacidad_sala,
    sala_disponible,
    notificar
)
from server.models import Sala, Reunion 

class TestAsignaciones(unittest.TestCase):
    # Configuración de salas y reuniones para las pruebas
    def setUp(self):
        self.salas = [
            Sala(id=1, nombre='Sala A', capacidad_maxima=10),
            Sala(id=2, nombre='Sala B', capacidad_maxima=20),
        ]

        self.reuniones = [
            Reunion(id=1, descripcion='Reunión 1', cantidad_asistentes=5,
                    horario_deseado=datetime(2024, 9, 20, 10, 0), duracion=timedelta(hours=1)),
            Reunion(id=2, descripcion='Reunión 2', cantidad_asistentes=8,
                    horario_deseado=datetime(2024, 9, 20, 11, 0), duracion=timedelta(hours=1)),
            Reunion(id=3, descripcion='Reunión 3', cantidad_asistentes=15,
                    horario_deseado=datetime(2024, 9, 20, 12, 0), duracion=timedelta(hours=1)),
        ]
    # se asignan 3 reuniones
    def test_asignar_reuniones_a_salas_exitoso(self):
        asignaciones = asignar_reuniones_a_salas(self.salas, self.reuniones)
        self.assertEqual(len(asignaciones), 3)  

    
        asignaciones = asignar_reuniones_a_salas(self.salas, self.reuniones)
        self.assertEqual(len(asignaciones), 3)  

    # se recuelven los conflictos entre salas
    def test_sala_disponible_sin_conflictos(self):
        salas_ocupadas = {}
        reunion = Reunion(id=5, descripcion='Reunión Test',
                          cantidad_asistentes=5,
                          horario_deseado=datetime(2024, 9, 20, 10, 0),
                          duracion=timedelta(hours=1))
        self.assertTrue(sala_disponible(salas_ocupadas, 1, reunion.horario_deseado, reunion.duracion))

    # se resuelven los conflictos entre salas A y B
    def test_sala_disponible_con_conflictos(self):
        salas_ocupadas = {
            1: [{'inicio': datetime(2024, 9, 20, 10, 0), 'duracion': timedelta(hours=1)}]
        }
        reunion = Reunion(id=6, descripcion='Reunión Test Conflicto',
                          cantidad_asistentes=5,
                          horario_deseado=datetime(2024, 9, 20, 10, 30),
                          duracion=timedelta(hours=1))
        self.assertFalse(sala_disponible(salas_ocupadas, 1, reunion.horario_deseado, reunion.duracion))

    # test para capacidad de sala maximo 10 personas 
    def test_capacidad_sala(self):
        sala = Sala(id=1, nombre='Sala A', capacidad_maxima=10)
        self.assertEqual(capacidad_sala(sala), 10)

    # si no hay disponibilidad entrega error
    def test_notificar(self):
        with self.assertLogs('root', level='INFO') as log:  
            notificar({'id': 1})
            self.assertIn("No se pudo asignar la reunión con id 1 debido a falta de disponibilidad.", log.output[0])


if __name__ == '__main__':
    unittest.main()