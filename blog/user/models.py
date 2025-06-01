from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True)
    age = models.CharField(max_length=2)

    def __str__(self):
        return self.username  
