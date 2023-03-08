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
    aproved = models.BooleanField(null=True)
