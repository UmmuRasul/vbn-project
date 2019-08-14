from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    pass

    class Meta:
        model = Video
        fields = ['title', ' categories', 'content', 'date']