from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from .models import ProfilePicture, Post
from .serializers import ProfilePictureSerializer, UserSerializer, PostSerializer

# update profile picture or create new profile picture
class ProfilePictureApiView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  # helper function to obtain profile picture
  def get_object(self, user_id):
    try:
      return ProfilePicture.objects.get(user=user_id)
    except ProfilePicture.DoesNotExist:
      return None
  # get profile picture
  def get(self, request, *args, **kwargs):
    profile_picture_instance = self.get_object(request.user.id)
    if not profile_picture_instance:
      return Response({'error': 'Profile Picture does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProfilePictureSerializer(profile_picture_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)
  # create new profile picture
  def post(self, request, *args, **kwargs):
    data = {
      'user': request.user.id,
      'image': request.data.get('image')
    }
    serializer = ProfilePictureSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  # update profile picture
  def patch(self, request, *args, **kwargs):
    profile_picture_instance = self.get_object(request.user.id)
    if not profile_picture_instance:
      return Response({'error': 'Profile Picture does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    data = {
      'image': request.data.get('image'),
    }
    serializer = ProfilePictureSerializer(instance=profile_picture_instance, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# get user information from database
class UserInfoApiView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  # helper function to get user
  def get_object(self, user_id):
    try:
      return User.objects.get(id=user_id)
    except User.DoesNotExist:
      return None

  # get authenticated users information
  def get(self, request, *args, **kwargs):
    user_instance = self.get_object(request.user.id)
    if not user_instance:
      return Response({'error': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

# get posts related to user
class UserPostsApiView(APIView):
  [permissions.IsAuthenticated]

  def get(self, request, *args, **kwargs):
    posts = Post.objects.filter(user=request.user.id)
    print(posts)
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)