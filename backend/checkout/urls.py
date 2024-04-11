from django.urls import path
from checkout.views import checkout, success, cancel

urlpatterns = [
    path('', checkout, name='merch'),
    path('success_checkout/', success , name='success'),
    path('cancel_checkout/', cancel , name='cancel'),
]