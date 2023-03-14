from .models import BondRequest
from rest_framework.views import Response, status
from .serializers import BondFriendRequestSerializer


def check_if_exists(sender, receiver):
    if receiver == sender:
        return Response({"message": "can't send request to yourself"})

    request_exists = BondFriendRequestSerializer.objects.filter(
        sender=sender, receiver=receiver
    )
    request_reverse_exists = BondFriendRequestSerializer.objects.filter(
        sender=receiver, receiver=sender
    )

    if request_exists:
        serializer = BondFriendRequestSerializer(request_exists[0])
        return Response(
            {"WARNING": "request already existent", "request": serializer.data},
            status=status.HTTP_409_CONFLICT,
        )
    elif request_reverse_exists:
        serializer = BondFriendRequestSerializer(request_reverse_exists[0])
        return Response(
            {
                "WARNING": "request already existent",
                "request": serializer.data,
            },
            status=status.HTTP_409_CONFLICT,
        )
