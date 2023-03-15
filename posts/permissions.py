from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import Request, View
from friends.models import FriendList
from posts.models import Post


class IsAccountOrFriend(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        post = get_object_or_404(Post, id=view.kwargs["post_id"])
        print(post.user)

        friend = FriendList.objects.filter(friends=request.user).first()

        return (request.user == post.user) or (request.user and friend)
