from django.db import models
from django.contrib.auth.models import User

class keyid(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    keys= models.CharField(max_length=5)

    def __str__(self):
        return self.user.username
