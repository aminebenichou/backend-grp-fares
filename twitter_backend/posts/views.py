from django.shortcuts import render
from rest_framework import viewsets, generics, authentication
from .models import Post
from .serializers import *
from users.permissions import isGmailUser, canAddPost
# Create your views here.


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerGeneral
    authentication_classes =[authentication.BasicAuthentication]
    permission_classes = [isGmailUser, canAddPost]


class PostsGenericView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerGeneral

class PostsGenericViewGET(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerGET

class PostsUpdateGenericView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerDetailed
class PostsDeleteGenericView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerDetailed