import json
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.conf import settings
from .models import Sala

# funcion sender que carga la base de datos con el archivo salas_config.json al momento de hacer una migracion 
@receiver(post_migrate)
def load_salas(sender, **kwargs):
    if sender.name == 'server': 
        try:
            config_path = settings.BASE_DIR / 'salas_config.json'
            with open(config_path) as f:
                salas = json.load(f)
            
            for sala_data in salas:
                Sala.objects.update_or_create(
                    nombre=sala_data['nombre'],
                    defaults={
                        'horario_disponibilidad': sala_data['horario_disponibilidad'],
                        'capacidad_maxima': sala_data['capacidad_maxima']
                    }
                )
        except Exception as e:
            print(f"Error al cargar las salas: {e}")
