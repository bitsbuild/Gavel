from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_400_BAD_REQUEST
from user.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def create_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            'Account Created Successfully',
            status=HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {
                'Status':'Account Creation Failed',
                'Error':str(e)
            },
            status=HTTP_400_BAD_REQUEST
        )
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    try:
        request.user.delete()
        return Response(
            'Account Deleted Successfully',
            status=HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                'Status':'Account Deletion Failed',
                'Error':str(e)
            },
            status=HTTP_400_BAD_REQUEST
        )
