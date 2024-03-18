from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, null=True)







    def __str__(self):
        return self.description
