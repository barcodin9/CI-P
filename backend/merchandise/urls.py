
from django.urls import path 
from merchandise.views import get_all_products

urlpatterns = [
    path('products/', get_all_products, name='all_products'),
]