from django.urls import path 
from . import views
from .views import product_detail

urlpatterns = [
   path('', views.checkout, name='checkout'),
   path('success_checkout/<order_number>', views.success_checkout, name='success_checkout'),
   path('product/<int:id>/', product_detail, name='products_template'),
]
