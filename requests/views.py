from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from .serializers import BondRequestSerializer
from followers.models import FollowersList
from rest_framework.views import APIView
from .validations import check_if_exists
from .models import BondRequest
from users.models import User


class BondRequestGetView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        requests_sent_friend = BondRequest.objects.filter(
            sender=request.user, request_type="friend"
        )
        requests_received_friend = BondRequest.objects.filter(
            receiver=request.user, request_type="friend"
        )
        requests_sent_follower = BondRequest.objects.filter(
            sender=request.user, request_type="follower"
        )
        requests_received_follower = BondRequest.objects.filter(
            receiver=request.user, request_type="follower"
        )

        serializer_sent_friend = BondRequestSerializer(requests_sent_friend, many=True)
        serializer_received_friend = BondRequestSerializer(
            requests_received_friend, many=True
        )
        serializer_sent_follower = BondRequestSerializer(
            requests_sent_follower, many=True
        )
        serializer_received_follower = BondRequestSerializer(
            requests_received_follower, many=True
        )

        return Response(
            {
                "friend_requests": {
                    "sent": serializer_sent_friend.data,
                    "received": serializer_received_friend.data,
                },
                "follower_requests": {
                    "sent": serializer_sent_follower.data,
                    "received": serializer_received_follower.data,
                },
            },
            status=status.HTTP_200_OK,
        )


class BondFriendRequestView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, user_id: str) -> Response:
        receiver = User.objects.get(id=user_id)
        sender = request.user

        validation = check_if_exists(sender, receiver)

        if validation:
            return validation

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


class BondRequestDetail(APIView):
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


class BondFollowerRequestView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, user_id: str) -> Response:
        receiver = User.objects.get(id=user_id)
        sender = request.user

        if not receiver.private:
            receiver_follower_list = FollowersList.objects.get(owner=receiver)
            is_follower = receiver_follower_list.is_follower(sender)
            if is_follower:
                return Response(
                    {"WARNIG": "you alredy follow this user"},
                    status=status.HTTP_409_CONFLICT,
                )
            receiver_follower_list.add_follower(sender)
            return Response({"message": "following user"})
        elif receiver.private:
            validation = check_if_exists(sender, receiver)

            if validation:
                return validation

            follower_request = BondRequest.objects.create(
                sender=sender, receiver=receiver, request_type="follower"
            )

            serializer = BondRequestSerializer(follower_request)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
