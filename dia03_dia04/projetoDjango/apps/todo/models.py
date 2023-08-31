from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)# campo de texto limitado
    
    description = models.TextField()# sem limite de caracters
    
    date = models.DateField()# data
    
    def __str__(self):
        return self.name    