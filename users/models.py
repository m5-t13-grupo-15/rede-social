from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email = models.EmailField(max_length=127, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    private = models.BooleanField(null=False, default=False)
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)

    def __str__(self):
        return self.username
