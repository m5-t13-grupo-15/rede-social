from django.db import models
from users.models import User


class Friends(models.Model):
    owner_id = models.OneToOneField(
        User,
        primary_key=True,
        unique=True,
        on_delete=models.CASCADE,
        related_name="friends",
    )
    friends = models.ManyToManyField("users.User", related_name="user_friends")
