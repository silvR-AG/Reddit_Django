# Generated by Django 4.0.6 on 2022-07-21 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0004_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]