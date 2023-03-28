from cmath import atan
from turtle import title
from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  content = models.TextField()
  email = models.EmailField(max_length=100, null=True)
  upload = models.FileField(upload_to='uploads/',null=True)

  def __str__(self):
    return self.title

  def summary(self):
    return self.content[:100]