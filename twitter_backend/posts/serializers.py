from rest_framework import serializers
from .models import Post
from users.serializers import UserDisplaySerializer



class PostSerializerGET(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    class Meta:
        model=Post
        fields=['id','content', 'user', 'created_at', 'image']

class PostSerializerGeneral(serializers.ModelSerializer):
    
    class Meta:
        model=Post
        fields=['id','content', 'user', 'created_at', 'image']
        
class PostSerializerDetailed(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    class Meta:
        model=Post
        fields=['id','content', 'user', 'created_at', 'image']
        
    

        