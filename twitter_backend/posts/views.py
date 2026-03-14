from django.shortcuts import render
from rest_framework import viewsets, generics, authentication, response, status
from .models import Post
from .serializers import *
from users.permissions import isGmailUser, canAddPost
from rest_framework.decorators import action
# Create your views here.


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerGeneral
    authentication_classes =[authentication.BasicAuthentication]
    # permission_classes = [isGmailUser, canAddPost]

    @action(detail=True, methods=['get'])
    # if detail is true that means django expects id in url
    # url format is http://127.0.0.1:8000/api/posts/posts/{id}/{method-name}/
    def like_post(self, request, pk=None):
        post = self.queryset.get(id=pk)
        data ={
            'post_content': post.content,
            'liked':False
        }
        return response.Response(data, status=status.HTTP_200_OK)


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