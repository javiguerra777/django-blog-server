from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, ProfilePicture


class PostSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Post
    fields = ['id', 'title', 'body', 'timestamp', 'user']
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')

class ProfilePictureSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProfilePicture
    fields = ['image']