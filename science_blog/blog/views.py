from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


from blog.models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


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






