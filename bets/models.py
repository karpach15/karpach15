from django.db import models
from drivers.models import Drivers

class Stakes(models.Model):
	drivers_list = Drivers.objects.order_by('-races_won')
	DRIVERS_CHOICES = []
	for driver in drivers_list:
		DRIVERS_CHOICES.append((driver.name, driver.name + ' ' + driver.surname),)

	name = models.CharField(max_length = 50, choices = DRIVERS_CHOICES)
	stake = models.FloatField()
	expected_winner_name = models.CharField(max_length = 50)
	expected_winner_surname = models.CharField(max_length = 50)