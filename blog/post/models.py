from django.db import models
from user.models import CustomUser



class Post(models.Model):
    class statusPost(models.TextChoices):
        draft = 'draft' , 'DRAFT'
        published = 'published' , 'PUBLISHED'


    title = models.CharField( max_length=50)
    content = models.TextField()
    image = models.ImageField( upload_to='post_images/', null=True, blank=True)
    user = models.ForeignKey(CustomUser,  on_delete=models.CASCADE , related_name='posts')
    status = models.CharField(max_length=10 , choices = statusPost.choices ,default=statusPost.draft)

    def __str__(self):
        return self.title
    