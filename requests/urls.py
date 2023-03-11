from django.urls import path, include
from requests.views import BondRequestGetView


urlpatterns = [path("requests/", BondRequestGetView.as_view())]
