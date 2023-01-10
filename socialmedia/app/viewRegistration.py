from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from knox.models import AuthToken
from .serializers import RegisterSerializer, ProfilePictureSerializer

class SignUpApiView(APIView):
  def post(self, request, *args, **kwargs):
    data = {
      'username': request.data.get('username').lower(),
      'email': request.data.get('email').lower(),
      'password': request.data.get('password'),
       }
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
      user = User.objects.create_user(
        data.get('username'),
        data.get('email'),
        data.get('password')
      )
      new_data = {
        'image': request.data.get('image'),
        'user': user.id
      }
      token = AuthToken.objects.create(user)
      profile_pic_serializer = ProfilePictureSerializer(data=new_data)
      if profile_pic_serializer.is_valid():
        profile_pic_serializer.save()
        return Response({'token': token[1]}, status=status.HTTP_200_OK)
      return Response({
        'warning': 'unable to create profile picture',
        'token': token[1
        ]}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(APIView):
  def post(self, request, *args, **kwargs):
    data = {
      'username': request.data.get('username').lower(),
      'password': request.data.get('password')
    }
    # checks if username and password are valid
    user = authenticate(username=data.get('username'), password=data.get('password'))
    # if user is unable to login then throw an error
    if not user:
      return Response({'error': 'user login failed, check username or password'}, status=status.HTTP_400_BAD_REQUEST)
    # if user is able to login then create a token and send it to client
    token = AuthToken.objects.create(user)
    return Response({'token': token[1]}, status=status.HTTP_201_CREATED)
