from django.shortcuts import render
import uuid
from django.http import JsonResponse
from rest_api.models import Post, Nano_Address, Transaction
from django.core import serializers
import urllib.request as urllib2
from amazon.api import AmazonAPI
from django.views.decorators.csrf import csrf_exempt
import json, string, time

AMAZON_ASSOC_TAG = "silverstat194-20"
AMAZON_SECRET_KEY = "J9rsxoQWYUh8/9mapQEgOBORJG9gszBOlzL5xtc7"
AMAZON_ACCESS_KEY = "AKIAISYHHX6HVKJOGSTQ"
NANO_MARKET = "https://api.coinmarketcap.com/v1/ticker/nano/"



# Create your views here.
@csrf_exempt
def createpost(request):
      json_dump_obs = json.loads(request.body.decode('utf-8'))
      string_url = json_dump_obs['amazonLink']
      product_id = None
      for e in string_url.split("/"):
            if len(e) == 10:
                  product_id = e
                  break

      amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
      product = amazon.lookup(ItemId=product_id)
      print("USD PRICE")
      print(product.price_and_currency[0])

      wallet =  Nano_Address.objects.first()
      wallet.used = True
      wallet.save()

      post = Post(
            post_id = str(uuid.uuid4()).replace('-','')[:7].upper(), \
            isActive = True, \
		isFunded = False, \
		imageUrl  = product.large_image_url, \
      	name  = product.title, \
      	amazonLink  = string_url,\
      	organization  = json_dump_obs['organization'], \
      	person  = json_dump_obs['person'], \
      	address  =   wallet.address,\
      	plea  = json_dump_obs['plea'], \
      	raisedNano = 0.0, \
      	raisedUsd = 0.0, \
      	priceNano = float(product.price_and_currency[0])/get_nano_price(), \
      	priceUsd =  float(product.price_and_currency[0]), \
      	numDonations = 0, \
      	timeLeft = time.time() + (60*60*7*24)*1000, \
            streetAddress = json_dump_obs['streetAddress'],
      )



      # post = Post(
      #       post_id = str(uuid.uuid4()).replace('-','')[:7].upper(), \
      #       isActive = True, \
      #       isFunded = False, \
      #       imageUrl  = product.large_image_url, \
      #       name  = product.title, \
      #       amazonLink  = string_url,\
      #       organization  = "Goowel", \
      #       person  = "go", \
      #       address  =  wallet.as_str(), \
      #       plea  = "rs", \
      #       raisedNano = 0.0, \
      #       raisedUsd = 0.0, \
      #       priceNano = 0.0, \
      #       priceUsd =  product.price_and_currency[0], \
      #       numDonations = 0.0, \
      #       timeLeft = 100, \
      #       streetAddress = "123 Main",
      # )
      post.save()

      return JsonResponse(post.as_json(), safe=False)

@csrf_exempt
def getposts(request):
      nano_price_usd = get_nano_price()
      posts = []
      for e in Post.objects.all():
            e.priceNano = nano_price_usd
            e.priceNano = nano_price_usd
            e.raisedUsd = nano_price_usd*e.raisedNano
            posts.append(e)

      return JsonResponse([e.as_json() for e in posts], safe=False)

@csrf_exempt
def got_donation(request):
      json_dump_obs = json.loads(request.body.decode('utf-8'))
      address_from = "Placeholder"
      address_to = json_dump_obs['to']
      address_to = json_dump_obs['amount']
      post_id = json_dump_obs['token']
      trans = Transaction(
            address_from=address_from,\
            address_to=address_to,\
            post_id=post_id
            )

      post = Post.objects.filter(post_id=post_id).first()
      post.raisedNano += json_dump_obs['amount']
      post.raisedUsd += post.raisedNano*get_nano_price()
      post.numDonations += 1

      if post.raisedUsd >= priceNano*get_nano_price():
            post.isFunded = True
            post.isActive = False

      post.save()
      trans.save()
      return JsonResponse({"status":"200"})

@csrf_exempt
def dump(request):
      all_post_to_dump = Post.objects.filter(dumped=False).filter(isFunded=True).all()

      for p in all_post_to_dump:
            p.dumped = True
            p.save()
     
      all_post_to_dump_json = json.loads(str([e.as_dump() for e in all_post_to_dump]).replace("'", "\""))
      

      for p in all_post_to_dump_json:
            p['transactions'] = [e.as_json() for e in Transaction.objects.filter(post_id=p['post_id']).all()]

      return JsonResponse(all_post_to_dump_json, safe=False)


def get_nano_price():
      req = urllib2.Request(NANO_MARKET)
      opener = urllib2.build_opener()
      f = opener.open(req)
      json_data = json.loads(f.read().decode('utf-8'))
      nano_price_usd = json_data[0]['price_usd']
      return float(nano_price_usd)


