from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=50)
    cls = models.CharField(max_length=50)
    roll = models.IntegerField()
    avatar = models.ImageField()

  
