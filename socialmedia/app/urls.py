from django.urls import path
from .viewPost import PostApiView, PostDetailsApiView
from .viewRegistration import SignUpApiView, LoginApiView
from .viewUser import ProfilePictureApiView, UserInfoApiView, UserPostsApiView

urlpatterns = [
  path('posts', PostApiView.as_view()),
  path('post/<int:post_id>', PostDetailsApiView.as_view()),
  path('signup', SignUpApiView.as_view()),
  path('login', LoginApiView.as_view()),
  path('profile_picture', ProfilePictureApiView.as_view()),
  path('user', UserInfoApiView.as_view()),
  path('user_post', UserPostsApiView.as_view())
]