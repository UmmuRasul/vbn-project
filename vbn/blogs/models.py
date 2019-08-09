from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

CATEGORIES = [
    ('Health','health'),
    ('Education','edu'),
    ('Sports','sports'),
    ('Politics','politics')
]


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    comments = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class News(models.Model):
    title = models.CharField(max_length=100)
    categories = models.CharField(choices=CATEGORIES, default='Education', max_length=40)
    image = models.ImageField(upload_to='profile_pics')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    editor = models.CharField(max_length=80)

    def __str__(self):
        return self.categories
