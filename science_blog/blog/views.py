from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, UpdateForm, Category
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'home_v1.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_created']  # ['-id']


    def get_context_data(self, *args, object_list=None, **kwargs):
        categ_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["categ_menu"] = categ_menu
        return context


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
    form_class = UpdateForm
    # fields = ['title', 'body', 'tags', 'title_tag', 'date_updated']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home-sweet-home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories.replace('-', ' '))
    return render(
            request, 'categories.html',
            {'categories': categories.title().replace('-', ' '), 'category_posts': category_posts}
            )


def CategoryListView(request):
    categ_menu_list = Category.objects.all()
    return render(
        request, 'category_list.html', {'categ_menu_list': categ_menu_list}
        )


def custom_datetime_picker(request):
    return render(request, 'custom_datetime_picker.html', {})
