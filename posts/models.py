from django.db import models
import uuid
class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts", default=None 
    )
    
    content = models.TextField()
    public = models.BooleanField()
    
    likes = models.ManyToManyField(
        "users.User", related_name="posts_liked"
    )
    
    # comments = models.ManyToManyField(
    #     "users.User",
    #     through="posts.PostComments",
    #     related_name="comments_post",
    # )

class PostComments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="post_comments_user",
    )

    comment_user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_post_comments",
    )
    
    text = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
