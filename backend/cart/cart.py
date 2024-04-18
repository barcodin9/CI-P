from merchandise.models import Product
from decimal import Decimal
from django.http import JsonResponse
from django.conf import settings



class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('cart', {})

        if 'cart' not in self.session:
            self.session['cart'] = {}
        self.cart = self.session['cart']

        # ensure cart on all site pages
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        #logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
        #look up db products
        products = Product.objects.filter(id__in=product_ids)
        #return
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty

        self.session.modified = True
        response = JsonResponse({'message': 'Cart updated..'})
        return response
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
    
    def calculate_delivery(total):
        return total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    
    def grand_total(delivery_cost, total):
        return total + delivery_cost


    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.price * value)
        total = Decimal(total)
        delivery_cost = Cart.calculate_delivery(total)
        grand_total = Cart.grand_total(delivery_cost, total)
        return total, delivery_cost, grand_total
    