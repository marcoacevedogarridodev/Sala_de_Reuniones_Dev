from django.db import models
from django.core.exceptions import ValidationError


class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    horario_disponibilidad = models.CharField(max_length=50)  
    capacidad_maxima = models.IntegerField()

    def __str__(self):
        return self.nombre
        

class Reunion(models.Model):
    descripcion = models.CharField(max_length=255)
    duracion = models.DurationField()  
    cantidad_asistentes = models.IntegerField()
    horario_deseado = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return f"Reunión {self.id}: {self.descripcion} (Duración: {self.duracion})"
    
    def validate(self):
        if self.cantidad_asistentes > self.sala.capacidad_maxima:
            raise ValidationError('La cantidad de asistentes no puede exceder la capacidad maxima de la sala.')


class Asignacion(models.Model):
    sala = models.ForeignKey(Sala, related_name='asignaciones', on_delete=models.CASCADE)
    reunion = models.ForeignKey(Reunion, related_name='asignaciones', on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return f"Asignación de {self.reunion} en {self.sala} para el {self.fecha}"

