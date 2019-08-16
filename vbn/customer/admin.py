from django.contrib import admin
from .models import News, Video, ContactUs
# Register your models here.

admin.site.register(News)
admin.site.register(ContactUs)
admin.site.register(Video)
