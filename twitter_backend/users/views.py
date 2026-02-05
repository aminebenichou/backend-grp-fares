from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import customuser
from .serilizers import ListUsersSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def ListUsersView(request):
    users = customuser.objects.all()

    serializer = ListUsersSerializer(users, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

