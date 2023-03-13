from django.urls import path, include
from bond_requests.views import BondRequestGetView


urlpatterns = [path("requests/", BondRequestGetView.as_view())]
