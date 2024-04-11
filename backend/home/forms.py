from django import forms
from .models import Newsletter

# class SignUpForm(forms.Form):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'email-entry2'}))

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']