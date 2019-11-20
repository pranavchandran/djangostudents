from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=25)




