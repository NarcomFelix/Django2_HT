import os
import json

from django.shortcuts import render

from products.models import Product, ProductCategory




def index(request):
    context = {'title': "geekShop"}
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'geekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/products.html', context)
