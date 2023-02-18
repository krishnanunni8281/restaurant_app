from django.contrib.auth.models import AbstractUser

from django.db import models
from employee.models import Food

class User(AbstractUser):
    options=(("employee","employee"),
             ("customer","customer"))
    role=models.CharField(max_length=12,choices=options,default="customer")

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Food,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("incart","incart"),
        ("cancelled","cancelled"),
        ("order_placed", "order_placed")

    )
    status=models.CharField(max_length=120,choices=options,default="incart")

class Orders(models.Model):
    item=models.ForeignKey(Food,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    address=models.CharField(max_length=100)
    options=(
        ("buyitem","buyitem"),
        ("cancel","cancel"),
        ("intransit","intransit"),
        ('orderplaced','orderplaced')
    )
    status=models.CharField(max_length=30,choices=options,default="buyitem")

