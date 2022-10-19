from django.db import models
from profiles.models import Profile

 
class Post(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    image_url = models.CharField(max_length=255, default='https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['created_at']

    def __str__(self):
        return self.title



# TODO: create and run migrations
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author')
    body = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['created_at']

    def __str__(self):
        return self.body