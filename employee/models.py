from django.db import models



# Create your models here.





class Staff(models.Model):
    name =models.CharField(max_length=120)
    age = models.PositiveIntegerField(default=2)
    idnum = models.PositiveIntegerField(default=100)
    place=models.CharField(max_length=120)
    experience = models.PositiveIntegerField(default=3)

class Food(models.Model):
    name=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to ="images",null=True,blank=True)



