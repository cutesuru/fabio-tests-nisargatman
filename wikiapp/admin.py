from django.contrib import admin

# Register your models here.
from .models import Continent,Country,City

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)