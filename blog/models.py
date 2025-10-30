from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
  title=models.CharField(max_length=200)# -Title of the post
  content=models.TextField()#-content of the post
  author= models.ForeignKey(User, on_delete=models.CASCADE)# -link to user. Author (user relationship)
  created_at= models.DateTimeField(auto_now_add=True)#-Timestamps for creation
  updated_at=models.DateTimeField(auto_now=True)#-Timestamps for updates
   
def __str__ (self):
  return self.title


