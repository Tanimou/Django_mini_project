from django.urls import path
from . import views##we need to import views

##here is where we mapping our views to urls using path
urlpatterns=[
    
    path("", views.index),## we leve a blank string to say that index will be the main page, the products page. the path will be "127.0.0.1:8000/products"
    path("new",views.new),##we add a new path to the views.new so when user go to 127.0.0.1:8000/new the views.new function will be executed
]

