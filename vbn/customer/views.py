from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserCustomerRegister, ContactForm 
from .models import News, Video, ContactUs
from django.views.generic import ListView
from blogs.models import Post




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


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'customer/contact_cus.html', {'form': form})
    

    
def news(request):
        daily_news = {
                'news':News.objects.all()
                }
        return render(request, 'customer/news.html', daily_news)

class NewsListView(ListView):
        model = News
        template_name = 'customer/news.html'
        context_object_name = 'news'
        ordering = ['-date']
        paginate_by = 1

def video(request):
        daily_videos = {
                'videos':Video.objects.all()
                }
        return render(request, 'customer/video.html', daily_videos)

def about(request):
    return render(request, 'customer/about.html', {'title':'About'})

def blogs(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'customer/blogs.html', context)


class PostListView(ListView):
        model = Post
        template_name = 'customer/blogs.html'
        context_object_name = 'posts'
        ordering = ['-date_posted']
        paginate_by = 2

