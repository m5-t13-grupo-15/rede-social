from django.db import models


class Post(models.Model):
    owner_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    public = models.BooleanField()
    likes = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts_liked"
    )
