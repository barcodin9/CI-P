from django.shortcuts import render, get_object_or_404
from .cart import Cart
from merchandise.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, 'cart_summary.html', {"cart_products":cart_products, "quantities":quantities} )

def cart_add(request):
    cart = Cart(request)
    # test POST
    if request.POST.get('action') == 'post':
        #get product related
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('quantity', 1) 

       
        if product_id and product_qty:
            product_id = int(product_id)
            product_qty = int(product_qty)
        else:
            return JsonResponse({'error': 'Product ID or quantity missing'})

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        response = JsonResponse({'Product Name': product.name})
        return response





def cart_delete(request):
    pass

def cart_update(request):
    pass