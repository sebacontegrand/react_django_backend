from django.db import models

# Create your models here.
class Missions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='missions')

class Launches(models.Model):
    name=models.CharField(max_length=100)
    rocket=models.CharField(max_length=100,default='Default Rocket Name')
    youtube=models.URLField(max_length=200)

