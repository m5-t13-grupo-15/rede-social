# Generated by Django 4.0.7 on 2023-03-09 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollowers',
            fields=[
                ('owner_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='followers', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
