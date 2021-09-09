import os
import json

from django.shortcuts import render

from products.models import Product, ProductCategory




def index(request):
    context = {'title': "geekShop"}
    return render(request, 'products/index.html', context)

def products(request, category_id=None):
    context = {'title': 'geekShop - Каталог', 'categories': ProductCategory.objects.all(),}
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    context['products'] = products
    return render(request, 'products/products.html', context)
