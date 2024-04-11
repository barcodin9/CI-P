
from django.urls import path, include
from merchandise.views import get_all_products, merchandise

urlpatterns = [
    path('', get_all_products, name='all_products'),
    path('', merchandise, name='merch'),
    path('cart/', include('cart.urls')),    
]