import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="awesome title")
    created_time = models.DateTimeField(datetime.datetime.now())
    modified_time = models.DateTimeField(datetime.datetime.now(), default=datetime.datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    tags = models.CharField(max_length=255, default="")


    def __str__(self):
        return f"{self.title}   |    {self.author}"
