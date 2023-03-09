from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from users.models import User
from .models import BondRequest
from .serializers import BondRequestSerializer
from rest_framework.views import APIView


class BondFriendRequestGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        requests_sent = BondRequest.objects.filter(sender=request.user)
        requests_received = BondRequest.objects.filter(receiver=request.user)

        serializer_sent = BondRequestSerializer(requests_sent, many=True)
        serializer_received = BondRequestSerializer(requests_received, many=True)

        return Response(
            {"sent": serializer_sent.data, "received": serializer_received.data},
            status=status.HTTP_200_OK,
        )


class BondFriendRequestView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, user_id: str) -> Response:
        receiver = User.objects.get(id=user_id)
        sender = request.user

        if receiver == sender:
            return Response({"message": "can't send request to yourself"})

        request_exists = BondRequest.objects.filter(sender=sender, receiver=receiver)
        request_reverse_exists = BondRequest.objects.filter(
            sender=receiver, receiver=sender
        )

        if request_exists:
            serializer = BondRequestSerializer(request_exists[0])
            return Response(
                {"WARNING": "request already existent", "request": serializer.data},
                status=status.HTTP_409_CONFLICT,
            )
        elif request_reverse_exists:
            serializer = BondRequestSerializer(request_reverse_exists[0])
            return Response(
                {
                    "WARNING": "request already existent",
                    "request": serializer.data,
                },
                status=status.HTTP_409_CONFLICT,
            )

        friend_request = BondRequest.objects.create(
            sender=sender, receiver=receiver, request_type="friend"
        )

        serializer = BondRequestSerializer(friend_request)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        requests_sent = BondRequest.objects.filter(sender=request.user)
        requests_received = BondRequest.objects.filter(receiver=request.user)

        return Response(
            {"sent": requests_sent, "received": requests_received},
            status=status.HTTP_200_OK,
        )


class BondFriendRequestDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request, request_id: str, res: str) -> Response:
        bond_request = BondRequest.objects.get(id=request_id)

        if request.user == bond_request.sender:
            if res == "cancel":
                bond_request.cancel()
                return Response({"message": "request canceled"})
            else:
                return Response({"message": "can't accept or decline your own request"})

        if request.user != bond_request.receiver:
            return Response(
                {"message": "this request is not your to respond"},
                status=status.HTTP_200_OK,
            )

        if res == "accept":
            bond_request.accept()
            return Response({"message": "request accepted"}, status=status.HTTP_200_OK)
        elif res == "decline":
            bond_request.decline()
            return Response({"message": "request declined"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "message": "invalid option, please choose between <- accept -> or <- decline -> or <- cancel ->"
                },
                status=status.HTTP_200_OK,
            )
