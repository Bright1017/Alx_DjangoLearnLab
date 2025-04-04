from django.db import models
from django.conf import settings
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_post')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_like')
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts_comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_comment')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
