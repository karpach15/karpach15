from django.db import models

class Drivers(models.Model):
	STATUS_CHOICES = [('True', 'True'), ('False', 'False')]

	name = models.CharField(max_length = 30)
	surname = models.CharField(max_length = 30)
	about = models.TextField(blank=True)
	races_participated = models.IntegerField()
	races_won = models.IntegerField()
	date_of_getting_driving_licens = models.DateField()
	reg_date = models.DateTimeField()
	profile_pic = models.CharField(default="https://icon-library.net/images/profile-icon-white/profile-icon-white-3.jpg", max_length = 250)
	status = models.CharField(default='False', max_length = 10, choices = STATUS_CHOICES)

	def __str__(self):
		return self.name