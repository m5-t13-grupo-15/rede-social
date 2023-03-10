from .views import FollowerListView
from requests.views import BondFollowerRequestView, BondRequestDetail
from django.urls import path


urlpatterns = [
    path("followers/", FollowerListView.as_view()),
    path("followers/new_request/<str:user_id>/", BondFollowerRequestView.as_view()),
    path(
        "followers/request_res/<str:request_id>/<str:res>/", BondRequestDetail.as_view()
    ),
]
