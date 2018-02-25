from django.shortcuts import render
import uuid
from django.http import JsonResponse
from rest_api.models import Post, Nano_Address
from django.core import serializers
import urllib.request as urllib2
from amazon.api import AmazonAPI
import json, string

AMAZON_ASSOC_TAG = "silverstat194-20"
AMAZON_SECRET_KEY = "J9rsxoQWYUh8/9mapQEgOBORJG9gszBOlzL5xtc7"
AMAZON_ACCESS_KEY = "AKIAISYHHX6HVKJOGSTQ"
NANO_MARKET = "https://api.coinmarketcap.com/v1/ticker/nano/"



# Create your views here.
def createpost(request):
      string_url = "https://www.amazon.com/FEINZER-Professional-Luxury-Ceramic-Vegetable/dp/B00H7KNFG2/ref=sr_1_1_sspa?ie=UTF8&qid=1519532786&sr=8-1-spons&keywords=knife&psc=1"
      product_id = None
      for e in string_url.split("/"):
            if len(e) == 10:
                  product_id = e
                  break

      amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
      product = amazon.lookup(ItemId=product_id)
      print("USD PRICE")
      print(product.price_and_currency[0])



  #     post = Post(
  #           post_id = str(uuid.uuid4()).replace('-','')[:7].upper(), \
  #           isActive = True, \
		# isFunded = False, \
		# imageUrl  = product.large_image_url, \
  #     	name  = product.title, \
  #     	amazonLink  = request.POST['amazonLink'],\
  #     	organization  = request.POST['organization'], \
  #     	person  = request.POST['person'], \
  #     	address  =  Nano_Address.objects.filter(used=False).first(),\
  #     	plea  = request.POST['plea'], \
  #     	raisedNano = 0, \
  #     	raisedUsd = 0, \
  #     	priceNano = 0, \
  #     	priceUsd =  product.price_and_currency[0], \
  #     	numDonations = 0, \
  #     	timeLeft = request.POST['timeLeft']
  #     )


      post = Post(
            post_id = str(uuid.uuid4()).replace('-','')[:7].upper(), \
            isActive = True, \
            isFunded = False, \
            imageUrl  = product.large_image_url, \
            name  = product.title, \
            amazonLink  = string_url,\
            organization  = "Goowel", \
            person  = "go", \
            address  =  Nano_Address.objects.filter(used=False).first().as_str(), \
            plea  = "rs", \
            raisedNano = 0, \
            raisedUsd = 0, \
            priceNano = 0, \
            priceUsd =  product.price_and_currency[0], \
            numDonations = 0, \
            timeLeft = 100
      )
      post.save()

      return JsonResponse({"status":"200"})


def getposts(request):

      nano_price_usd = get_nano_price()
      posts = []
      for e in Post.objects.all():
            e.priceNano = nano_price_usd
            e.priceNano = nano_price_usd
            e.raisedUsd = nano_price_usd*e.raisedNano
            posts.append(e)

      return JsonResponse([e.as_json() for e in posts], safe=False)


def got_donation(request):
      address_from = request.POST['address_from']
      address_to = request.POST['address_to']
      post_id = request.POST['post_id']
      trans = Transaction(
            address_from=address_from,\
            address_to=address_to,\
            post_id=post_id
            )
      trans.save()
      return JsonResponse({"status":"200"})

def get_nano_price():
      req = urllib2.Request(NANO_MARKET)
      opener = urllib2.build_opener()
      f = opener.open(req)
      json_data = json.loads(f.read().decode('utf-8'))
      nano_price_usd = json_data[0]['price_usd']
      return nano_price_usd

