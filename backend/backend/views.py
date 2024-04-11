from django.shortcuts import render, redirect
from django.conf import settings




# Create your views here.
def home(request):
    return render(request, 'index.html')

