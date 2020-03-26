from django.db import models



class User(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

class Beer(models.Model):
    beer_name = models.CharField(max_length=255)
    brewery = models.CharField(max_length=10)
    abv = models.CharField(max_length=10)
    
    def __str__(self):
        return self.beer_name

class Cellar(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name='beer')


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    cellar = models.ForeignKey(Cellar, on_delete=models.CASCADE, related_name='cellars')
    
