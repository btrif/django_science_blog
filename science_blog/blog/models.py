from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="science blog title tag")
    # date_created = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=False, default=datetime.now)
    # date_updated = models.DateTimeField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(default=datetime.now)


    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    tags = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.title}   |    {self.author}"

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)) )
        return reverse('home-sweet-home')
