from django.contrib import admin
from races.models import Past_Races, Future_Races

admin.site.register(Past_Races)
admin.site.register(Future_Races)