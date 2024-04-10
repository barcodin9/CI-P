from django.shortcuts import render, get_object_or_404
from .cart import Cart
from merchandise.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, 'cart_summary.html', {"cart_products":cart_products} )

def cart_add(request):
    cart = Cart(request)
    # test POST
    if request.POST.get('action') == 'post':
        #get product related
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        #product in db
        product = get_object_or_404(Product, id=product_id)
        #save to session
        cart.add(product=product, quantity=product_qty)

        #return response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'Product Name: ': product.name})
        return response




def cart_delete(request):
    pass

def cart_update(request):
    pass