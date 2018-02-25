from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def createpost(request):
	return JsonResponse({'foo':'bar'})


def getposts(request):
	return JsonResponse({'foo':'bar'})


def got_donation(request):
	return JsonResponse({'foo':'bar'})
