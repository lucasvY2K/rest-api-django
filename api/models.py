from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    length = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title
