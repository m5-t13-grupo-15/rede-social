from django.db import models
from users.models import User


class FriendList(models.Model):
    owner = models.OneToOneField(
        "users.User",
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="owner",
    )
    friends = models.ManyToManyField("users.User", related_name="friends", blank=True)

    def add_friend(self, user):
        if not user in self.friends.all():
            self.friends.add(user)
            self.save()

    def remove_friend(self, user):
        if user in self.friends.all():
            self.friends.remove(user)
            self.save()

    def unfriend(self, user_to_remove):
        remover_friends = self
        remover_friends.remove_friend(user_to_remove)

        user_to_remove_friends = FriendList.objects.get(owner=user_to_remove)
        user_to_remove_friends.remove_friend(self.owner)
