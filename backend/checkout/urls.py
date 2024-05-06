from django.urls import path 
from . import views
from .views import product_detail, success_checkout

urlpatterns = [
   path('', views.checkout, name='checkout'),
   path('success_checkout/<str:order_number>/', success_checkout, name='success_checkout'),
   path('product/<int:id>/', product_detail, name='products_template'),
]
