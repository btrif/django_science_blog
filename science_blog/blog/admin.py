from django.contrib import admin
from .models import Post, Category


# Register your models here.

# access Post from the admin area
admin.site.register(Post)
admin.site.register(Category)
