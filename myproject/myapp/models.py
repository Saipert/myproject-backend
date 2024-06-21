# En myapp/models.py

from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    rival = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
