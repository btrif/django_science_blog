# Generated by Django 4.2.2 on 2023-06-17 19:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]