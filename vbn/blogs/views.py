from django.shortcuts import render
from .models import Post

# Create your views here.


def dashboard(request):
    return render(request, 'blogs/dashboard.html')


def contact(request):
        return render(request, 'blogs/contact.html')

def about(request):
    return render(request, 'blogs/about.html', {'title':'About'})
    
def blogs(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blogs/blogs.html', context)
