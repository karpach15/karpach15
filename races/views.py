from django.shortcuts import render
from races.models import Past_Races, Future_Races

def races(request):
	past_races_list = Past_Races.objects.order_by('-time_date')
	future_races_list = Future_Races.objects.order_by('-time_date')
	current_jackpot = 35
	return render(request, 'races/races.html', {'page': 'races', 'account_pic': request.session['account_pic'], 'past_races_list': past_races_list, 'future_races_list': future_races_list, 'current_jackpot': current_jackpot})