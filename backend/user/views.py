from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_400_BAD_REQUEST
@api_view(['POST'])
def create_user(request):
    pass
@api_view(['DELETE'])
def delete_user(request):
    try:
        request.user.delete()
        return Response(
            'Account Deleted Successfully',
            status=HTTP_200_OK
        )
    except Exception as e:
        return Response(
            'Account Deletion Failed',
            status=HTTP_400_BAD_REQUEST
        )
