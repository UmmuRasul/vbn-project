from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ContactUs

class UserCustomerRegister(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class ContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactUs
        fields =  ['email', 'message']
