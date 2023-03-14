from .views import FriendListView
from bond_requests.views import (
    BondFriendRequestView,
    BondRequestDetail,
)
from django.urls import path


urlpatterns = [
    path("friends/", FriendListView.as_view()),
    path("friends/new_requests/<str:user_id>/", BondFriendRequestView.as_view()),
    path(
        "friends/requests_res/<str:request_id>/<str:res>/",
        BondRequestDetail.as_view(),
    ),
]
