from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.TextField(max_length=100, unique=True)
    department = models.TextField(max_length=50)
    age = models.IntegerField()
    education = models.TextField(max_length=50)
    
    def __str__(self):
        return  f"{self.id}"
    
    
    
