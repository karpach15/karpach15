from django.shortcuts import render
from .models import Account_profile
from django.utils import timezone
from django.http import HttpResponseRedirect

def account_profile(request):
	if request.GET:
		login = request.GET['login']
		password = request.GET['password']
		
		account_list = Account_profile.objects.all()
		for profile in account_list:
			if login == profile.login and password == profile.password:
					request.session['user'] = login
					request.session['account_pic'] = profile.account_pic
					return HttpResponseRedirect('/account_profile/')
			else:
				return HttpResponseRedirect('/account_profile/login')
	if request.session['user'] != '':
		return render(request, 'account_profile/account_profile.html', {'page': 'account_profile', 'account_pic': request.session['account_pic'], 'notification': False})
	else:
		return HttpResponseRedirect('/account_profile/login')

def login(request):
	if request.session['user'] != '':
		return HttpResponseRedirect('/account_profile/')
	else:
		return render(request, 'account_profile/account_login.html', {'page': 'account_profile', 'account_pic': request.session['account_pic'], 'notification': False})

def register(request):
	if request.POST:
		account_name = request.POST['account_name']
		account_surname = request.POST['account_surname']
		login = request.POST['login']
		password = request.POST['password']
		account_pic = request.POST['account_pic']
		password_repeat = request.POST['password_repeat']
		if account_pic == '':
			account_pic = '../main/profile_icon.png'

		if password == password_repeat:
			a = Account_profile(
				account_name = account_name,
				account_surname = account_surname,
				login = login,
				password = password,
				account_create_date = timezone.now(),
				account_pic = account_pic)
			a.save()

			return HttpResponseRedirect('../login')

	return render(request, 'account_profile/account_register.html', {'page': 'account_profile','account_pic': request.session['account_pic'], 'notification': False})

def logout(request):
	request.session['user'] = ''
	request.session['account_pic'] = ''
	return HttpResponseRedirect('/account_profile/login')