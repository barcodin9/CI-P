from django.shortcuts import render
from merchandise.models import Product


# Create your views here.

def get_all_products(request):
    products = Product.objects.all()
    return render(request, 'merch.html', {'products': products})
    
