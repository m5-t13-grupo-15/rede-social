from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts", default=None 
    )
    
    content = models.TextField()
    public = models.BooleanField()
    
    likes = models.ManyToManyField(
        "users.User", related_name="posts_liked"
    )
