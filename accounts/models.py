from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Customer(models.Model):
	user = models.OneToOneField(
		User,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name="customer"
	)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name