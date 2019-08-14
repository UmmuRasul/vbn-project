from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCustomerRegister

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