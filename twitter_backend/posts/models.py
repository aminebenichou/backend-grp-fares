from django.db import models
from users.models import customuser
# Create your models here.
class Post(models.Model):
    content=models.TextField(default='')
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    user = models.ForeignKey(customuser, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="assets/", null=True, blank=True)