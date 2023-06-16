from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_time']        # ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    # fields = '__all__'
    # fields = ['title', 'body', 'tags']


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    # fields = ['title', 'body', 'tags', 'title_tag', 'modified_time']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home-sweet-home')
