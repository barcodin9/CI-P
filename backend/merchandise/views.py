from django.shortcuts import render
from django.http import JsonResponse
from merchandise.models import Product


# Create your views here.

def get_all_products(request):
    products = Product.objects.all().values()
    products_list = list(products) 
    return JsonResponse({'products': products_list})