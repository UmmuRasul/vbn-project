from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserCustomerRegister

# Create your views here.


def register_cus(request):
    if request.method == 'POST':
        form = UserCustomerRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Your Account has been created, You can login now')
            return redirect('login')
    else:
        form = UserCustomerRegister()
    return render(request, 'users/register.html', {'form':form})