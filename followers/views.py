from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from .serializers import BondListSerializer
from .models import FollowersList


# Create your views here.
class FollowerListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = [BondListSerializer]

    def get(self, request: Request) -> Response:
        follower_list = FollowersList.objects.get(owner=request.user)
        serializer = BondListSerializer(follower_list)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
