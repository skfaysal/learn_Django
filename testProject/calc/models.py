from django.db import models

# Create your models here.
class Diseases(models.Model):
    num1=models.CharField(max_length=100)
    num2=models.CharField(max_length=100)


