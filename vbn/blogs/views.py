from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class PostListView(ListView):
        model = Post
        template_name = 'blogs/blogs.html'
        context_object_name = 'posts'
        ordering = ['-date_posted']

class PostDetailView(DetailView):
        model = Post

class PostCreateView(CreateView):
        pass
 
        model = Post
        fields = ['title', 'content', 'comments']

        def form_valid(self, form):
                form.instance.author = self.request.user
                return super().form_valid(form)