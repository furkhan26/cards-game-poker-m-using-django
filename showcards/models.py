from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cards(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='static/images')   
    status = models.IntegerField(null=True, blank=True)
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class TempCards(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='static/images')   
    playedby = models.CharField(max_length=100,blank=True,null=True)
    status = models.IntegerField(null=True, blank=True, default=0)
