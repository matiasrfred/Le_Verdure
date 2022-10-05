from unittest.util import _MAX_LENGTH
from urllib.parse import MAX_CACHE_SIZE
from django.db import models

# Create your models here.

class pdv_ext(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre = models.CharField(max_length=50)
    calidad = models.CharField(max_length=1)

    def __str__(self):
        return (self.nombre +" "+ self.calidad)
