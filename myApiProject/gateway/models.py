from django.db import models
from django.db.models.deletion import CASCADE
from user.models import CustomUser

# Create your models here.
class JWT(models.Model):
    user = models.ForeignKey(CustomUser, related_name="login_user", on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   