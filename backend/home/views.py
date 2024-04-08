from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def newsletter_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            return redirect('success_url') 
    else:
        form = SignUpForm()
    return render(request, 'your_template.html', {'form': form})