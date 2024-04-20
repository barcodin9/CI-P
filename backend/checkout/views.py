from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order, OrderLineItem
from merchandise.models import Product 
from cart.context_processor import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    print("Debug - Cart Contents:", cart)
    if not cart:
        messages.error(request, "There's currently nothing in your basket.")
        return redirect('merch')
    
    current_cart = cart_contents(request)
    print("Current cart:", current_cart)
    total = current_cart['grand_total']
    print("Total from cart:", total)

    stripe_total = round(Decimal(total) * 100)

    if stripe_total < 50:  
            messages.error(request, "The total amount must be at least €0.50")

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)


    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.total = total
            order.save()
            # Process payment and order here (pseudo-code)
            # clear the session cart after payment
            request.session['cart'] = {}
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

    if not stripe_public_key:
         messages.warning(request, 'Stripe public key is missing. \ Did you forget to set it in your environment?')


    context = {
        'order_form': order_form,
        'cart_products': cart_products,
        'subtotal': subtotal,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    

    return render(request, 'checkout/checkout.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})

def success_checkout(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/success_checkout.html'
    context = {
        'order': order,
    }

    return render(request, template, context)