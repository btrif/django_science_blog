#  Created by btrif Trif on 10-06-2023 , 9:41 PM.
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, \
    UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView



urlpatterns = [

    path('home/', views.home, name="home"),

    path('', HomeView.as_view(), name="home-sweet-home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete-post"),
    path('custom_datetime_picker/', views.custom_datetime_picker, name="custom_datetime_picker"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    path('category/<str:categories>/', CategoryView, name="category"),
    path('category_list/', CategoryListView, name="category-list"),

]


