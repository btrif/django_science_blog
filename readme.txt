.LOG

(django_sci_venv) D:\workspace\btrif\django_science_blog>django-admin startproject science_blog

 (django_sci_venv) D:\workspace\btrif\django_science_blog>cd science_blog

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

(django_sci_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 10, 2023 - 20:51:03
Django version 4.2.2, using settings 'science_blog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


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

(django_sci_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...





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


(django_sci_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py startapp blog


######## After the Post in models


(.science_blog_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Post

(.science_blog_venv) D:\workspace\btrif\django_science_blog\science_blog>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK


### Django Page Creation

- Whenever we create a new page file we need a 3 step process :
1. a html template File,
2. A view
3. an URL
