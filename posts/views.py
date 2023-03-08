from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class PostUniqueView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "post_id"
