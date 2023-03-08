from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("posts/", views.PostView.as_view()),
    path("posts/<int:post_id>/", views.PostUniqueView.as_view()),
    path(
        "posts/<int:post_id>/like/", views.PostUniqueView.as_view({"put": "like_post"})
    ),
    path(
        "posts/<int:post_id>/unlike/",
        views.PostUniqueView.as_view({"put": "unlike_post"}),
    ),
]
