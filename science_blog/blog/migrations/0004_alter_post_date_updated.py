# Generated by Django 4.2.2 on 2023-06-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_created_time_remove_post_modified_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
