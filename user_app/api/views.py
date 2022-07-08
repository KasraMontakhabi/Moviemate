from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from user_app.api.serializers import RegisterationSerializer
from user_app import models


@api_view(["POST"])
def logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def registration_view(request):

    if request.method == "POST":
        serializer = RegisterationSerializer(data=request.data)

        data = {}  # initialize data

        if serializer.is_valid():

            account = serializer.save()  # save taccount

            data["response"] = "Registration successful"  # saving to data
            data["username"] = account.username   # saving to data
            data["email"] = account.email   # saving to data

            # getting token that is automatically generated in models
            token = Token.objects.get(user=account).key
            data["token"] = token  # saving to data

        else:
            serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)
