from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("posts/", views.PostView.as_view()),
    path("posts/<int:post_id>/", views.PostUniqueView.as_view()),
]
