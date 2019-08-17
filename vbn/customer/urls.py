from django.urls import path
from . import views
from .views import  NewsListView, PostListView

urlpatterns = [
    path('', views.home_cus, name='customer-home'),
    path('about_cus', views.about_cus, name='custmer-about'),
    path('contact_us', views.contact_us, name='custmer-contact'),
    path('news/',  NewsListView.as_view(), name='customer-news'),
    path('video/', views.video, name='customer-video'),
    path('blogs/', views.blogs, name='customer-blogs'),
    path('blogs/', PostListView.as_view(), name='customer-blogs'),
    

]