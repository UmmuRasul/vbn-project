from django.urls import path
from .views import PostListView,PostDetailView
from . import views

urlpatterns = [
    path('', views.dashboard, name='blogs-dashboard'),
    path('about/', views.about, name='blogs-about'),
    path('blogs/', PostListView.as_view(), name='blogs-blogs'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
