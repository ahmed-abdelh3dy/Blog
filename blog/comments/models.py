from django.db import models
from user.models import CustomUser
from post.models import Post



class Comments(models.Model):
    user = models.ForeignKey(CustomUser , on_delete = models.CASCADE , related_name='user_comments')
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    content = models.TextField()


    def __str__(self):
        return self.content
    