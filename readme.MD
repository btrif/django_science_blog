.LOG

### Start new project

```
(django_sci_venv) D:\workspace\btrif\django_science_blog>django-admin startproject science_blog

```

```
 (django_sci_venv) D:\workspace\btrif\django_science_blog>cd science_blog
```

### Migrate

```
(django_sci_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

### Start Django server
```
(django_sci_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 10, 2023 - 20:51:03
Django version 4.2.2, using settings 'science_blog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Create super user (admin)
```
(django_sci_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py createsuperuser
Username (leave blank to use 'btrif'): admin
Email address: admin@admin.admin
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

```
(django_sci_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

```


```
System check identified no issues (0 silenced).
June 10, 2023 - 20:55:34
Django version 4.2.2, using settings 'science_blog.settings'
Starting development server at http://127.0.0.1:8000/
[10/Jun/2023 20:55:46] "GET /admin/ HTTP/1.1" 302 0
[10/Jun/2023 20:55:46] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4181
[10/Jun/2023 20:55:46] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 2929
[10/Jun/2023 20:55:46] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2694
[10/Jun/2023 20:55:46] "GET /static/admin/css/login.css HTTP/1.1" 200 958
[10/Jun/2023 20:55:46] "GET /static/admin/css/base.css HTTP/1.1" 200 21207
[10/Jun/2023 20:55:46] "GET /static/admin/css/responsive.css HTTP/1.1" 200 18533
[10/Jun/2023 20:55:46] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3063
[10/Jun/2023 20:55:46] "GET /static/admin/js/theme.js HTTP/1.1" 200 1943
[10/Jun/2023 20:55:50] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[10/Jun/2023 20:55:50] "GET /admin/ HTTP/1.1" 200 5556
[10/Jun/2023 20:55:50] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 441
[10/Jun/2023 20:55:50] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[10/Jun/2023 20:55:50] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
```

### Start the blog app
```
(django_sci_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py startapp blog

```

- Everytime we create a new app we will add the app to the settings.py -> INSTALLED_APPS
- Add to the science_blog/urls.py -> these are the main URLS:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),   
]
```

### Write the Model

- and after the Post mode in models.py was written


#### makemigrations - generating the script to modify the DB

This will generate a file in the migrations folder

```
(.science_blog_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Post
```

#### Migrate again

This will execute the previously generate file

```
(.science_blog_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

#### - Create Template HTML File
#### - Create Views
#### - Create URL


### Django Page Creation

- Whenever we create a new page file we need a 3 step process :
1.  a html template File,
2.    A view
3.  an URL

----------------------------------

18.JUN.2023 - 11:34AM

### User Authentication

##### Creating a User authentication for blog - Using a different app

- In Django Everything is an app : the blog website is an app
- We will create a separate app for User Authentication System

```
(.science_blog_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py startapp members
```

- a new folder ( app) called members was created :
- initially it will contain the same files : migrations folder, admin.py, apps.py, mode.py, tests.py, views.py 
- we will add in this folder  a new file urls.py 
- Everytime we create a new app we will add the app to the settings.py -> INSTALLED_APPS
- Also in science_blog/urls.py we must include members.urls : 
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
```

- Why two members urls ?
  - the order is important: Django will use the builtin contrib.auth.urls to handle User Authentication
  - the second url is for other types of pages

- Create members/templates/registration folders
- Start creating templates



### Login & Logout - User Authentication

- Django Framework handles also Login and Logout.
- in settings.py must add a redirect URL :
 ```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```
 
- For the register we must add an url in members :
```
path('register/', UserRegisterView.as_view(), name='register'),
```

- And in views.py must add :
```
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
```

- Django has a function : is_authenticated which help with showing/ not showing
private posts of a specific user.
- first must edit the jinja template from base.html
```
{% if user.is_authenticated %}
{% else %}
{% endif %}
```
- next add same functionality to home.html;
- Finally, and most important protect the update_post.html, add_post.html, delete_post.html
to not allow anonymous update or edit. This is done also by adding:
```
{% if user.is_authenticated %}
{% else %}
{% endif %}
```

## Django Tips

#### Django Homepage post preview

How to display on homepage only snippet (short preview) of the entire blog post
Go in home.html :
```
{{ post.body|slice:":200" }}
{{ post.body|truncatewords:40 }}
```


#### Fix spacing in the Article Detail View

- By default Django escape out html formatting, because of security (injections)
- To set us, article_detail.html & home.html :
```
{{ post.body|safe }}
```
- then add <p> tags within article

#### Slugify categories
- Means that when you have a space ( e.g. coding tutorials) we must add :
```
in home.html
<a href="{% url 'category' post.category|slugify %}">{{ post.category }}</a>  -
in views.py :
category_posts = Post.objects.filter(category=categories.replace('-', ' '))
```


## Categories
- To add categories we must create a new model
- we must modify the form :
```
categories = Category.objects.all().values_list('name', 'name')

'category' : forms.Select(choices=categories),
```