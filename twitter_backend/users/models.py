from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class customuser(AbstractUser):
    phone=models.CharField(max_length=13)
    email=models.EmailField(default='')


    # USERNAME_FIELD=phone

    # user_permissions= 

    def __str__(self):
        return self.phone