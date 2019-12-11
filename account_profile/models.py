from django.db import models
from django.utils import timezone

class Account_profile(models.Model):
	account_name = models.CharField(max_length = 50)
	account_surname = models.CharField(max_length = 50)
	login = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	account_create_date = models.DateTimeField(default = timezone.now())
	account_pic = models.CharField(default="../main/profile_icon.png", max_length = 250)

	def __str__(self):
		return (self.account_name + ' ' +self.account_surname )