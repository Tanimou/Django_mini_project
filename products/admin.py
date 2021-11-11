from django.contrib import admin
# we need to import our Product class from models
from .models import Product, Offer

##this is to provide all functionnalities so we can manage our models in the admin area


class ProductAdmin(admin.ModelAdmin):
    # this is how the product page in the admin area will be displayed when we manage products
    list_display = ("name", "price", "stock")
    ##so new product will be displayed with 3 columns name, price and stock


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


##to manage our products in the admin page area
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
# Register your models here.
