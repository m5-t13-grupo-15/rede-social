from .models import BondRequest
from rest_framework.views import Response, status
from .serializers import BondRequestSerializer


def check_if_exists(sender, receiver):
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
