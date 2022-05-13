from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 256)
    description = models.CharField(max_length = 256)
    def __str__(self):
        return f'{self.name}'