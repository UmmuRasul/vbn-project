from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_cus, name='customer-home'),
    path('about_cus', views.about_cus, name='custmer-about'),
    path('contact_cus', views.about_cus, name='custmer-contact'),

]