from django.db import models
import uuid


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    post_id = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="post_comments"
    )
    user_id = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="user_comments"
    )
    content = models.TextField()
    commented_at = models.DateTimeField(auto_now=True)
