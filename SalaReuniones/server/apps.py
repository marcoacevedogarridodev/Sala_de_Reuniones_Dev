from django.apps import AppConfig
import json
from django.conf import settings
from django.db.utils import OperationalError

class MyAppConfig(AppConfig):
    name = 'server'
    # llamar a la función de carga de salas
    def ready(self):     
        import server.signals

    def load_salas_from_config(self):
        try:
            # carga el archivo salas_config.json con la informacion de salas a la base de datos
            config_path = settings.BASE_DIR / 'salas_config.json'
            with open(config_path) as f:
                salas = json.load(f)

            from .models import Sala
            for sala_data in salas:
                Sala.objects.update_or_create(
                    nombre=sala_data['nombre'],
                    defaults={
                        'horario_disponibilidad': sala_data['horario_disponibilidad'],
                        'capacidad_maxima': sala_data['capacidad_maxima']
                    }
                )
        except OperationalError as e:
            print(f"Error al acceder a la base de datos: {e}")
