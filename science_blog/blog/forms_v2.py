#  Created by btrif Trif on 15-06-2023 , 4:28 PM.
from datetime import datetime
from django.utils import timezone
from django import forms
from .models import Post, Category

# choices = [('science', 'science'),('self development', 'self development'),('coding', 'coding')]
categories = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'tags', 'category', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'This is title Placeholder'}),
            'tags' : forms.TextInput(attrs={'class' : 'form-control'}),
            'category' : forms.Select(choices=categories, attrs={'class' : 'form-control'}),
            'author' : forms.Select(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'tags', 'category', 'body', 'date_updated')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'This is title Placeholder'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'tags' : forms.TextInput(attrs={'class' : 'form-control'}),
            'category' : forms.Select(choices=categories, attrs={'class' : 'form-control'}),
            'date_updated': forms.DateTimeInput(attrs={'type': 'datetime-local', 'placeholder' : timezone.now().strftime('%Y') }),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),

            }

