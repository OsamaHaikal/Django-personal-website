from django.db import models
from OsamaHaikal import settings
from django.contrib.auth.models import User 


class Skill(models.Model):
    title =models.CharField(max_length=100)
    Percentage = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Portfolio(models.Model):
    category =models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)

    image = models.ImageField(upload_to='portfolio/images/')
    btn=models.CharField(max_length=100)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title

 

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    message = models.TextField(max_length=350)

      
