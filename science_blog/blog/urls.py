#  Created by btrif Trif on 10-06-2023 , 9:41 PM.
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView



urlpatterns = [

    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home-sweet-home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),

]


