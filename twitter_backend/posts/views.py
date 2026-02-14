from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer
# Create your views here.


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

