from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='blogs-dashboard'),
    path('about/', views.about, name='blogs-about'),
    path('contact/', views.contact, name='blogs-contact'),
    path('blogs/', views.blogs, name='blogs-blogs'),
]
