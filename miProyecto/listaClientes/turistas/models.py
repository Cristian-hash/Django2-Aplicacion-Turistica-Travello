from django.db import models

# Create your models here.
#Creando el modelo 

class Turista(models.Model):
    nombres=models.TextField()
    apellidos=models.TextField()
    nacionalidad=models.TextField()
#creacion de un objeto por el shell