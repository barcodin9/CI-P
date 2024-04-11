from django.urls import path 
from .views import media

urlpatterns = [
   path('', media, name='media'),
    

]

