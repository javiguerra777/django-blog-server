from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Post, ProfilePicture
from .serializers import PostSerializer

# Create your views here.
class PostApiView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  # get all posts
  def get(self, request, *args, **kwargs):
    profilePictures = ProfilePicture.objects.all()
    posts = Post.objects.select_related('user').all()
    list = []
    for post in posts:
      listData = {
          'title': post.title,
          'body': post.body,
          'id': post.id,
          'user': {
            'id': post.user.id,
            'username': post.user.username
          }
        }
      for image in profilePictures:
        if image.user.id == post.user.id:
         print(image.image)
         listData['user']['image'] = image.image
      list.append(listData)
    return Response(list, status=status.HTTP_200_OK)
  # create new post
  def post(self, request, *args, **kwargs):
    data = {
      'title': request.data.get('title'),
      'body': request.data.get('body'),
      'user': request.user.id,
    }
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      profilePicture = ProfilePicture.objects.get(user=request.user.id)
      sentData = {
        'title': serializer.data.get('title'),
        'body': serializer.data.get('body'),
        'id': serializer.data.get('id'),
        'user': {
          'id': request.user.id,
          'username': request.user.username,
          'image': profilePicture.image
        }
      }
      return Response(sentData, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailsApiView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  # helper function to get post
  def get_object(self, post_id, user_id):
    try:
      return Post.objects.get(id=post_id, user=user_id)
    except Post.DoesNotExist:
      return None
  # get single post
  def get(self, request, post_id, *args, **kwargs):
    post_instance = self.get_object(post_id, request.user.id)
    if not post_instance:
      return Response({'error': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(post_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)
  # update post
  def put(self, request, post_id, *args, **kwargs):
    post_instance = self.get_object(post_id, request.user.id)
    if not post_instance:
      return Response({'error': 'post does not exist'}, status=status.HTTP_404_NOT_FOUND)
    data = {
      'title': request.data.get('title'),
      'body': request.data.get('body'),
    }
    serializer = PostSerializer(instance=post_instance, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      profilePicture = ProfilePicture.objects.get(user=request.user.id)
      sentData = {
        'title': serializer.data.get('title'),
        'body': serializer.data.get('body'),
        'id': serializer.data.get('id'),
        'user': {
          'id': request.user.id,
          'username': request.user.username,
          'image': profilePicture.image
        }
      }
      return Response(sentData, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  # delete post
  def delete(self, request, post_id, *args, **kwargs):
    post_instance = self.get_object(post_id, request.user.id)
    if not post_instance:
      return Response({'error': 'post not found'}, status=status.HTTP_400_BAD_REQUEST)
    post_instance.delete()
    return Response({'id': post_id}, status=status.HTTP_200_OK)
