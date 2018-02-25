from django.db import models

# Create your models here.

class Post(models.Model):
      post_id = models.IntegerField()
      isActive = models.BooleanField(default=True)
      isFunded = models.BooleanField(default=False)
      imageUrl  = models.CharField(max_length=300)
      name  = models.CharField(max_length=300)
      amazonLink  = models.CharField(max_length=300)
      organization  = models.CharField(max_length=300)
      person  = models.CharField(max_length=300)
      address  = models.CharField(max_length=300)
      plea  = models.CharField(max_length=300)
      raisedNano = models.IntegerField()
      raisedUsd = models.FloatField()
      priceNano = models.FloatField()
      priceUsd =  models.FloatField()
      numDonations = models.FloatField()
      timeLeft = models.IntegerField()


class Nano_Address(models.Model):
	imageUrl  = models.CharField(max_length=300)