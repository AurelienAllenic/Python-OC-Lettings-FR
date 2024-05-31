from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user', related_query_name='profile_user_query')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
