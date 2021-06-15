from django.db import models
# min 1:25:52
# Create your models here.

class Destination:
    id: int
    name : str
    img:str
    desc: str
    price:int