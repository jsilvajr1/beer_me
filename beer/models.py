from django.db import models
from django.contrib.auth.models import User


class Beer(models.Model):
    beer_name = models.CharField(max_length=255)
    brewery = models.CharField(max_length=10)
    abv = models.CharField(max_length=10)
    
    def __str__(self):
        return self.beer_name

class Cellar(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name='beer')


class Profile(models.Model):
    cellar = models.ForeignKey(Cellar, on_delete=models.CASCADE, related_name='cellars')
    
