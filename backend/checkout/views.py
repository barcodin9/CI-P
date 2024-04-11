import stripe
from django.shortcuts import render, redirect
from django.conf import settings

def home(request):
    return render(request, 'index.html')

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1P307yRv8bNUIMLr8Vs5lFLb',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url= 'http://localhost:8000/checkout/success_checkout/',
            cancel_url= 'http://localhost:8000/checkout/cancel_checkout/',
        )

        return redirect(checkout_session.url, code=303)

def success(request):
    return render(request, 'success_checkout.html')
def cancel(request):
    return render(request, 'cancel_checkout.html')