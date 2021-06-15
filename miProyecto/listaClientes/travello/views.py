from django.shortcuts import render

# Create your views here.
def index(request,*args,**kwargs):

    #creacion de diccionario 

    #de partir de la coma espara convertir el precio en dinamico
    return render(request,'index.html',{'price':700})
