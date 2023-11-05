from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission

from companies.models import Enterprise

class User(AbstractBaseUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
class Group(models.Model):
    name = models.CharField(max_length=85)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

class Group_Permissions(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission  = models.ForeignKey(Permission, on_delete=models.CASCADE)

class User_Groups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)