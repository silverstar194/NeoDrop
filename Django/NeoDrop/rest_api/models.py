from django.db import models

# Create your models here.

class Post(models.Model):
      post_id = models.CharField(max_length=10)
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

      def as_json(self):
        return dict(
            post_id =self.post_id, 
            isActive=self.isActive,
            isFunded=self.isFunded,
            imageUrl=self.imageUrl,
            name =self.name,
            amazonLink = self.amazonLink,
            organization = self.organization,
            person = self.person,
            address = self.address,
            plea = self.plea,
            raisedNano = self.raisedNano,
            raisedUsd = self.raisedUsd,
            priceNano= self.priceNano,
            numDonations = self.numDonations,
            timeLeft = self.timeLeft,
            )

class Nano_Address(models.Model):
	address  = models.CharField(max_length=300)
	used = models.BooleanField(default=False)

	def as_str(self):
		return str(self.address)

class Transaction(models.Model):
	address_from  = models.CharField(max_length=300)
	address_to  = models.CharField(max_length=300)
	post_id  = models.CharField(max_length=300)


