from django.shortcuts import render
from .models import Post, News, Video
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def dashboard(request):
    return render(request, 'blogs/dashboard.html')


def contact(request):
        return render(request, 'blogs/contact.html')

def news(request):
        daily_news = {
                'news':News.objects.all()
                }
        return render(request, 'blogs/news.html', daily_news)

def video(request):
        daily_videos = {
                'videos':Video.objects.all()
                }
        return render(request, 'blogs/video.html', daily_videos)

def about(request):
    return render(request, 'blogs/about.html', {'title':'About'})
    
def blogs(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blogs/blogs.html', context)


class PostListView(ListView):
        model = Post
        template_name = 'blogs/blogs.html'
        context_object_name = 'posts'
        ordering = ['-date_posted']
        paginate_by = 2

class PostDetailView(DetailView):
        model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
        model = Post
        fields = ['title', 'content', 'comments']

        def form_valid(self, form):
                form.instance.author = self.request.user
                return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
        model = Post
        fields = ['title', 'content', 'comments']

        def form_valid(self, form):
                form.instance.author = self.request.user
                return super().form_valid(form)

        def test_func(self):
                post = self.get_object()
                if self.request.user == post.author:
                        return True
                return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Post
        success_url = '/blogs'
        
        def test_func(self):
                post = self.get_object()
                if self.request.user == post.author:
                        return True
                return False
        