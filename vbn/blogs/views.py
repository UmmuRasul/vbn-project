from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import  Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def dashboard(request):
    return render(request, 'blogs/dashboard.html')

def blogs_sub(request):
    return render(request, 'blogs/blogs_sub.html')

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
        success_url = 'customer/blogs'
        
        def test_func(self):
                post = self.get_object()
                if self.request.user == post.author:
                        return True
                return False
