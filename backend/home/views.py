from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import NewsletterForm

# Create your views here.
def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter_signup/')
    else:
        form = NewsletterForm()
    return render(request, 'newsletter.html', {'form': form})