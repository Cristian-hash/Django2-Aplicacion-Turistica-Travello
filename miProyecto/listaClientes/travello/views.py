from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request,*args,**kwargs):

    dest1=Destination()
    dest1.name='Arequipa (Dinamico)'#cambiando statico a dinamico
    dest1.desc='Ciudad Blanca(Dinamico)'
    #13.passing Dynamic Data in html(prt2)//imagen que sea dinamica
    dest1.img='destination_1.jpg'
    dest1.price=1000
    
    dest2=Destination()
    dest2.name='Lima (Dinamico)'#cambiando statico a dinamico
    dest2.desc='Ciudad De Los Reyes(Dinamico)'
    #13.passing Dynamic Data in html(prt2)//imagen que sea dinamica
    dest2.img='destination_2.jpg'
    dest2.price=4000

    dest3=Destination()
    dest3.name='Trujillo (Dinamico)'#cambiando statico a dinamico
    dest3.desc='Ciudad La Marineroa(Dinamico)'
    #13.passing Dynamic Data in html(prt2)//imagen que sea dinamica
    dest3.img='destination_1.jpg'
    dest3.price=8000



    #pasando tooo esto como un solo objeto
    dests=[dest1,dest2,dest3]


    #creacion de diccionario 

    #de partir de la coma espara convertir el precio en dinamico
    return render(request,'index.html',{'dest1':dests})
