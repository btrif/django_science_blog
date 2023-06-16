#  Created by btrif Trif on 15-06-2023 , 4:28 PM.
import datetime

from django import forms
from .models import Post




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'tags', 'body', 'date_updated')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'This is title Placeholder'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            'tags' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.Select(attrs={'class' : 'form-control'}),
            'date_updated': forms.DateTimeInput({'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),

            }