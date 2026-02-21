from rest_framework.decorators import api_view
from .models import customuser
from .serilizers import ListUsersSerializer, groupSerializer, permissionSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.models import Group, Permission
# Create your views here.


# @api_view(['GET'])
# def ListUsersView(request):
#     users = customuser.objects.all()

#     serializer = ListUsersSerializer(users, many=True)

#     return Response(serializer.data, status=status.HTTP_200_OK)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = customuser.objects.all()
    serializer_class = ListUsersSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = groupSerializer

class PermissionsViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = permissionSerializer