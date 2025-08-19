from django.urls import path
from user.views import create,delete
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("create/",create,name="create"),
    path("get-token/",obtain_auth_token,name="get-token"),
    path("delete/",delete,name="delete")
]
