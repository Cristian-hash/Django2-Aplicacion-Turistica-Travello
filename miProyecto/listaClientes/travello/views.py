from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request,*args,**kwargs):

    dest1=Destination()
    dest1.name='Arequipa (Dinamico)'#cambiando statico a dinamico
    dest1.desc='Ciudad Blanca(Dinamico)'
    dest1.price=1000
    
    #creacion de diccionario 

    #de partir de la coma espara convertir el precio en dinamico
    return render(request,'index.html',{'dest1':dest1})
