from django.shortcuts import render
from django.shortcuts import render, redirect, reverse



def checkout(request):
    bag = request.session.get('cart', {})
    if not bag:
        messages.error(request, "There's currently nothing in your basket..")
        return redirect(reverse('merchandise'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)