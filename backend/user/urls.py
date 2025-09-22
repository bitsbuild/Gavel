from django.urls import path
from user.views import create_user,delete_user
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('create_user/',create_user,name='create_user'),
    path('get_token/',obtain_auth_token,name='get_token'),
    path('delete_user/',delete_user,name='delete_user')
]