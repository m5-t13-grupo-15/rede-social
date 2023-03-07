from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        ...

    def post(self, request, pk):
        ...

    def patch(self, request, pk):
        ...

    def delete(self, request, pk):
        ...
