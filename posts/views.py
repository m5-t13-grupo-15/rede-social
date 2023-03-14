from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from followers.models import FollowersList
from friends.models import FriendList

from posts.permissions import IsAccountOrFriend
from users.models import User
from .models import Post, PostComments
from .serializers import PostCommentsSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q


class PostView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class PostTimeLineView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id)
        print(user)
        user_follow = user.following.all().values_list("owner")
        friends_list = FriendList.objects.get(owner = self.request.user)
        friends = friends_list.friends.all()
        posts_friends = Post.objects.filter(Q(user__in=friends) | Q(user__in=user_follow))

        return posts_friends


class PostUniqueView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "post_id"

    def like_post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.likes.add(request.user)

    def unlike_post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.likes.remove(request.user)

    def put(self, request, *args, **kwargs):
        if request.data.get("action") == "like":
            return self.like_post(request, *args, **kwargs)
        elif request.data.get("action") == "unlike":
            return self.unlike_post(request, *args, **kwargs)
        else:
            return super().put(request, *args, **kwargs)


class PostCommentCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOrFriend]

    queryset = PostComments.objects.all()
    serializer_class = PostCommentsSerializer
    lookup_url_kwarg = "post_id"

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        serializer.save(comment_user=self.request.user, post=post)


class PostCommentDestroy(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = PostComments.objects.all()
    serializer_class = PostCommentsSerializer
    lookup_url_kwarg = "comment_id"
