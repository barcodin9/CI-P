from django.shortcuts import render, get_object_or_404
from .cart import Cart
from decimal import Decimal
from merchandise.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    print("Cart Data:", request.session.get('cart', {})) 
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    total, delivery_cost, grand_total = cart.cart_total()
    return render(request, 'cart_summary.html', {"cart_products":cart_products, "quantities":quantities, 'totals':total, 'delivery_cost':delivery_cost, 'grand_total':grand_total} )

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

        response = JsonResponse({'Product Name': product.name, 'message': 'Item added to cart!'})
        return response
       
        





def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        return response



def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('quantity', 1))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        return response