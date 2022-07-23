# Generated by Django 4.0.6 on 2022-07-22 09:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0006_posts_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='unlikes',
            field=models.ManyToManyField(related_name='blog_unlike', to=settings.AUTH_USER_MODEL),
        ),
    ]