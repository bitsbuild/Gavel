from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from user.serializer import UserSerializer
@api_view(['POST'])
def create(request):
    try:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Account Creation Successful",status=HTTP_201_CREATED)
    except Exception as e:
        return Response("Account Creation Failed",status=HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request):
    try:
        request.user.delete()
        return Response("Account Deletion Successful",status=HTTP_200_OK)
    except Exception as e:
        return Response("Account Deletion Failed",status=HTTP_400_BAD_REQUEST)