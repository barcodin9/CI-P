from merchandise.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # ensure cart on all site pages
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        #logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def __len___(self):
        return len(self.cart)
    
    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
       #look up db products
        products = Product.objects.filter(id__in=product_ids)
        #return
        return products