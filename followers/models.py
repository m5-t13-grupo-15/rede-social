from django.db import models
from users.models import User


class UserFollowers(models.Model):
    owner_id = models.OneToOneField(
        User,
        primary_key=True,
        unique=True,
        on_delete=models.CASCADE,
        related_name="followers",
    )
    followers = models.ManyToManyField(User, related_name="following")
