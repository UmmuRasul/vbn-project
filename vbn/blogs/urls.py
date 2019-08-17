from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='blogs-dashboard'),
    path('sub/', views.dashboard, name='blogs-sub'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]