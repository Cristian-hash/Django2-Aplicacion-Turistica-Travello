from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mi_Bienvenida(request,*args,**kwargs):

    #creacion de diccionario 
    return render(request,'home.html',{'name':'Travello'})

def registro(request,*args,**kwargs):
    
    return render(request,'ingreso.html')
