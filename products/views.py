import os
import json

from django.shortcuts import render
from products.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {'title': "geekShop"}
    return render(request, 'products/index.html', context)

def products(request):
    #file_path = os.path.join(MODULE_DIR, 'fixtures/products.json')
    context = {
        'title': 'geekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/products.html', context)
