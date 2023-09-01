from django.db import models
from apps.users.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)# campo de texto limitado
    
    description = models.TextField()# sem limite de caracters
    
    date = models.DateField()# data
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #user = models.ForeignKey(User, on_delete=models.PROTECT)
    #user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    
    def __str__(self):
        return self.name