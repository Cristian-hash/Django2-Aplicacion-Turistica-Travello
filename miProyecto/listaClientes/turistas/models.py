from django.db import models

# Create your models here.
#Creando el modelo 

class Turista(models.Model):
    nombre=models.TextField()
    apellidos=models.TextField()
    dni=models.TextField()
