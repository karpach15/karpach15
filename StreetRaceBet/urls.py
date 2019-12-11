from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('main.urls')),
	path('drivers/', include('drivers.urls')),
	path('bets/', include('bets.urls')),
	path('account_profile/', include('account_profile.urls')),
	path('races/', include('races.urls')),
]