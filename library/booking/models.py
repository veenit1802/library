from django.db import models

# Create your models here.
class bookde(models.Model):   
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    avail=models.CharField(max_length=7)