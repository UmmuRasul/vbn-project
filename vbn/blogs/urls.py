from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,  NewsListView
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='blogs-dashboard'),
    path('about/', views.about, name='blogs-about'),
    path('sub/', views.sub, name='blogs-sub'),
    path('news/',  NewsListView.as_view(), name='blogs-news'),
    path('video/', views.video, name='blogs-video'),
    path('blogs/', PostListView.as_view(), name='blogs-blogs'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]