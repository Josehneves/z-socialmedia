# Generated by Django 4.2.7 on 2023-11-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_app', '0002_tweet_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
