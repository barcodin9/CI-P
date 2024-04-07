import stripe
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'test.html')

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
            success_url= 'http://localhost:8000',
            cancel_url= 'http://localhost:8000',
        )

        return redirect(checkout_session.url, code=303)