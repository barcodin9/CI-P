from .cart import Cart

# track cart on all relevant pages

def cart(request):
    return {'cart': Cart(request)}