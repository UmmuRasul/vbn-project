from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserCustomerRegister, ContactUs

# Create your views here.


def register_cus(request):
    if request.method == 'POST':
        form = UserCustomerRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Your Account has been created, You can login now')
            return redirect('login_cus')
    else:
        form = UserCustomerRegister()
    return render(request, 'customer/register_cus.html', {'form':form})

def home_cus(request):
    return render(request,'customer/home_cus.html')



def about_cus(request):
    return render(request,'customer/about_cus.html')

def contact_cus(request):
    def contact_us(request):
        if request.method == 'POST':
            form = ContactUs(request.POST)
            if form.is_valid():
                # send email code goes here
                return HttpResponse('Thanks for contacting us!')
        else:
            form = ContactUs()
    return render(request, 'customer/contact_cus.html', {'form': form})