from django.db import models
from users.models import User


class FollowersList(models.Model):
    owner = models.OneToOneField(
        User,
        primary_key=True,
        unique=True,
        on_delete=models.CASCADE,
        related_name="followers",
    )
    followers = models.ManyToManyField(User, related_name="following")

    def add_follower(self, user):
        if not user in self.followers.all():
            self.followers.add(user)
            self.save()

    def remove_follower(self, user):
        if user in self.followers.all():
            self.followers.remove(user)

    def unfollow(self, user):
        self.remove_follower(user)

    def is_follower(self, user):
        if user in self.followers.all():
            return True
