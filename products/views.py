from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

##here is where we define our views when user gets to them through urls


def index(request):
    products = Product.objects.all()  # to get all the products in our database
    #return HttpResponse("hello world")
    
    # we use the render function to render a template
    #we say that we want to render our index.html,
    #we pass a dictionaries of key/value pairs to list our produts
    return render(request, "index.html", {"products": products})


def new(request):
    return HttpResponse("New product")
