from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField(default=0.0)
    cantidad = models.IntegerField()
