from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User, PermissionsMixin

class User(User, PermissionsMixin):
    def __str(self):
        return "@{}".format(self.username)