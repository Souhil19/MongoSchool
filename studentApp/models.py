#from django.db import models
from djongo import models

# Create your models here.


class Subscription(models.Model):
    starting_year= models.DateField()
    ending_year=models.DateField()

    class Meta:
        abstract = True


class Student(models.Model):
    name =models.CharField(max_length=20)
    birth_date= models.DateField()
    field= models.CharField(max_length=5)
    subscription = models.EmbeddedField(
        model_container=Subscription,default=''
    )
    objects = models.DjongoManager()

