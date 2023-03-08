from django.contrib import admin
from .views import FriendListView
from requests.views import (
    BondFriendRequestView,
    BondFriendRequestDetail,
    BondFriendRequestGetView,
)
from django.urls import path, include


urlpatterns = [
    path("friends/", FriendListView.as_view()),
    path("friends/requests/", BondFriendRequestGetView.as_view()),
    path("friends/requests/<str:user_id>/", BondFriendRequestView.as_view()),
    path(
        "friends/requests_res/<str:request_id>/<str:res>/",
        BondFriendRequestDetail.as_view(),
    ),
]
