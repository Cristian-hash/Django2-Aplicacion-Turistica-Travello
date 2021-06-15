from django.shortcuts import render

# Create your views here.
def index(request,*args,**kwargs):

    #creacion de diccionario 
    return render(request,'index.html')
