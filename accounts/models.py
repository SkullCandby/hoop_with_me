from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    useR = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    is_email_verified = models.BooleanField(default=True, null=True)
    image = models.ImageField(upload_to="C:/Users/dvmes/PycharmProjects/hoop with me/accounts/profile_pictures", blank=True, null=True)
    def __str__(self):
        return self.useR