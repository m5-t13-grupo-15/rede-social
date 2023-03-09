from django.db import models
import uuid


class RequestTypes(models.TextChoices):
    friend = "friend"
    follower = "follower"


# Create your models here.
class BondRequest(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    receiver = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="received_requests"
    )
    sender = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="sent_requests"
    )
    request_type = models.CharField(max_length=20, choices=RequestTypes.choices)
    sent_at = models.DateTimeField(auto_now=True)
    aproved = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=False, default=True)

    def accept(self):
        if self.request_type == "friend":
            receiver_friends = FriendList.objects.get(owner=self.receiver)
            sender_friends = FriendList.objects.get(owner=self.sender)

            receiver_friends.add_friend(self.sender)
            sender_friends.add_friend(self.receiver)

            self.aproved = True
            self.is_active = False
            self.save()

        elif self.request_type == "follower":
            receiver_friends = FriendList.objects.get(owner=self.receiver)
            sender_friends = FriendList.objects.get(owner=self.sender)

            receiver_friends.add_friend(self.sender)
            sender_friends.add_friend(self.receiver)

            self.aproved = True
            self.is_active = False
            self.save()

    def decline(self):
        self.aproved = False
        self.is_active = False
        self.save()

    def cancel(self):
        self.aproved = False
        self.is_active = False
        self.save()
