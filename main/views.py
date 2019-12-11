from django.shortcuts import render

def index(request):
	return render(request, 'main/homePage.html', {'page': 'main', 'account_pic': request.session['account_pic']})