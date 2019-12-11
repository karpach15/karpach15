from django.db import models

class Past_Races(models.Model):
	race_name = models.CharField(max_length = 120)
	time_date = models.DateTimeField()
	start = models.CharField(max_length = 120)
	finish = models.CharField(max_length = 120)
	distance = models.FloatField(max_length = 50)
	base_stake = models.FloatField()
	jackpot = models.FloatField()
	winner = models.CharField(max_length = 120)
	drivers = models.IntegerField()
	stakes = models.IntegerField()

	def __str__(self):
		return self.race_name

class Future_Races(models.Model):
	race_name = models.CharField(max_length = 120)
	time_date = models.DateTimeField()
	start = models.CharField(max_length = 120)
	finish = models.CharField(max_length = 120)
	distance = models.FloatField(max_length = 50)
	base_stake = models.FloatField()
	drivers = models.IntegerField()
	stakes = models.IntegerField()

	def __str__(self):
		return self.race_name