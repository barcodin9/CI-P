
from django.urls import path 
from merchandise.views import get_all_products, merchandise

urlpatterns = [
    path('merch/', get_all_products, name='all_products'),
    path('merch/', merchandise, name='merch'),
]