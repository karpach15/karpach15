from django.shortcuts import render
from races.models import Future_Races

def bets(request):
	races_list = Future_Races.objects.order_by('-time_date')
	return render(request, 'bets/bets.html', {'page': 'bets', 'account_pic': request.session['account_pic'], 'races_list': races_list})

def bet_confirm(request):
	return render(request, 'bets/bet_confirm.html', {'page': 'bets', 'account_pic': request.session['account_pic'], 'notification': False})