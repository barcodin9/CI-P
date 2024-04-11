from django.shortcuts import render
from merchandise.models import Product
from django.contrib.auth.decorators import login_required



# Create your views here.

def get_all_products(request):
    products = Product.objects.all()
    return render(request, 'merch.html', {'products': products})

@login_required
def merchandise(request):
    return render(request, 'merch.html')
    
