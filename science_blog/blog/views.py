from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView




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
    # fields = '__all__'
    fields = ('title', 'body', 'tags')