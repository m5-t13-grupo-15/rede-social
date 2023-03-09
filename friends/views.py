from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer
from .serializer import FriendListSerializer
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from .models import FriendList
from users.models import User


class FriendListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        friend_list = FriendList.objects.get(owner=request.user)

        serializer = FriendListSerializer(friend_list)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
