from django.db import models
from datetime import datetime

class Artista(models.Model):
    alias = models.CharField(max_length=30,primary_key=True)
    nombre =models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.alias

class Album(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDePublicacion = models.DateField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    nombre = models.CharField(max_length=60)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre