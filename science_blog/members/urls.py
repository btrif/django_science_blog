#  Created by btrif Trif on 10-06-2023 , 9:41 PM.
from django.urls import path
from .views import UserRegisterView




urlpatterns = [

    path('register/', UserRegisterView.as_view(), name='register'),

]


