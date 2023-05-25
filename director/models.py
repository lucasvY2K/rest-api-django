from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.TextField(max_length=255)
    birth_date = models.DateField()
    nationality = models.TextField(max_length=255)