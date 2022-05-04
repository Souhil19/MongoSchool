from django.db import models

# Create your models here.


class Student(models.Model):
    name =models.CharField(max_length=20)
    birth_date= models.DateField()
    field= models.CharField(max_length=5)
