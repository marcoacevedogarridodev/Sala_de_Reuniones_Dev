import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)

# funcion para asignar reuniones a cada sala A o B 
def asignar_reuniones_a_salas(salas, reuniones):
    asignaciones = []
    salas_ocupadas = {}

    # Ordena reuniones por horario deseado
    reuniones = sorted(reuniones, key=lambda r: (r.horario_deseado is None, r.horario_deseado))

    # Recorre reuniones en base de datos y inserta datos
    for reunion in reuniones:
        sala_asignada = asignar_reunion_a_sala(salas, reunion, salas_ocupadas)
        
        if sala_asignada:
            asignaciones.append({
                "id": reunion.id,  
                "descripcion": reunion.descripcion,  
                "fecha": reunion.horario_deseado,  
                "sala_id": sala_asignada.id, 
            })
        else:
            notificar(reunion)  # Notifica si no se puede asignar la reunion
    
    return asignaciones


# funcion que asigna reunion si la sala se encuentra disponible 
def asignar_reunion_a_sala(salas, reunion, salas_ocupadas):
    for sala in salas:
        if sala_disponible(salas_ocupadas, sala.id, reunion.horario_deseado, reunion.duracion):
            if sala.id not in salas_ocupadas:
                salas_ocupadas[sala.id] = []
            salas_ocupadas[sala.id].append({
                'inicio': reunion.horario_deseado,
                'duracion': reunion.duracion,
            })
            # Devuelve la sala asignada
            return sala  
    return None

# funcion que nos trae la capacidad maxima de la sala a asignar
def capacidad_sala(sala):
    return sala.capacidad_maxima

# funcion que nos indica si la sala se encuentra disponible en el horario indicado (se inserta en asignar_reunion_a_sala)
def sala_disponible(salas_ocupadas, sala_id, horario_deseado, duracion):
    if horario_deseado is None or duracion is None:
        print(f"Error: horario_deseado={horario_deseado}, duracion={duracion}")
        return False  
    
    if sala_id not in salas_ocupadas:
        salas_ocupadas[sala_id] = []

    ocupacion_fin = horario_deseado + duracion
    
    for ocupacion in salas_ocupadas[sala_id]:
        ocupacion_inicio = ocupacion['inicio']
        ocupacion_fin_existente = ocupacion_inicio + ocupacion['duracion']
        
        # verificar si hay un conflicto de horario entre asignaciones
        if (horario_deseado < ocupacion_fin_existente and ocupacion_fin > ocupacion_inicio):
            return False
            
    return True

# funcion que actuializa el estado de la sala si estuviera ocupada 
def actualizar_sala_ocupada(salas_ocupadas, sala_id, horario_deseado, duracion):
    if sala_id not in salas_ocupadas:
        salas_ocupadas[sala_id] = []
    salas_ocupadas[sala_id].append({"inicio": horario_deseado, "duracion": duracion})

# funcion de notificacion de indisponibilidad de una reunion (con get traigo el id de cada reunion) y con loggin envio el error
def notificar(reunion):
    reunion_id = reunion.id
    logging.info(f"No se pudo asignar la reunión con id {reunion_id} debido a falta de disponibilidad.")









