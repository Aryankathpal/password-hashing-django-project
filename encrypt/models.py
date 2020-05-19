from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from accounts.models import keyid
# Create your models here.
class encoded(models.Model):
    hasher=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    name=models.CharField(max_length=50)
    date=models.DateTimeField(default=now,blank=True)
    password = models.CharField(max_length=50)
    enc = models.CharField(max_length=100)

    def __str__(self):
        return self.hasher.username

    def date_mod(self):
        return self.date.strftime('%b %e %Y')
