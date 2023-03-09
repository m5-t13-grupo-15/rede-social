# Generated by Django 4.0.7 on 2023-03-09 00:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('public', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('commented_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
