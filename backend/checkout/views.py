from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from merchandise.models import Product 


def checkout(request):
    cart = request.session.get('cart', {})
    print("Debug - Cart Contents:", cart)
    
    if not cart:
        messages.error(request, "There's currently nothing in your basket.")
        return redirect('merch')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            # Process payment and order here (pseudo-code)
            # clear the session cart after payment
            request.session['cart'] = {}
            messages.success(request, "Thank you for your order.")
            return redirect('success_checkout') 
    else:
        order_form = OrderForm()

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    cart_products = [
        {'product': product, 'quantity': cart[str(product.id)], 'subtotal': product.price * cart[str(product.id)]}
        for product in products
    ]
    
    subtotal = sum(Decimal(item['subtotal']) for item in cart_products)
    delivery_cost = subtotal * Decimal('0.10')
    grand_total = subtotal + delivery_cost

    context = {
        'order_form': order_form,
        'cart_products': cart_products,
        'subtotal': subtotal,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total
    }

    return render(request, 'checkout/checkout.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})

