from django.db import models

# Create your models here.
#Creando el modelo 

class Turista(models.Model):
    nombres=models.TextField()
    apellidos=models.TextField()

    #no nos importa de que pais venga
    nacionalidad=models.TextField()
    #importante que se tenga que marcar esta casilla por eso lo dejo en false
    vacunado_Covid=models.BooleanField(default=False)

    
#creacion de un objeto por el shell