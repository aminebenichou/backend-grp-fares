from django.shortcuts import render
from rest_framework import viewsets, generics, authentication
from .models import Post
from .serializers import PostSerializer
from users.permissions import isGmailUser, canAddPost
# Create your views here.


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes =[authentication.BasicAuthentication]
    permission_classes = [isGmailUser, canAddPost]

