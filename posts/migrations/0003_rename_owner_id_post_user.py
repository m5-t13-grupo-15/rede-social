# Generated by Django 4.0.7 on 2023-03-08 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_likes_post_owner_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner_id',
            new_name='user',
        ),
    ]