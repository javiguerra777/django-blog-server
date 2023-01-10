from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfilePicture(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
  image = models.URLField(max_length=253)

  def __str__(self):
    return self.image

class Post(models.Model):
  title = models.CharField(max_length = 15)
  body = models.CharField(max_length = 255)
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
  user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)

  def __str__(self):
    return self.body
