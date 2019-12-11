from django.shortcuts import render
from drivers.models import Drivers
from django.utils import timezone

def drivers(request):
	drivers_list = Drivers.objects.order_by('-races_won')
	return render(request, 'drivers/drivers.html', {'page': 'drivers', 'account_pic': request.session['account_pic'], 'drivers_list': drivers_list})

def driver_reg(request):
	return render(request, 'drivers/register.html', {'notification': False, 'page': 'drivers', 'account_pic': request.session['account_pic']})

def reg_result(request):
	name = request.POST['name']
	surname = request.POST['surname']
	about = request.POST['about']
	date_of_getting_driving_licens = request.POST['date_of_getting_driving_licens']
	profile_pic = request.POST['profile_pic']

	a = Drivers(name = name, surname = surname, about = about, races_participated = 0, races_won = 0, date_of_getting_driving_licens = date_of_getting_driving_licens, reg_date = timezone.now(), profile_pic = profile_pic, status = False)
	a.save()

	return render(request, 'drivers/reg_result.html')