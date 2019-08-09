from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', views.dashboard, name='blogs-dashboard'),
    path('about/', views.about, name='blogs-about'),
    path('news/', views.news, name='blogs-news'),
    path('video/', views.video, name='blogs-video'),
    path('blogs/', PostListView.as_view(), name='blogs-blogs'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]