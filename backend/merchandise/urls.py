
from django.urls import path 
from merchandise.views import get_all_products

urlpatterns = [
    path('', get_all_products, name='all_products'),
]